module constante
implicit none
save
real*8,parameter :: pi=3.141592654 !pi (le real*8 nous donne le nombre de chiffres après la virgule prise)
real*8,parameter :: mu=3.98600E5 !GMearth (km^3/s^2) [Constante gravitationnell x Masse du corps]
real*8,parameter :: RT=6398.14 !Rayon Terre (km)
real*8,parameter :: enrad=pi/180.0 !Convertir degré en rad
real*8,parameter :: endeg=180.0/pi !Convertir rad en degré
end module constante


subroutine readTLE(sma,ecc,inc,Om,omega,M0,nn,epoch,aa) !Demi-Grand axe/Excentricité/Inclinaison/Longitude du noeud ascendant/Argument du périgée/Anomalie MOYENNE/époque/année
use constante
implicit none
real*8, intent(out) :: sma,ecc,inc,Om,omega,M0,epoch !Ceux sont les variables de sorties, pour les variables d'entrées, on fait "intent(in) :: ....."
real*8 :: nn,day !nn=Mean motion, le moyen mouvement
integer :: e
integer, intent(out) :: aa
read(*,'(18x,i2,f12.8)') aa,day !(1ère ligne du INPUT:[On passe 18position x,la valeur un entier sur 2 positions i2, la valeur est un float avec f12(nombre de position en comptant les chiffres après la virgule).8 chiffres après la virgule])
read(*,'(9x,f7.4,x,f8.4,x,i7,2x,f7.4,x,f8.4,x,f11.8)') inc,Om,e,omega,M0,nn
ecc=e*1E-7 !e=Eccentricité
nn=nn*2.0*pi !Mean motion (révolutions/jour), comme le mu est en (km^3/s^2), on converti nn en (rad/s)=(revo*2pi/86400) 86400=secondes en 1journée
sma=(mu/nn**2)**(1.0/3.0) !1.0 car Fortran peut faire apparaître des valeurs si on mets pas le 1.0
inc=inc*enrad !convertir en rad car dans la formule de Newton tout est en RADIAN
Om=Om*enrad
omega=omega*enrad
M0=M0*enrad
if (aa==20) then !Pour une époque de référence au 01/01/2020
    epoch=day
endif
if (aa==21) then
    epoch=day+366.0
endif
end subroutine readTLE



subroutine anomecc(ecc,M,E) !Calcul anomalie Excentrique avec formule de Kepler
use constante
implicit none
real*8, intent(in) :: ecc,M
real*8, intent(out) :: E
integer :: i
E=M !Etape d'initialisation, on définit le E0,la valeur de départ
do i=1,3 !Répétez l'étape 3 fois le calcul ci-dessous
    E=E-((E-ecc*sin(E)-M)/(1.0-ecc*cos(E))) !print*, i,E [On affiche la valeur de E à chaque fois qu'on l'étape, donc on aura E pour 6 valeurs]
enddo
end subroutine anomecc  !Comme on a une ANOMALIE NORMALE ET EXCENTRIQUE (M et ecc) déjà faible, ça varie très peu, on est déjà proche de la tangeante


subroutine vecteur(xC,yC,zC,sma,ecc,inc,Om,omega,M,Aecc,epoch,nn) ! Cacul des éléments orbitaux obtenus dans le TLE en vecteur avec le calcul matriciel
use constante
implicit none
real*8 :: X,Y,Z,xA,yA,zA,xB,yB,zB,Aecc
real*8, intent(in) :: sma,ecc,inc,Om,omega,M,nn,epoch
real*8, intent(out) :: xC,yC,zC
call anomecc(ecc,M,Aecc)
X= Sma*(cos(Aecc)-ecc)
Y= Sma*sqrt(1.0-ecc**2)*sin(Aecc) ! X Y Z nous ont été données dans le PPT
Z= 0.0 !Comme on est dans un plan à 3 dimensions, on a 3 rotation R1 R2 et R3 a effectué pour convertir nos X Y Z en vecteur position (xC,yC,zC)

xA= cos(omega)*X - sin(omega)*Y !Ici, on fait la 1ère rotation, avec l'argument du périgée (omega)
yA= sin(omega)*X + cos(omega)*Y
zA= Z


xB= xA ! Ici, on a effectué la 2ème rotation avec l'inclinaison (inc)
yB= cos(inc)*yA - sin(inc)*zA
zB= sin(inc)*yA + cos(inc)*zA


xC= cos(Om)*xB - sin(Om)*yB ! Ici, on a effectué la 3-me rotation, avec la longitude du noeud ascendant (Om)
yC= sin(Om)*xB + cos(Om)*yB
zC = zB
end subroutine vecteur



subroutine latitude(xC,yC,zC,phiprim,r,phi)
use constante
implicit none
real*8,intent(in) :: xC,yC,zC
real*8,intent(out) :: phiprim,r,phi
r= sqrt((xC**2.0)+(yC**2.0)+(zC**2.0))
phiprim= asin(zC/r)
phi= atan(tan(phiprim)/(1.0-0.0033528**2.0))
phi= phi*endeg ! On convertit phi, la latitude géographique =/= latitude géocentrique phiprim, en degré
end subroutine latitude


subroutine longitude(xC,yC,lambda,alpha,t,teta)
use constante
implicit none
real*8,intent(in) :: xC,yC,t
real*8,intent(out) :: lambda,alpha,teta
alpha = atan2(yC,xC)
teta = 0.177834888 + 6.300387958*(t-275.0) ! teta est l'angle entre le méridian de greenwich GMST et la localisation du point choisit
do while (teta>pi)
    teta = teta - (2.0*pi)
enddo
do while (teta<(-pi))
    teta = teta + (2.0*pi) ! En faisant ça, on obtient l'angle teta sur un intervalle [pi;-pi]
enddo
lambda = (alpha - teta)
do while (lambda>pi)
    lambda = lambda - (2.0*pi)
enddo
do while (lambda<(-pi))
    lambda = lambda + (2.0*pi)
enddo
lambda = lambda*endeg ! On convertit la longitude en degré, afin de pouvoir tracer les points de chaque coordonnées sur une carte
end subroutine longitude


program main
use constante !On fait appelle aux constante, comme ça pas besoin de les redéfinir
implicit none ! OBLIGER à chaque nouvel algortihme
real*8 :: sma,ecc,inc,Om,omega,M0,nn,epoch,Aecc,M,t,annee
real*8 :: xC,yC,zC,X,Y,Z,phiprim,r,phi,lambda,alpha,teta
integer :: aa
call readTLE(sma,ecc,inc,Om,omega,M0,nn,epoch,aa) !On utilise call afin d'utiliser la subroutine

write(*,*) 'On obtient la position en coordonnées cartésiennes du satellite (x,y,z) tel que:'
write(*,*) 'x=',xC
write(*,*) 'y=',yC
write(*,*) 'z=',zC
write(*,*) 'Année (années)                       :',aa+2000
write(*,*) 'Jour (jours)                         :',epoch
write(*,*) 'Inclinaison (°degré)                 :',inc*endeg
write(*,*) 'Excentricité                         :',ecc
write(*,*) 'Argument du périgée (°degré)         :',omega*endeg
write(*,*) 'Longitude du noeud ascendant (°degré):',Om*endeg
write(*,*) 'Moyen Mouvement (Rad/jour)           :',nn
write(*,*) 'Demi Grand Axe (km)                  :',sma


T= (24.0/16.0) ! T est la période, c'est le temps que prend l'ISS pour faire un tour complet de la Terre, et l'ISS fait environ 16 tours autour de la Terre en 24h
t=epoch
do while ((t-epoch) < T)
    M = M0 + (nn*(t-epoch)) ! M0 est le seul élément qui est défini à l'époque, le M ici varie constamment au cours du temps
    call anomecc(ecc,M,Aecc)
    call vecteur(xC,yC,zC,sma,ecc,inc,Om,omega,M,Aecc,epoch,nn)
    call latitude(xC,yC,zC,phiprim,r,phi)
    call longitude(xC,yC,lambda,alpha,t,teta)
    t=t + (1.0/720.0) ! Ici, on fait un pas de 2min, mais comme t est en jours, on convertit 2min en jours
    print*,lambda,phi,(t-epoch)
enddo

end program main

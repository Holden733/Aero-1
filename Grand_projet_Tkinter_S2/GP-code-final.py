# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 01:58:51 2021
"""
import tkinter as tk                     
from tkinter import * 
from pandas import DataFrame
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time


 
programme = tk.Tk()
programme.title("Flight Analyses System")
programme.geometry("720x480")
###-----------------------------------------------------Partie1-------------------------------------------------------------------------
#Fonction
def login():
    a = 0
    i = 0
    df=pd.read_csv("user_info.csv",delimiter=(","))
    df2=pd.read_csv("user_login.csv")
    confirmation = 0
    for csv_email in df['email']:
        i=i+1
        if str(csv_email)== Entree1.get():
            numero = i-1
            password = df['password']
            if str(password[numero]) == Entree2.get():
                confirmation = 1
                break
    if confirmation == 1:
        affichage_resultat1 = tk.Label(o1, text="Bienvenue dans le système d’analyses !")
        affichage_resultat1.grid(column=1, row=5)
        affichage_resultat1.after(3000, affichage_resultat1.destroy)        
        print('oui')
        maj = {'number': i, 'email': Entree1.get(), 'date': time.strftime("%d/%m/%y"), 'time': time.strftime("%H:%M:%S")}
        print(i)
        for csv_email in df2['email']:
            if str(csv_email)== Entree1.get():
                email = df2[df2['email']== Entree1.get()].index
                df2 = df2.drop(email)
            else:
                df2 = df2
        df2 = df2.append(maj, ignore_index = True)
        df2.to_csv('user_login.csv', index = False)
        
    else:
        print('non')
        affichage_resultat2 = tk.Label(o1, text="Pas un utilisateur valide !")
        affichage_resultat2.grid(column=1, row=5)
        affichage_resultat2.after(3000, affichage_resultat2.destroy)        
                    

def signup():
    a = 0
    i = 0
    df=pd.read_csv("user_info.csv",delimiter=(","))
    confirmation=0
    for csv_email in df['email'] :
        i+=1
        if str(csv_email) == Entree3.get() :
            numero = i-1
            password = df['password']
            #print(numero)
            if str(password[numero]) == Entree4.get():
                confirmation = 1
    if confirmation == 1:
        affichage_resultat1 = tk.Label(o1, text=" E-mail déjà inscrit !")
        affichage_resultat1.grid(column=1, row=9)
        affichage_resultat1.after(3000, affichage_resultat1.destroy)
       
    else:
        new_email= Entree3.get()
        new_password = Entree4.get()
        affichage_resultat2 = tk.Label(o1, text="Nouvel utilisateur enregistré !")
        affichage_resultat2.grid(column=1, row=9)
        affichage_resultat2.after(3000, affichage_resultat2.destroy)
        df2 = {'number': i, 'email': new_email, 'password' : new_password}
        df = df.append(df2, ignore_index = True)
        df.to_csv('user_info.csv',index=False)  
        print(i)

            
#Création de la barre d'onglets
Onglets = ttk.Notebook(programme)
Onglets.place(relwidth=1, relheight=1)
#Onglets.geometry("720x360")
o1 = ttk.Frame(Onglets)
o1.pack()
o2 = ttk.Frame(Onglets)
o2.pack()
o3 = ttk.Frame(Onglets)
o3.pack()
Onglets.add(o1, text="LOGIN")
Onglets.add(o2, text="PASSENGERS")
Onglets.add(o3, text="FLIGHT VISUALIZATION")


#Ajout des labels
label1 = Label(o1, text='Welcome to Flight Analyses System',font=("courier",20))
label1.grid(row = 0, column= 1)
label2 = Label(o1, text='Email:',font=("courier",10),bg='blue')
label2.grid(row = 1, column= 0)
label3 = Label(o1, text='Password:',font=("courier",10),bg='blue')
label3.grid(row = 2, column= 0)
label4 = Label(o1, text='Email:',font=("courier",10),bg='yellow')
label4.grid(row = 6, column= 0)
label5 = Label(o1, text='Password:',font=("courier",10),bg='yellow')
label5.grid(row = 7, column= 0)
#Ajout des entrées
Entree1 = Entry(o1)
Entree1.grid(row = 1, column= 1)
Entree2 = Entry(o1)
Entree2.grid(row = 2, column= 1)
Entree3 = Entry(o1)
Entree3.grid(row = 6, column= 1)
Entree4 = Entry(o1)
Entree4.grid(row = 7, column= 1)
#Création des boutons
bouton1 = Button(o1, text='LOGIN', font=("courier",10),bg='blue', command=login)
bouton1.grid(row = 4, column= 1)
bouton2 = Button(o1, text='SIGNUP', font=("courier",10),bg='yellow', command=signup)
bouton2.grid(row = 8, column= 1)





###---------------------------------------------------------------Partie2--------------------------------------------------------------------
#Fonction
def liste():
    i=0
    df = pd.read_csv('passenger_info.csv', delimiter=(","))
    confirmation = 0
    for airline in df['Airline']:
        i+=1
        if str(airline) == spinbox1.get():
            numero = i-1
            destination = df['Destination']
            prix = df['Price']
            #print("aero")
            if str(destination[numero]) == spinbox2.get():
                #print('')
                if str(prix[numero]) == spinbox3.get():
                    print('gg')
                    confirmation = 1
                    passengersid= df['PassengerID']
                    a = str(passengersid[numero])
                    nom = df['Lastname']
                    b = str(nom[numero]) 
                    terminal = df['Terminal']
                    c = str(terminal[numero])
                    zone = df['Boarding Area']
                    d = str(zone[numero])
                    affichage = tableau.insert(parent='', index=0, text='', values=(a,b,c,d))
                 
                
                    
                    

#Label
titre = Label(o2,text='Passenger information',font=("courier",15))
titre.grid(row = 3, column= 5)
label = Label(o2, text="                  ", font=("arial italic", 18) )
label.grid(column=1, row=1)

#Bouton
liste = ttk.Button(o2, text="List passenger", command=liste)

liste.grid(row = 3, column= 1)

 
#Tableau
tableau = ttk.Treeview(o2, columns=('Passengerid', 'Lastname', 'Terminal','BoardingArea'))
tableau.heading('Passengerid', text='Passengerid')
tableau.heading('Lastname', text='Lastname')
tableau.heading('Terminal', text='Terminal')
tableau.heading('BoardingArea', text='Boarding Area')
tableau['show'] = 'headings'
tableau.grid(row = 4, column= 5)

#Menu deroulant
df = pd.read_csv('passenger_info.csv', delimiter=(","))

company = list(set(df['Airline']))
destination = list(set(df['Destination']))
price= list(set(df['Price']))


spinbox1 = ttk.Spinbox(o2, values=company)
spinbox1.grid(column=1, row=2)

spinbox2 = ttk.Spinbox(o2, values=destination )
spinbox2.grid(column=2, row=2)

spinbox3 = ttk.Spinbox(o2, values=price )
spinbox3.grid(column=3, row=2)


###-------------------------------------------Partie3-----------------------------------------------------------
##__________________________________________Affichage1__________________________________________________________

#Lecture fichier
dd = pd.read_csv('flight_info.csv', delimiter=',')

#Création tableau 
tv = ttk.Treeview(o3)
tv['columns']=('Year','Month','DayofMonth','DayOfWeek','FlightDate','FlightNum','OriginAirportID','OriginCityName','OriginState','OriginStateName','DestAirportID','DestCityName','DestState','DestStateName','DepTime','DepDelayMinutes','ArrTime','ArrDelayMinutes','AirTime','Distance')
#Entete
tv.heading('#0', text='', anchor=CENTER)
tv.heading('Year', text='Year', anchor=CENTER)
tv.heading('Month', text='Month', anchor=CENTER)
tv.heading('DayofMonth', text='DayofMonth', anchor=CENTER)
tv.heading('DayOfWeek', text='DayOfWeek', anchor=CENTER)
tv.heading('FlightDate', text='FlightDate', anchor=CENTER)
tv.heading('FlightNum', text='FlightNum', anchor=CENTER)
tv.heading('OriginAirportID', text='OriginAirportID', anchor=CENTER)
tv.heading('OriginCityName', text='OriginCityName', anchor=CENTER)
tv.heading('OriginState', text='OriginState', anchor=CENTER)
tv.heading('OriginStateName', text='OriginStateName', anchor=CENTER)
tv.heading('DestAirportID', text='DestAirportID', anchor=CENTER)
tv.heading('DestCityName', text='DestCityName', anchor=CENTER)
tv.heading('DestState', text='DestState', anchor=CENTER)
tv.heading('DestStateName', text='DestStateName', anchor=CENTER)
tv.heading('DepTime', text='DepTime', anchor=CENTER)
tv.heading('DepDelayMinutes', text='DepDelayMinutes', anchor=CENTER)
tv.heading('ArrTime', text='ArrTime', anchor=CENTER)
tv.heading('ArrDelayMinutes', text='ArrDelayMinutes', anchor=CENTER)
tv.heading('AirTime', text='AirTime', anchor=CENTER)
tv.heading('Distance', text='Distance', anchor=CENTER)
#Colonnes
tv.column('#0', width=0, stretch=NO)
tv.column('Year', anchor=CENTER, width=40)
tv.column('Month', anchor=CENTER, width=55)
tv.column('DayofMonth', anchor=CENTER, width=80)
tv.column('DayOfWeek', anchor=CENTER, width=80)
tv.column('FlightDate', anchor=CENTER, width=80)
tv.column('FlightNum', anchor=CENTER, width=80)
tv.column('OriginAirportID',anchor=CENTER, width=80 )
tv.column('OriginCityName', anchor=CENTER, width=80)
tv.column('OriginState', anchor=CENTER, width=80)
tv.column('OriginStateName', anchor=CENTER, width=80)
tv.column('DestAirportID',anchor=CENTER, width=80)
tv.column('DestCityName', anchor=CENTER, width=80)
tv.column('DestState', anchor=CENTER, width=80)
tv.column('DestStateName', anchor=CENTER, width=80)
tv.column('DepTime',anchor=CENTER, width=80)
tv.column('DepDelayMinutes',anchor=CENTER, width=80)
tv.column('ArrTime', anchor=CENTER, width=80)
tv.column('ArrDelayMinutes', anchor=CENTER, width=80)
tv.column('AirTime', anchor=CENTER, width=80)
tv.column('Distance', anchor=CENTER, width=80)
#Lignes
dd1 = dd['Year']
dd2 = dd['Month']
dd3 = dd['DayofMonth']
dd4 = dd['DayOfWeek']
dd5 = dd['FlightDate']
dd6 = dd['OriginAirportID']
dd7 = dd['OriginCityName']
dd8 = dd['OriginState']
dd9 = dd['OriginStateName']
dd10 = dd['DestAirportID']
dd11 = dd['DestCityName']
dd12 = dd['DestState']
dd13 = dd['DestStateName']
dd14 = dd['DepTime']
dd15 = dd['DepDelayMinutes']
dd16 = dd['ArrTime']
dd17 = dd['ArrDelayMinutes']
dd18 = dd['AirTime']
dd19 = dd['Distance']
#Condition
len(dd1)
a = 0
while a < len(dd1):
    tv.insert(parent='', index=a, iid=a, text='', values=(dd1[a],dd2[a],dd3[a],dd4[a],dd5[a],dd6[a],dd7[a],dd8[a],dd9[a],dd10[a],dd11[a],dd12[a],dd13[a],dd14[a],dd15[a],dd16[a],dd17[a],dd18[a],dd19[a]))
    a += 1
tv.place(relx=0,rely=0,relwidth=1, relheight=0.2)


#Graphique1

data1= {"Pays1":['                        Arizona',
                 '                       Texas',
                 '                      Florida',
                 '                     North California',
                 '                    California',
                 '                   Pensylvania',
                 '                  Washington',
                 '                 Nevada',
                 '                Georgia',
                 '               Virginia',
                 '              Wisconsin',
                 '             Ohio',
                 '            Illinois',
                 '           Missouri',
                 '          Nebraska',
                 '         Indiana',
                 '        Utha',
                 '       Massachusettes',
                 '      Hawaii',
                 '     New York',
                 '    Iowa',
                 '   Minnesota',
                 '  Colorado',
                 ' Oregon',
                 'Maryland'],
"DestStateName":[1066,466,286,226,160,120,88,72,72,64,60,56,56,52,32,24,20,16,16,12,8,8,2.4,1.6,0.8]}
df1 = DataFrame(data1, columns=["Pays1","DestStateName"])
figure1 = plt.Figure(figsize=(4,4), dpi=80)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, o3)
bar1.get_tk_widget().place(relx=0,rely=0.2,relwidth=0.25, relheight=0.7)
df1 = df1[["Pays1","DestStateName"]].groupby("Pays1").sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Le nombre de vols vers différentes destinations')

#Graphique2
data2= {"Pays2":['                        Arizona',
                 '                       California',
                 '                      Colorado',
                 '                     Florida',
                 '                    Georgia',
                 '                   Hawaii',
                 '                  Illinois',
                 '                 Indiana',
                 '                Iowa',
                 '               Maryland',
                 '              Massachusetts',
                 '             Minesota',
                 '            Missouri',
                 '           Nebraska',
                 '          Nevada',
                 '         New York',
                 '        North Californa',
                 '       Ohio',
                 '      Oregon',
                 '     Pensylvania',
                 '    Texas',
                 '   Utha',
                 '  Virginia',
                 ' Washington',
                 'Wisconsin'],
"DepDelayMinutes":[10825,2018,183,1697,825,275,871,321,91,45,27,137,229,183,642,183,1284,871,0,1284,4495,458,733,917,183]}
df2 = DataFrame(data2, columns=["Pays2","DepDelayMinutes"])
figure2 = plt.Figure(figsize=(4,4), dpi=80)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, o3)
bar2.get_tk_widget().place(relx=0.25,rely=0.2,relwidth=0.25, relheight=0.7)
df2 = df2[["Pays2","DepDelayMinutes"]].groupby("Pays2").sum()
df2.plot(kind='bar', legend=True, ax=ax2,color='r')
ax2.set_title('Comparaison des délais avec la destination 1')
rects2 = ax2.patches
pourcentage2=['38.57%','7.31%','0.31%','6.17%','2.73%','0.86%','2.76%','1.02%','0.13%','0.08%','0.07%','0.23%','0.78%','0.64%','2.24%','0.62%','4.41%','2.83%','0.0%','4.58%','15.93%','1.45%','2.51%','3.19%','0.59%']
for x2, y2 in zip(rects2, pourcentage2):
    height = x2.get_height()
    ax2.text(x2.get_x() + x2.get_width() / 2, height + 5, y2 ,ha='center', va='bottom',fontsize=7, color='blue', fontweight='bold')


#Graphique3
data3= {"Pays3":['                        Arizona',
                 '                       California',
                 '                      Colorado',
                 '                     Florida',
                 '                    Georgia',
                 '                   Hawaii',
                 '                  Illinois',
                 '                 Indiana',
                 '                Iowa',
                 '               Maryland',
                 '              Massachusetts',
                 '             Minesota',
                 '            Missouri',
                 '           Nebraska',
                 '          Nevada',
                 '         New York',
                 '        North Californa',
                 '       Ohio',
                 '      Oregon',
                 '     Pensylvania',
                 '    Texas',
                 '   Utha',
                 '  Virginia',
                 ' Washington',
                 'Wisconsin'],
"ArrDelayMinutes":[12000,3052,105,2000,842,421,631,210,52,31,0,105,421,105,1578,210,2000,1157,0,2000,6842,947,1052,1263,210]}
df3 = DataFrame(data3, columns=["Pays3","ArrDelayMinutes"])
figure3 = plt.Figure(figsize=(4,4), dpi=80)
ax3 = figure3.add_subplot(111)
bar3 = FigureCanvasTkAgg(figure3, o3)
bar3.get_tk_widget().place(relx=0.5,rely=0.2,relwidth=0.25, relheight=0.7)
df3 = df3[["Pays3","ArrDelayMinutes"]].groupby("Pays3").sum()
df3.plot(kind='bar', legend=True, ax=ax3,color='r')
ax3.set_title('Comparaison des délais avec la destination 2')
rects3 = ax3.patches
pourcentage3=['39.3%','10.01%','0.26%','6.66%','2.84%','1.49%','2.1%','0.8%','0.09%','0.09%','0.01%','0.23%','0.75%','0.29%','3.14%','0.4%','3.95%','2.31%','0%','3.92%','14.25%','1.78%','2.12%','2.69%','0.51%']
for x3, y3 in zip(rects3, pourcentage3):
    height = x3.get_height()
    ax3.text(x3.get_x() + x3.get_width() / 2, height + 5, y3,ha='center', va='bottom',fontsize=7, color='blue', fontweight='bold')

#Graphique4
data4= {"Pays4":['              Hawaii',
                 '             Arizona',
                 '            California',
                 '           North California',
                 '          Nevada',
                 '         Ohio',
                 '        Virginia',
                 '       Florida',
                 '      Minnesota',
                 '     Indiana',
                 '    Texas',
                 '   Wisconsin',
                 '  Illinois',
                 ' Nebraska',
                 'Pensylvania'],
"Distance":[2818,2818,2272,2272,2159,1977,1954,1943,1500,1477,1454,1454,1431,1318,1295]}
df4 = DataFrame(data4, columns=["Pays4","Distance"])
figure4 = plt.Figure(figsize=(4,4), dpi=80)
ax4 = figure4.add_subplot(111)
bar4 = FigureCanvasTkAgg(figure4, o3)
bar4.get_tk_widget().place(relx=0.75,rely=0.2,relwidth=0.25, relheight=0.7)
df4 = df4[["Pays4","Distance"]].groupby("Pays4").sum()
df4.plot(kind='bar', legend=True, ax=ax4)
ax4.set_title('Top 15 des vols')


programme.mainloop()

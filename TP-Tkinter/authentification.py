import tkinter                     
from tkinter import * 
from pandas import DataFrame
import pandas as pd
from tkinter import ttk
import webbrowser
import accueil as a
import tkinter as tk                     
import pandas as pd
import webbrowser
from tkinter import messagebox
import accueil as a
import trajet as t
import graph as g
import authentification as au


def authentification():
    connect = Tk()
    connect.withdraw()
    top = Toplevel(connect)
    top.title("Connexion")
    top.geometry("760x480")
    top.config(bg='black')

    def accueil(): 
        ac = Tk()
        ac.title("Accueil")
        ac.geometry("720x480")
        ac.config(bg='black')
     
        def textparcours1() :
            if choix.get() == 1:
                t.textuel_trajet1()
            elif choix.get()==2:
                t.textuel_trajet2()
            elif choix.get() ==3:
                t.textuel_trajet3()

        def graphparcours1():
            if choix.get() ==1:
                g.graph_trajet1()
            elif choix.get()==2:
                g.graph_trajet2()
            elif choix.get() ==3:
                g.graph_trajet3()

        def deco():
            ac.destroy()
            top.deiconify()
            messagebox.showwarning(title='Attention', message='Vous etes deconnecte')
            Entree1.delete(0,END)
            Entree2.delete(0,END)
                
        
        def activateparcours1():
            if choix.get() == 1:
                bouton1.config(state='active')
                bouton2.config(state='active')
            else:
                bouton1.config(state='disabled')
                bouton2.config(state='disabled')
        def activateparcours2():
            if choix.get() == 2:
                bouton1.config(state='active')
                bouton2.config(state='active')
            else:
                bouton1.config(state='disabled')
                bouton2.config(state='disabled')
        def activateparcours3():
            if choix.get() == 3:
                bouton1.config(state='active')
                bouton2.config(state='active')
            else:
                bouton1.config(state='disabled')
                bouton2.config(state='disabled')
        #Label       
        label1 = Label(ac, text='Accueil',font=("courier",40),bg='black',fg='#d3c04d')
        label1.place(x=200, y=0)

        #Boutons
        choix = IntVar()
        case1= Checkbutton(ac,text="parcours 1",font=("courier",10),variable=choix, onvalue=1, offvalue=0,bg='black',fg='#d3c04d', command = activateparcours1)
        case1.place (x=20, y=100)
        case2= Checkbutton(ac,text="parcours 2",font=("courier",10), variable=choix,onvalue=2,offvalue=0,bg='black',fg='#d3c04d',command = activateparcours2)
        case2.place(x=20, y=200)
        case3= Checkbutton(ac,text="parcours 3",font=("courier",10), variable=choix,onvalue=3,offvalue=0,bg='black',fg='#d3c04d',command = activateparcours3)
        case3.place(x=20, y=300 )

        bouton1 = Button(ac,text='Affichage textuel', command= textparcours1, state='disabled',font=("courier",10),activebackground="black", activeforeground="#d3c04d",bg='black',fg='#d3c04d')
        bouton1.place(x=400, y=100)
        bouton2 = Button(ac,text='Affichage graphique', command= graphparcours1,state='disabled',font=("courier",10),activebackground="black", activeforeground="#d3c04d",bg='black',fg='#d3c04d')
        bouton2.place(x=400, y=200)
        bouton3 = Button(ac,text='Déconnexion', font=("courier",10),activebackground="#d3c04d", activeforeground="black",bg='black',fg='#d3c04d', command= deco)                 
        bouton3.place(x=400,y=300)

    
    def connexion():
        users = pd.read_json("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/users.json")
        i=0
        confirmation = 0
        for email in users['user']:
            i=i+1
            if str(email)== Entree1.get():
                numero = i-1
                mdp = users['password']
                if str(mdp[numero]) == Entree2.get():
                    confirmation = 1
                    break   
        if confirmation == 1:
            messagebox.showinfo(title='Confirmation', message= "Bonjour " + Entree1.get())
            top.withdraw()
            accueil()
            
            
        else:
            messagebox.showerror(title='Erreur', message='Email ou mot de passe incorrect')
            
            
            
    def ouvrir():        
            webbrowser.open_new("https://www.google.com/maps")

    label1 = Label(top, text="Connectez vous",font=("courier",30),bg='black',fg='#d3c04d')
    label1.place(relx=0,rely=0,relwidth=0.7, relheight=0.1)
    label2 = Label(top, text='Identifiant',font=("courier",20),bg='black',fg='#d3c04d')
    label2.place(relx=0,rely=0.2,relwidth=0.3, relheight=0.1)
    label3 = Label(top, text='Mot de passe',font=("courier",20),bg='black',fg='#d3c04d')
    label3.place(relx=0,rely=0.3,relwidth=0.3, relheight=0.1)

    Entree1 = Entry(top, font=15)
    Entree1.place(relx=0.5,rely=0.2,relwidth=0.4, relheight=0.1)
    Entree2 = Entry(top, font=15)
    Entree2.place(relx=0.5,rely=0.3,relwidth=0.4, relheight=0.1)

    bouton1 = Button(top, text='Connexion', font=("courier",10),fg='black',bg='#d3c04d', command= connexion)
    bouton1.place(relx=0.5,rely=0.5,relwidth=0.4, relheight=0.1)

    bouton2 = Button(top, text='Cliquez ici pour savoir où vous êtes !', font=("courier",10),bg='black',fg='#d3c04d', command=ouvrir)
    bouton2.place(relx=0.2,rely=0.8,relwidth=0.5, relheight=0.1)

    top.mainloop()
    
if __name__ == '__main__':
    authentification()
    



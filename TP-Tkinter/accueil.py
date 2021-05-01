import tkinter as tk                     
from tkinter import * 
from pandas import DataFrame
import pandas as pd
from tkinter import ttk
import webbrowser
from tkinter import messagebox
import accueil as a
import trajet as t
import graph as g
import authentification as au

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

        ac.mainloop()
    
    
    
if __name__ == '__main__':
    accueil()


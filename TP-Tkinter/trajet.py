import pandas as pa
import tkinter as tk
from tkinter import ttk

users = pa.read_json("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/users.json")
file1 = pa.read_csv("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/tracesGPS1.csv")
file2 = pa.read_csv("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/tracesGPS2.csv")
file3 =  pa.read_csv("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/tracesGPS3.csv")

def textuel_trajet1():
    #affichage textuel 1

    aff = tk.Tk()
    aff.title("affichage textuel du trajet")
    aff.geometry("400x700")
    aff.config(bg='black')

    frame = tk.Frame(aff,bg ="white")
    frame.place(relwidth = 1 ,relheight = 1)

    label = tk.Label(frame, text="coordonnées GPS du premier trajet",font=("courier",30),bg = "red")
    label.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.2)
    #def tableau
    tableau = ttk.Treeview(frame, columns=('latitude', 'longitude'))
    tableau['columns']=('latitude','longitude')
    #entetes
    tableau.heading('#0', text='')
    tableau.heading('latitude', text='latitude')
    tableau.heading('longitude', text='longitude')
    tableau['show'] = 'headings'

    #colonne 
    tableau.column('#0', width=0)
    tableau.column('latitude', width=40)
    tableau.column('longitude', width=55)

    #Lignes
    dd1 = file1['latitude']
    dd2 = file1['longitude']

    #Condition
    len(dd1)
    a = 0
    while a < len(dd1):
        tableau.insert(parent='', index=a, iid=a, text='', values=(dd1[a],dd2[a]))
        a += 1

    tableau.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.5)

    bouton = tk.Button(frame, text='Retour', font=("courier",15),bg="white")
    bouton.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)




def textuel_trajet2():
    #affichage textuel 2

    aff2 = tk.Tk()
    aff2.title("affichage textuel du trajet")
    aff2.geometry("400x700")
    aff2.config(bg='black')
    frame = tk.Frame(aff2,bg ="white")
    frame.place(relwidth = 1 ,relheight = 1)

    label = tk.Label(frame, text="coordonnées GPS du deuxième trajet",font=("courier",30),bg = "red")
    label.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.2)
    #def tableau
    tableau = ttk.Treeview(frame, columns=('latitude', 'longitude'))
    tableau['columns']=('latitude','longitude')
    #entetes
    tableau.heading('#0', text='')
    tableau.heading('latitude', text='latitude')
    tableau.heading('longitude', text='longitude')
    tableau['show'] = 'headings'

    #colonne 
    tableau.column('#0', width=0)
    tableau.column('latitude', width=40)
    tableau.column('longitude', width=55)

    #Lignes
    dd1 = file2['latitude']
    dd2 = file2['longitude']

    #Condition
    len(dd1)
    a = 0
    while a < len(dd1):
        tableau.insert(parent='', index=a, iid=a, text='', values=(dd1[a],dd2[a]))
        a += 1

    tableau.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.5)


    bouton = tk.Button(frame, text='Retour', font=("courier",15),bg="white")
    bouton.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)


def textuel_trajet3():
    #affichage textuel 3

    aff3 = tk.Tk()
    aff3.title("affichage textuel du trajet")
    aff3.geometry("400x700")
    aff3.config(bg='black')
    frame = tk.Frame(aff3,bg ="white")
    frame.place(relwidth = 1 ,relheight = 1)

    label = tk.Label(frame, text="coordonnées GPS du troisième trajet",font=("courier",30),bg = "red")
    label.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.2)
    #def tableau
    tableau = ttk.Treeview(frame, columns=('latitude', 'longitude'))
    tableau['columns']=('latitude','longitude')
    #entetes
    tableau.heading('#0', text='')
    tableau.heading('latitude', text='latitude')
    tableau.heading('longitude', text='longitude')
    tableau['show'] = 'headings'

    #colonne 
    tableau.column('#0', width=0)
    tableau.column('latitude', width=40)
    tableau.column('longitude', width=55)

    #Lignes
    dd1 = file3['latitude']
    dd2 = file3['longitude']

    #Condition
    len(dd1)
    a = 0
    while a < len(dd1):
        tableau.insert(parent='', index=a, iid=a, text='', values=(dd1[a],dd2[a]))
        a += 1

    tableau.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.5)

    bouton = tk.Button(frame, text='Retour', font=("courier",15),bg="white")
    bouton.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)

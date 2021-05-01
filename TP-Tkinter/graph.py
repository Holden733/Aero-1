import pandas as pa
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg








def graph_trajet1():
    file1 = pa.read_csv("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/tracesGPS1.csv")
    #graph1
    df = pa.DataFrame(file1)
    app = tk.Tk()
    app.geometry("350x200")
    app.title("représentation graphique des coordonnées GPS 1")
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    fig_canvas = FigureCanvasTkAgg(fig,app)
    fig_canvas.get_tk_widget().place(relwidth=1 , relheight=1)
    #config graphique
    img = plt.imread("SatIvry.png")
    ax.plot(df.longitude , df.latitude , color = "blue", marker = "<")
    ax.set_title("trajet 1")
    ax.set_xlabel("longitudes(°)")
    ax.set_ylabel("latitudes(°)")
    ax.imshow(img,extent = (2.382, 2.394, 48.811, 48.815))
    app.mainloop()




def graph_trajet2():
    file2 = pa.read_csv("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/tracesGPS2.csv")
    #praph 2
    df = pa.DataFrame(file2)
    app = tk.Tk()
    app.geometry("350x200")
    app.title("représentation graphique des coordonnées GPS 2")
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    fig_canvas = FigureCanvasTkAgg(fig,app)
    fig_canvas.get_tk_widget().place(relwidth=1 , relheight=1)
    #config graphique
    img = plt.imread("SatIvry.png")
    ax.plot(df.longitude , df.latitude , color = "blue", marker = "<")
    ax.set_title("trajet 2")
    ax.set_xlabel("longitudes(°)")
    ax.set_ylabel("latitudes(°)")
    ax.imshow(img,extent = (2.382, 2.394, 48.811, 48.815))
    app.mainloop()




def graph_trajet3():
    file3 =  pa.read_csv("https://raw.githubusercontent.com/JohvanyROB/IN121_2020_2021/main/tracesGPS3.csv")
    #praph 3
    img = plt.imread("SatIvry.png")
    df = pa.DataFrame(file3)
    app = tk.Tk()
    app.geometry("350x200")
    app.title("représentation graphique des coordonnées GPS 2")
    """
    frame = tk.Frame(app)
    frame.place(relwidth = 1,relheight = 1 )

    texte = tk.Text(frame,font=("arial",15))
    texte.insert(tk.INSERT, df.to_string(index=False))
    texte.place(relwidth=1,relheight=1)
    """
    fig = plt.Figure()
    ax = fig.add_subplot(111)
    fig_canvas = FigureCanvasTkAgg(fig,app)
    fig_canvas.get_tk_widget().place(relwidth=1 , relheight=1)

    #config graphique
    ax.plot(df.longitude , df.latitude , color = "blue", marker = "<")
    ax.set_title("trajet 3")
    ax.set_xlabel("longitudes(°)")
    ax.set_ylabel("latitudes(°)")
    ax.imshow(img,extent = (2.382, 2.394, 48.811, 48.815))
    app.mainloop()






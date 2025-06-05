import tkinter as tk


ventana = tk.Tk()
ventana.title("mi proyecto")
ventana.geometry("500x300")
ventana.geometry("500x300")
#con coordenadas de inicio
#ventana.geometry("500x300+500+400")# si lo agregamos asi con el primero movemos la pestaña en el eje x y con el segundo en el eje y

ventana.minsize(300,200)#minimo al hacer mas chico
ventana.maxsize(800,600)#maximo al hacer mas grande
ventana.iconbitmap("9_tkinter/favicon.ico")#agregar un icono a la ventana
ventana.configure(background="black")
# ventana.resizable(False,False) no deja agrandar la ventana ni vertical ni horizontal
# ventana.resizable(False,True) no deja agrandar horizontalmente
# ventana.resizable(True,False) no deja agrandar verticalmente

ventana.attributes(alpha=0.9) # transparencia cuanto mas chico el valor mas trasparente
ventana.mainloop()
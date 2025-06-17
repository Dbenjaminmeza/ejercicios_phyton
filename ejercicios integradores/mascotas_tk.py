import random 
import tkinter as tk
from fotos_mascota import imagen

# venatana
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("mascota virtual")

# recuadro
juego_presentacion = tk.Frame(ventana)
juego_presentacion.configure(width= 300, height= 200)
juego_presentacion.pack() 

juego = tk.Frame(ventana)
juego.configure(width= 300, height= 200)
juego.pack() 


class MascotaVirtual:
    def __init__(self,nombre):
        self.nombre = nombre






def presentacion_juego():
    global nombre
    etiqueta_inicio = tk.Label(juego_presentacion, text = "\n╔════════════════════════════════════╗\n       Bienvenido a tu primer       \n           mascota virtual!             \n╚════════════════════════════════════╝\n")
    etiqueta_inicio.pack()
    texto_nombre = tk.Label(juego_presentacion, text="por favor ingresa el nombre de tu mascota")
    texto_nombre.pack()
    nombre = tk.Entry(juego_presentacion)
    nombre.pack()
    return nombre


nombre = presentacion_juego()
boton_comenzar = tk.Button(juego_presentacion, text="comenzar", command=lambda: presentacion_de_mascota(nombre))
boton_comenzar.pack()

def presentacion_de_mascota(nombre):
    nombre = nombre.get()
    etiqueta_juego = tk.Label(juego,text = f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota! ║\n╚════════════════════════════════════╝\n\t Hola mi nombre es {nombre}                     ")
    etiqueta_juego.pack()
    foto_mascota = tk.Label(juego,text = "\n╔════════════════════════════════════╗\n║                                    ║\n║              ▄▀▄  ▄▀▄              ║\n║            ▄▀ ▄▀▄▀ ▄▀              ║\n║           ▄▀ ▀▄▀ ▄▀                ║\n║          ▄▀'^''^' ▀▄               ║\n║        ▄▀   ▄▀▄     ▀▄             ║\n║        ▀▄▄▄▀   ▀▄     ▀▄           ║\n║                 ▀      ▀           ║\n║                                    ║\n╚════════════════════════════════════╝\n")
    foto_mascota.pack()
    for i in juego_presentacion.winfo_children():
        i.destroy()





#----------------------------------- menu de opciones---------------------------------------#
def menu_opciones():
    etiqueta_juego = tk.Label(juego,text = "\n╔════════════════════════════════════╗\n       Opciones disponibles:        \n                                   \n 1 - Alimentar                      \n 2 - Jugar                             \n 3 - Mostrar informacion  \n 4 - Salir                               \n                                   \n╚════════════════════════════════════╝\n")
    etiqueta_juego.pack()

    #-----------------------------------botones acciones-------------------------------------------#
    boton_alimetar = tk.Button(juego, text="alimetar")
    boton_alimetar.pack()
    boton_jugar = tk.Button(juego, text="jugar")
    boton_jugar.pack()
    boton_mostar_info = tk.Button(juego, text="mostar_info")
    boton_mostar_info.pack()



#----------------------------------ejecutar ventana----------------------------------------------#
ventana.mainloop()
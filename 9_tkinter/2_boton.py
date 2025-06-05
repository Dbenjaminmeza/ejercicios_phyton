import tkinter as tk


def saludar():
    print("hola info")

ventana = tk.Tk()
ventana.title("boton de saludo")
ventana.geometry("400x300")

boton = tk.Button(ventana, text="saludar", font= ("arial",30), command=saludar)
boton.pack()

ventana.mainloop()
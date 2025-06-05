import tkinter as tk


ventana = tk.Tk()
ventana.title("ahora son 3 botones")
ventana.geometry("400x300")


boton_1 = tk.Button(ventana, text="boton 1")
boton_2 = tk.Button(ventana, text="boton 2")
boton_3 = tk.Button(ventana, text="boton 3")


boton_1.pack(side="top")

boton_2.pack(side="left")

boton_3.pack(side="bottom")

ventana.mainloop()
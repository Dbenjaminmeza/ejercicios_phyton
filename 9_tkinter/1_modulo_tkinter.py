import tkinter as tk
# Importar Tkinter: Importamos el módulo Tkinter y lo
# asignamos al alias tk.


# creamos una ventana principal
ventana = tk.Tk()
# Establecer el título: Usamos el método title() para
# asignar un título a la ventana.
ventana.title("mi primer programa tkinter")

ventana.geometry("400x400") #alto por ancho en pixeles


# Crear un label: Creamos un objeto Label que mostrará el
# texto "¡Hola, mundo!". El primer argumento es la variable
# ventana, el segundo argumento es el texto que

etiqueta = tk.Label(ventana, text = "hola mundo!", font= ("Arial",30))

# Empaquetar el label: Usamos el método pack() para
# colocar el label dentro de la ventana. Hay otros métodos
# como grid() y place() para organizar los elementos de una
# forma más precisa.

etiqueta.pack()

# Iniciar el bucle principal: mainloop() inicia el bucle
# principal de la aplicación, que se encarga de manejar los
# eventos del usuario y mantener la ventana abierta hasta
# que se cierre.

ventana.mainloop()
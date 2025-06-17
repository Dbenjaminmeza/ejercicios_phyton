import tkinter as tk

def limpiar_marco(marco):
    for widget in marco.winfo_children():
        widget.destroy()

root = tk.Tk()
mi_marco = tk.Frame(root)
mi_marco.pack()

# Crear algunos widgets de ejemplo dentro del marco
etiqueta = tk.Label(mi_marco, text="Etiqueta 1")
etiqueta.pack()
boton = tk.Button(mi_marco, text="Botón")
boton.pack()

# Botón para limpiar el marco
boton_limpiar = tk.Button(root, text="Limpiar Marco", command=lambda: limpiar_marco(mi_marco))
boton_limpiar.pack()

root.mainloop()
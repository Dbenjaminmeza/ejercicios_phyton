import tkinter as tk

# crear una ventana

ventana = tk.Tk()
ventana.title = "menu desplegable"
ventana.geometry = ("400x300")

# crear un menu
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu, tearoff= 0)
barra_menu.add_cascade(label="principal", menu= menu_principal)
sub_menu = tk.Menu(menu_principal, tearoff= 0)
menu_principal.add_cascade(label="opciones", menu=sub_menu)

# funcionapara opciones con menu

def saludar():
    print("hola info!")

# ejecutar la funcion

sub_menu.add_command(label="salir", command=ventana.quit)
sub_menu.add_command(label="saludar", command=saludar)

# mostrar la ventana
ventana.mainloop()




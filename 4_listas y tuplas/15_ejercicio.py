""" 13-Crear una lista con los nombres de tres colores y agregar dos colores
más al final de la lista. Mostrar la lista resultante. """


lista = ["rojo","azul","verde"]

for i in range(2):
    colores = input("ingresa un color: ")
    lista.append(colores)

print(lista)
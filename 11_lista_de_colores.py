# Ejercicio 2: Contar apariciones
# Dada la lista:
# colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
# 1- Mostrá cuántas veces aparece “rojo” usando .count().
# 2- Reemplazá el primer “verde” por “amarillo”
# 3- Mostrá la lista final
# El objetivo es usar el método .count(), acceso por índice, asignación de valor. 

lista = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

lista_recuento= lista.count("rojo")
print(f"el color rojo aparece {lista_recuento} veces")

indice = lista.index("verde")
lista[indice] = "amarillo"
print(lista)
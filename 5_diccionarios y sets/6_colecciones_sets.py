# se definen entre {}, pueden contener cualquier tipo de dato,sin embargo, lista no y dic tampoco. 
# El unico caso es la tupla
# No son ordenada, pueden modificarse y no pueden contener elementos duplicados.


colores = {"rojo", "azul", "verde", ("algo", "amarillo")}

print(colores)


#agregar elemento

colores.add("morado")
print(f"colores.add: morado {colores}")

colores.add("morado")
print(f"colores.add: morado {colores}")

#elimirar elemento

colores.remove("verde")
print(f"colores.remove {colores}")
#elimirar elemento solo si lo encuentra
colores.discard("verde")
print(f"colores.discard {colores}")

valor_eliminado = colores.pop()
print(f"colores.pop {colores}")
print(f"elemento eliminado {valor_eliminado}")


#limpiar el set. retorna el set vacio

colores.clear()
print(colores)


#operador de pertenencia

print(f"el valor rojo esta en el set?: {"rojo" in colores}")
print(f"el valor rojo esta en el set?: {"morado" in colores}")


conjunto_1 = {1,2,3}
conjunto_2 = {4,3,5}

union = conjunto_1.union(conjunto_2)# une los elementos
print(union)
interseccion = conjunto_1.intersection(conjunto_2)# marca los repetidos
print(interseccion)
diferencia = conjunto_1.difference(conjunto_2)# muestra los elementos que no estan en el conjunto 2
print(diferencia)


# elimina los duplicados y luego lo pasa a lista de nuevo
lista_ordenado = [1,2,3,4,6,7,7,4,5,9]
list_sin_duplicados = list(set(lista_ordenado))
print(f"lista {lista_ordenado}")
print(f"lista sin duplicados{list_sin_duplicados}")
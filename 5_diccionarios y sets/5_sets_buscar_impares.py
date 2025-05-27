""" 6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el
número de elementos en el conjunto.
 """

conjunto = {1,2,3,4,5,6,7,8,9,10}
cantidad_impares = 0
conjunto_impares = set()

for i in conjunto:
    if i % 2 != 0:
        cantidad_impares += 1
        conjunto_impares.add(i)
        

print(f"la cantidad de impares es de {cantidad_impares}")
print(f"el set de impares es {conjunto_impares}")
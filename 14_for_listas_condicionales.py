# ------------------------------------------------------------------------------
# Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:

# Almacenar los números ingresados en una lista.

# Calcular la cantidad de números pares.

# Contar cuántos números impares se ingresaron.

# Mostrar por pantalla:

# La lista completa de números ingresados.

# La cantidad de los números pares.

# La cantidad de números impares

lista_de_numeros = []
cantidad_pares = 0
cantidad_impares = 0

for i in range(10):
    numero = float(input("ingresar un numero: "))
    lista_de_numeros.append(numero)


for n in lista_de_numeros:
    if n % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1


print(f"la lista de numeros ingresados es: {lista_de_numeros}")
print(f"la cantidad de numeros pares es: {cantidad_pares}")
print(f"la cantidad de numeros impares es: {cantidad_impares}")


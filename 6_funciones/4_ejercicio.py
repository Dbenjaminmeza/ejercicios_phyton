""" Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su factorial. """

def numerofactorial(numero):
    resultado = 1
    for i in range(numero):
        resultado *=  i + 1
    return resultado
    
numero_us = int(input("ingresa un numero para ver su factorial: "))
numerofactorial(numero_us)
print(f"el numero factorial de {numero_us} es {numerofactorial(numero_us)}")
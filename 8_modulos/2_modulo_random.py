import random


def numero_aleatorio():
    return random.randint(1,100)

print("-----------------------bienvenido al generador de numeros aleatorios------------------")
respuesta = input("¿queres comenzar? s/n: ")

while respuesta.upper() == "S":
    numero = numero_aleatorio()
    print(f"el numero aleatorio es : {numero}")
    respuesta = input("¿queres seguir jugando? s/n: ").upper()


print("gracias por jugar! ")
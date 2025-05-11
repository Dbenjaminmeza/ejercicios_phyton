numero_invisible = 48
intentos = 10
import os

numero_usuario_ingreso = input(f"bienvenido a adivina el numero, por favor ingresa un numero del 1 al 100, para eso vas a tener {intentos} intentos: ")

try:
    numero_usuario = int(numero_usuario_ingreso)
except ValueError:
    print("el numero ingreado es invalido")
    numero_usuario = - 1

while intentos > 0 and numero_usuario != numero_invisible :
    if 1 <= numero_usuario <= 100:
        if numero_usuario > numero_invisible:
            print("el numero que ingresaste es mayor al numero secreto")
        else:
            print("el numero que ingresaste es menor al numero secreto")
    else:
        print("el numero ingresado no esta en el rango pedido")
    
    intentos = intentos - 1

    print(f"te quedan {intentos} intentos")

    if intentos > 0:
        numero_usuario_ingreso = input("por favor ingresa otro numero ")
        try:
         numero_usuario = int(numero_usuario_ingreso)
        except ValueError:
          print("el numero ingreado es invalido")
          numero_usuario = - 1
        os.system('cls') 

if numero_usuario == numero_invisible:
    print("felicidades adivinaste el numero!!")
else:
    print("lo siento, no lograste adivinarlo")
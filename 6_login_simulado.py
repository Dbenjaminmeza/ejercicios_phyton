
intentos = 3
import time
import os

print("bienvenido por favor ingresa tus datos de usuario para autentificarte")

while intentos > 0:
    username = input("ingresa tu nombre de usuario: ")
    password = input("ingresa tu contraseña: ")

    if username == "benjameza" and password == "1234":
     print("logueo exitoso bienvenido: ",username)
     intentos = 0
    else:
        intentos = intentos - 1
        print("clave o contraseña incorrectos, por favor volve a ingresarlos te quedan:", intentos," intentos")
        if intentos == 0:
           for i in range(10):
            os.system('cls') 
            print(f"para volver a ingresar tus datos espera {i + 1} segundos")
            time.sleep(1)
           intentos = 3
        
intentos = 3
bandera = False

print("bienvenido por favor ingresa tus datos de usuario para autentificarte")

for i in range(3):
    if bandera == False:
        username = input("ingresa tu nombre de usuario: ")
        password = input("ingresa tu contraseña: ")

        if username == "benjameza" and password == "1234":
         print("logueo exitoso bienvenido: ",username)
         bandera = True
        else:
            intentos = intentos - 1
            print("clave o contraseña incorrectos, por favor volve a ingresarlos te quedan:", intentos," intentos")
        
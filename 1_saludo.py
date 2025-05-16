bandera = False

Nombre = input("ingresa tu nombre ")

while bandera == False:
    try:
        Edad = int(input("ingresa tu edad "))
        print(f"hola {Nombre}, tu edad es {Edad}")
        bandera = True
    except ValueError:
         print("ingresaste un valor incorrecto")
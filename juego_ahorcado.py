# EL JUEGO SE ENCUENTRA EN FASE ALPHA
palabras = ["metacrilato","otorrinolaringologia","paralelepipedo"]
intentos = 0
bandera = False
numero_correcto = False

print("Hola, bienvenido al ahorcado, en este juego vas a tener 10 intentos para adivinar la palabra oculta tene en cuenta que por cada intento fallido se resta uno. Mucha suerte!")

numero_usuario = input("primero: te pido que ingreses un numero del 1 al 3 para poder empezar ")

while numero_correcto == False:
    try:
        numero = int(numero_usuario)
        if numero == 1:
            palabra_elegida = palabras[0]
            numero_correcto = True
        elif numero == 2:
            palabra_elegida = palabras[1]
            numero_correcto = True
        elif numero == 3:
            palabra_elegida = palabras[2]
            numero_correcto = True
        else:
            numero_usuario = input("el numero no es valido, ingrese un numero del 1 al 3 ")
    except ValueError: 
       numero_usuario = input("el dato no es valido, ingrese un numero del 1 al 3: ")


print("tu palabra elegida es la siguiente")

palabra_oculta = len(palabra_elegida) * "_"
print(palabra_oculta)
# EL CODIGO REPRODUCE CORRECTAMENTE HASTA LA LINEA 32 EL RESTO IRE MEJORANDO
while intentos < 10 and bandera == False:
    letra = input ("ingresa una letra: ")
    letra_minuscula = letra.lower()
    """
        if  letra_minuscula in palabra_elegida:
            indice = palabra_elegida.find(letra_minuscula)
            palabra_oculta =  palabra_oculta[:indice] + letra_minuscula + palabra_oculta[indice+1:]
            print(palabra_oculta)

    """
    for i in palabra_elegida:
        if letra_minuscula == i:
            indice = palabra_elegida.find(letra_minuscula)
            palabra_oculta = palabra_oculta[:indice] + letra_minuscula + palabra_oculta[indice+1:]
        else:
            palabra_oculta
    print(palabra_oculta)
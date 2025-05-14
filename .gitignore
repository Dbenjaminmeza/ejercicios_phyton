palabras = ["metacrilato","otorrinolaringologia","paralelepipedo"]
intentos = 0
bandera = False

print("Hola, bienvenido al ahorcado, en este juego vas a tener 10 intentos para adivinar la palabra oculta tene en cuenta que por cada intento fallido se resta uno. Mucha suerte!")

numero_usuario = input("primero: te pido que ingreses un numero del 1 al 3 para poder empezar ")

try:
    numero = int(numero_usuario)
except ValueError: 
    input("el numero no es valido, ingrese otro numero")
    numero = 1
    


if numero == 1:
    palabra_elegida = palabras[0]
elif numero == 2:
    palabra_elegida = palabras[1]
else:
    palabra_elegida = palabras[2]
    

print("tu palabra elegida es la siguiente")

palabra_oculta = len(palabra_elegida) * "_ "
print(palabra_oculta)



while intentos < 10 and bandera == False:
    letras_del_usuario = input ("ingresa una letra: ")
    letra_a_minuscula = letras_del_usuario.lower()

    if  letra_a_minuscula in palabra_elegida:
        indice = palabra_elegida.find(letra_a_minuscula)
        palabra_oculta =  palabra_oculta[:indice] + letra_a_minuscula + palabra_oculta[indice+1:]
        print(palabra_oculta)







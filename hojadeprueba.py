palabra_elegida = "benja"
intentos = 0

palabra_oculta= len(palabra_elegida) * "_"
print(palabra_oculta)

while intentos < 10:
    letra = input ("Ingresar letra ")
    letra_minuscula = letra.lower()

    if letra_minuscula in palabra_elegida:
        indice = palabra_elegida.find(letra_minuscula)
        palabra_oculta = palabra_oculta[:indice] + letra_minuscula +palabra_oculta[indice+1:]
        print(palabra_oculta)
    else:
        intentos = intentos + 1
        print(f"te quedan {10 - intentos}")
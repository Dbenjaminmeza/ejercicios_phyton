texto = "hola Mundo"

print(texto.upper()) # imprimer en mayusculas
print(texto.lower())# imprimer en minusculas
print(texto.find("Mun")) # imprime el numero en donde se encuentra comienza desde el 0

nuevotexto = texto.replace("Mun","benja") #remplaza las letras del texto
print(nuevotexto)

print("Mundo" in texto) #boolean verdadero o falso

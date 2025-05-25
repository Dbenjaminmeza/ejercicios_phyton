temperatura = float(input("ingresar la temperatura a convertir: ")) 

medida = input("la temperatura actual se mide en C o F?: ").lower()


if medida == "c":
   print((temperatura * 9/5) + 32)
elif medida == "f":
   print((temperatura - 32) * 5/9)
else:
   print("el dato ingresado no es correcto: ")





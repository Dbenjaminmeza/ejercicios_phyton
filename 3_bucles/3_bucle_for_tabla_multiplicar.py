print("---Tabla de multiplicar---")

numero = int(input("ingresar un numero: "))

for i in range(1,11):
    calculo = numero * i
    print(f"{numero} x {i} = {calculo}")


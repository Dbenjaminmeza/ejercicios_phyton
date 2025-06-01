## frenar un bucle infinito
while True:
    resultado = input("ingrese s o n")
    if not resultado == "s" and not resultado == "n":
        print("respuesta invalida")
        continue
    if resultado == "n":
        print("exelente")
        break

    print("luego del break")
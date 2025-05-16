bandera = False
import os

while bandera == False:

    try:
        num_1 = float(input("ingrese un numero\n"))
        operacion = input("ingresa la operacion a realizar (+) (-) (*) (/) \n")
        num_2 = float(input("ingrese otro numero\n"))

        while operacion != "+" and operacion != "-" and operacion != "*" and operacion != "/":
            operacion = input("operador invalido, por favor ingresa alguno de los siguientes (+)(-)(*)(/) \n")
    
        if operacion == "+":
            resultado = num_1 + num_2
            print(f"{num_1} + {num_2} = {resultado}")
        elif operacion == "-":
            resultado = num_1 - num_2
            print(f"{num_1} - {num_2} = {resultado}")
        elif operacion == "*":
            resultado = num_1 * num_2
            print(f"{num_1} x {num_2} = {resultado}")
        elif operacion == "/" and num_2 != 0:
            resultado = num_1 / num_2
            print(f"{num_1} / {num_2} = {resultado}")
        elif operacion == "/" and num_2 == 0:
            print("operacion invalida")
        
        respuesta = input("desea realizar otra operacion? (si/no)\n")
        respuesta_minuscula = respuesta.lower()
        
        while respuesta_minuscula != "si" and respuesta_minuscula != "no":
            respuesta = input("desea realizar otra operacion? (si/no)\n")
            respuesta_minuscula = respuesta.lower()

        os.system("cls")
        
        if respuesta_minuscula == "no":
            bandera = True
            print("hasta la proxima")

    except ValueError:
        print("el dato ingresado no es valido \n")
        

   


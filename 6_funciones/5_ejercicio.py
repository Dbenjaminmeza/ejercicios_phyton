""" Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21% """

print("-----------CALCULADORA DE DE FACTURA + IVA O PORCENTAJE A APLICAR----------------------")
def respuesta_us(respuesta):
    if respuesta == 1:
        calculo_iva(sin_iva)
    elif respuesta == 2:
        porcentaje = float(input("ingresa el porcentaje a aplicar: "))
        calculo_iva(sin_iva, porcentaje)
    else:
        print("respuesta no valida")

def calculo_iva(sin_iva, porcentaje = 21):
    porcentaje_calculo = porcentaje / 100
    iva = sin_iva * porcentaje_calculo
    total_factura = sin_iva + iva
    print(f"el total de tu factura es: {total_factura} ")
    return total_factura


sin_iva = float(input("ingresa el total de la factura: "))
respuesta = int(input("el procentaje a agregar es 21 u otro: (ingrese 1 para: 21 / ingrese 2 para: otro): "))

respuesta_us(respuesta)
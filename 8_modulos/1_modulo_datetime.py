import datetime


fecha_actual = datetime.date.today() # obtener la fecha actual
print(fecha_actual)

fecha_y_hora_actual = datetime.datetime.now() #obtener la fecha y la hora actual
print(fecha_y_hora_actual)

def verificar_mayoria_de_edad():
    try:
        anio_nac = int(input("ingrese año de nacimiento: "))
        anio_actual = datetime.datetime.now().year
        print(anio_actual)
        edad = anio_actual - anio_nac
        if edad >= 18:
            print("sos mayor de edad")
        else:
            print("sos menor de edad")
    except ValueError:
        print("valor ingresado incorrecto")

verificar_mayoria_de_edad()
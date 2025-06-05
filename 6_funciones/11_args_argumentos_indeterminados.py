# nos permiten pasar a una funcion un numero de argumentos variables



def suma(*args):
    """ for n in numeros: con for
        resultado += n """
    print(type(args))
    resultado = sum(args) #con sum
    return f"el resultado es {resultado}"

resultado = suma(3 , 4 ,6 , 8, 40,21)
print(resultado)


# *kwargs permiten pasar un numero variableo indeterminado de argumentos con nombre: clave, valor

def ver_persona(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for clave, valor in kwargs.items():
        print(f"clave: {clave} valor: {valor}")


ver_persona(nombre = "juan", edad = 25, ciudad = "resistencia")

#indeterminados porcicionales, determinado posicionales, determinado nombrado, nombrados indeterminados
def mostrar_info(*args, nombre, edad = 0, **kwargs):
    print(args)
    print(nombre)
    print(edad)
    print(kwargs)

#otro ejemplo
mostrar_info(24,"info", nombre = "benja", edad = 23, ciudad = "resistencia" )


def mostrar_info(nombre, edad, *args, **kwargs):
    print(nombre)
    print(edad)
    print(args)
    print(kwargs)


mostrar_info("benja", 24,"info", 23, ciudad = "resistencia" )
#-----------------------------------------FUNCION------------------------------------------------------#
# ejemplo 1 de funcion imprime en pantalla

def my_function():
    print("esto es una funcion")
my_function()

# ejemplo 2 suma 2 numeros 
def sum_two_value(a,b):
    suma = a + b
    print (suma)

sum_two_value(30,25)

# ejemplo 3 con return. en este caso no imprime solo retorna el valor con lo cual debemos guardarlo en una variable

def sum_two_value(a,b):
    return a + b

resultado = sum_two_value(30,20)
print(f"El resultado es: {resultado}")

# ejemplo 4 con return

def suma(a , b):
    resultado = a + b
    return resultado

print(suma(30,60))

# ejemplo 5 

def name(name, surname):
    print(f"{name} {surname}")

name("Benja", "Meza")
name(name = "Meza", surname = "Benja") # puedo cambiarle el orden


# ejemplo 6: valor por defecto

def parametros_por_defecto(nombre , apellido, alias = "sin alias"):
    print(f"{nombre} {apellido} {alias}")

parametros_por_defecto("benja", "meza", "dani")
parametros_por_defecto("benja", "meza")

# ejemplo 7: con el * puedo pasarles los parametros que quiera

def print_text(*text):
    print(text)

print_text("Hola")
print_text("Hola", "python", "benja")
print_text("Hola", "python")


# ejemplo 7: con for puedo pasar todo a mayusculas

def print_text(*text):
    for i in text:
        print(i.upper())
    
print_text("Hola", "python", "benja")# esto no es una lista. Estos son parametros separados
print_text("daniel", "benjamin")
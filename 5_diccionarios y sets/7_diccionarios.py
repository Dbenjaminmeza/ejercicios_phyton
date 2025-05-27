# se definen con llave {} y ademas estan compuestos por key : value (clave, valor)
# las claves son unicas y los valores pueden ser repetidos
# pueden contener cualquier tipo de dato, incluso otros diccionarios
# sus elementos no tienen indice(son desordenados)
# son mutables, podemos agregar, modificar, eliminar


""" ejemplo de diccionario
coordenadas = {
    "x" : 20,
    "y" : 10
}
 """


estudiante = {
    "nombre" : "ana",
    "edad" : 23,
    "curso" : "matematicas" 
}


print(f"el conjutos diccionario es: {estudiante} y el tipo es: {type(estudiante)}")
print(f"La edad del estudiante es: {estudiante["edad"]}")

# agregar un key y su valor
estudiante["carrera"] = "ing"
print(estudiante)

# eliminar una key y su valor
del estudiante["carrera"]
print(estudiante)


# print claves del diccionario
print(f"las claves del diccionario son {estudiante.values()}")
# print valores del diccionario
print(f"los valores del diccionario son {estudiante.values()}")

# print valores del diccionario en una lista
print(f"los valores del diccionario son {list(estudiante.values())}")


estudiante_2 = {
    "nombre" : "juan",
    "edad" : 25,
    "curso" :{
    "nombre" : "programacion web",
    "tags" : ["pw","phyton","web", "django"] 
    } 
}


print(estudiante_2["curso"]["nombre"])
print(estudiante_2["curso"]["tags"])
print(estudiante_2["curso"]["tags"][3])
print(estudiante_2["curso"]["tags"][3])

estudiante_2["curso"]["tags"] = "java"
print(estudiante_2)
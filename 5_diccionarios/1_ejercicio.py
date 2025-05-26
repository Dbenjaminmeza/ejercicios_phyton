""" Ejercicio 3: Diccionario de estudiante
Dado este diccionario:

    estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "materias": ["Matemática", "Historia"]
    }

1- Mostrá el nombre y la edad
2- Agregá una materia nueva a la lista materias
3- Mostrá cuántas materias cursa con len() """

estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "materias": ["Matemática", "Historia"]
}

print("nombre: ", estudiante["nombre"])
print("Edad: ", estudiante["edad"])

estudiante["materias"].append("geografia")

print(estudiante)

total_materias = len(estudiante["materias"])
print(f"{estudiante["nombre"]} tiene {total_materias} materias")
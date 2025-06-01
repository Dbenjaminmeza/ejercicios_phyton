""" ejercicio estudiantes:
1_verificar si aprobo la materia sacando el promedio de los 3 meses por materia

"""

estudiantes = [
    {
    "nombre": "Juan",## estudiante 1
    "notas": {
        "mate": {
            "trimestre_uno": 8,
            "trimestre_dos": 4,
            "trimestre_tres": 5,
            },
        "castellano": {
            "trimestre_uno": 10,
            "trimestre_dos": 5,
            "trimestre_tres": 8,
            },
        "ingles": {
            "trimestre_uno": 10,
            "trimestre_dos": 9,
            "trimestre_tres": 7,
        }
    }
    },
    {
    "nombre": "Benja",## estudiante 2
    "notas": {
        "mate": {
            "trimestre_uno": 4,
            "trimestre_dos": 2,
            "trimestre_tres": 10,
            },
        "castellano": {
            "trimestre_uno": 6,
            "trimestre_dos": 5,
            "trimestre_tres": 7,
            },
        "ingles": {
            "trimestre_uno": 1,
            "trimestre_dos": 5,
            "trimestre_tres": 1,
        }
    }
    }
]

def estudiante_elegido(nombre):
    nombre = nombre.capitalize()
    for estudiante in estudiantes:
        if nombre == estudiante["nombre"]:
            notas = estudiante["notas"]
            return notas
    return None
    
        
def materia_elegida(materia):
    estudiante = estudiante_elegido(nombre)
    if estudiante is None:
        print("no se encontro el alumno")
        return
    materia =  materia.lower()
    if materia in estudiante:
        notas = estudiante
        if materia == "mate":
            nota = notas["mate"]
        elif materia == "castellano":
            nota = notas["castellano"]
        elif materia == "ingles":
            nota = notas["ingles"]
        print(f"las notas del trimestre son {nota}")
        nota = sum(nota.values())/len(nota.values())
        print(f"el promedio del alumno es {nota}")
        if nota >= 6:
            print(f"el alumno {nombre} aprobo la materia")
        else:
            print(f"el alumno {nombre} no aprobo la materia")
    else:
        print("materia no encontrada")

 
nombre = input("ingrese el nombre del alumno a consultar: ")
materia = input("ingrese la materia a consultar: ")
materia_elegida(materia)
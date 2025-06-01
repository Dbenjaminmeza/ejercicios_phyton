""" ejercicio estudiantes:
1_verificar si aprobo la materia sacando el promedio de los 3 meses por materia

"""

estudiantes = [
    {
    "nombre": "Juan",## estudiante 1
    "notas": {
        "mate": {
            "trimestre_uno": 10,
            "trimestre_dos": 5,
            "trimestre_tres": 8,
            },
        "castellano": {
            "trimestre_uno": 10,
            "trimestre_dos": 5,
            "trimestre_tres": 8,
            },
        "ingles": {
            "trimestre_uno": 10,
            "trimestre_dos": 5,
            "trimestre_tres": 8,
        }
    }
    },
    {
    "nombre": "benja",## estudiante 2
    "notas": {
        "mate": {
            "trimestre_uno": 10,
            "trimestre_dos": 5,
            "trimestre_tres": 8,
            },
        "castellano": {
            "trimestre_uno": 3,
            "trimestre_dos": 5,
            "trimestre_tres": 3,
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

    for estudiante in estudiantes:
       if nombre == estudiante["nombre"]:
        notas = estudiante["notas"]
        return notas
        
def materia_elegida(materia):

    if materia in estudiante_elegido(nombre):
        notas = estudiante_elegido(nombre)
        if materia == "mate":
           nota = notas["mate"]
        elif materia == "castellano":
            nota = notas["castellano"]
        elif materia == "ingles":
            nota = notas["ingles"]
        print(f"las del trimestre son {nota}")
        nota = sum(nota.values())/len(nota.values())
        print(f"el promedio del alumno es {nota}")
    else:
        print("materia no encontrada")    

        


nombre = input("ingrese el nombre del alumno a consultar: ")
materia = input("ingrese la materia a consultar: ")
materia_elegida(materia)
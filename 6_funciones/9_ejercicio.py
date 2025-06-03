""" 2 – Sistema de calificaciones de estudiantes {
Creá un programa que guarde las notas de varios estudiantes en un diccionario.
Luego, crea funciones para:
A- Agregar estudiante con sus notas.
B- Calcular el promedio de un estudiante
C- Mostrar los estudiantes aprobados (promedio >= 6) """


estudiantes = {
    'Ana': [9, 8, 10],
    'Luis': [4, 6, 5],
    'Carlos': [10, 10, 9]
}

def agregar_estudiante(base , nombre, notas):
    """ este es un texto dentro de la funcion:
    con esta funcion podemos agregar un estudiantes al diccionario """
    base[nombre] = notas
    

agregar_estudiante(estudiantes, "elias", [1,4,8])
print(estudiantes)
print(agregar_estudiante.__doc__)

def promedio_estudiantes(base, nombre):
    notas = base[nombre]
   #notas = base.get(nombre)
    notas = sum(notas)/len(notas)
    return f" el promedio de {nombre} es {notas}"

print(promedio_estudiantes(estudiantes, "elias"))

# forma con for i
""" def estudiantes_aprobados(base):
    estudiantes_aprobados = []
    for i in base:
        notas = base[i]
        notas = sum(notas)/len(notas)
        if notas >= 6:
            estudiantes_aprobados.append(i)

    return estudiantes_aprobados

print(estudiantes_aprobados(estudiantes)) """

# forma con for desempaquetado

def estudiantes_aprobados(base):
    aprobados = []
    desaprobados = []
    for nombre, notas in base.items():
        promedio = sum(notas)/len(notas)
        if promedio >= 6:
           aprobados.append(nombre)
        else:
            desaprobados.append(nombre)

    return f"los estudiantes aprobados son {aprobados}", f"los estudiantes desaprobados son {desaprobados}"

print(estudiantes_aprobados(estudiantes))

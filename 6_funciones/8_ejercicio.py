""" Ejercicio con Funciones 🧩
1- Generador de hechizos aleatorios {
Escribe una función que combine aleatoriamente un prefijo y sufijo de listas dadas y cree un
hechizo mágico (Usar módulo random) """


import random

def generado_hechizo():
    prefijos = ["Abra","Alakaza","Zendo","Foco","Magi"]
    sufijos = ["cadabra","lumos","mora","nox","flama"]
    palabra_1 = random.choice(prefijos)
    palabra_2 = random.choice(sufijos)
    hechizo = f"tu hechizo es {palabra_1} - {palabra_2}"
    return hechizo

print(generado_hechizo())
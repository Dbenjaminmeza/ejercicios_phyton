print("--------------TUPLAS-----------------")


frutas = ("manzana", "sandia", "cereza","manzana")
verduras = ("cebolla", "lechuga", "zapallo")

print(f"frutas : {frutas} tipo: {type(frutas)}")

print(f"elemento del indice 0: {frutas[0]}")
print(f"elemento del indice 0: {frutas[2]}")


print(f"la longitud es {len(frutas)}")

print(f"cuantas veces aparece manzana {frutas.count("manzana")}")

print(f"el indice de sandia es {frutas.index("sandia")}")

uno, dos, tres, cuatro = frutas

print(uno)

tupla_3 = frutas + verduras

print(f"concatenacion de tuplas: {tupla_3}")
# Ejercicio 1: Gestión de una lista de compras
# Crea una lista vacía llamada lista_compras
# Luego:
# 1- Agregá 3 productos usando .append()
# 2- Mostrá cuántos productos hay con len()
# 3- Eliminá el último producto con .pop()
# 4- Mostrá la lista actualizada
# El objetivo es aprender .append(), .pop() y .len()

lista_compras = []

lista_compras.append("manzana")
lista_compras.append("naranaj")
lista_compras.append("banana")

print(lista_compras)

resultado = len(lista_compras)
print(resultado)

pruducto_eliminado = lista_compras.pop()
print("el producto eliminado es: ", pruducto_eliminado)
print("lista actualizada: ", lista_compras)

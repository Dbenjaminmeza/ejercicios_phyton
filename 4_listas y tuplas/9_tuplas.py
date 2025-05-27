#se definen entre (), pueden contener cualquier tipo de dato, incluso otras tuplas o colecciones.
# son ordenadas(sus elementos tienen indice) y no pueden modificarse

numeros_de_tuplas = (2,32,79,53)

print(f"numeros de la tupla son: {numeros_de_tuplas} y el tipo es {type(numeros_de_tuplas)}")

print(f"el primer numero es {numeros_de_tuplas[0]}")

print(f"los del medio son {numeros_de_tuplas[1:3]}") #slicing toma el indice 1 al 3

print(f"la longitud es {len(numeros_de_tuplas)}")

# desempaquetado de tuplas

a, b, c, d = numeros_de_tuplas

print(f"indice a imprimir a = {a} b = {b} c = {c} d = {d}")

primer_elemento , *resto_elemento = numeros_de_tuplas

print(f"el primer elemento es {primer_elemento} y el resto es {resto_elemento}")

x, segundo_elemento , *resto_elemento = numeros_de_tuplas # se define el primero ya que es ordenado pero no se utiliza

print(f"el primer elemento es {segundo_elemento} y el resto es {resto_elemento}")

#matriz 

matriz = (
    [1,2,3],
    [4,5,6],
    [7,8,9]
)
print(matriz[1][2])


persona = ("juan", 32 , False)

#operador ternario
print(f"esta juan en la tupla? {"Si" if "juan" in persona else "no esta"}") 
print(f"esta 33 en la tupla? {"Si" if 33 in persona else "no esta"}") 

#pasar de lista a tupla y de tupla a lista

lista_de_numeros = list(numeros_de_tuplas)
print(lista_de_numeros)

lista_de_numeros = tuple(lista_de_numeros)
print(lista_de_numeros)
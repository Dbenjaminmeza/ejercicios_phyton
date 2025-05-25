lenguajes = ["phyton","Ruby","java","javascrip","C++"]

print(lenguajes[1])#las listan en phyton parten desde el indice 0

lenguajes[1] = "go" # al valor ruby lo cambia por go

print(lenguajes) #imprime la lista completa
print(lenguajes [-3]) # imprime el valor de javascrip en este caso por ubicacion
print(lenguajes [1:3])# imprime el rango del 1 al 3
print(lenguajes [1:]) # si no le pasamos uno de los valores asume que selecciona desde el ultimo/primero
print(lenguajes [:3]) # si no le pasamos uno de los valores asume que selecciona desde el ultimo/primero
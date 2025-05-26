lenguajes = ["phyton","Ruby","java","javascrip","C++"]
lenguajes.insert(3, "go") #inserta un valor nuevo a la lista ya creada en la posicion que queremos
print(lenguajes)

lenguajes.remove("Ruby") # elimina el valor del listado
print(lenguajes)

print("C++" in lenguajes)# consulta si es verdad o no que ese elento esta en el listado

print(len(lenguajes)) # informa cuantos elementos hay en la lista

lenguajes.clear() #limpia la lista completa
print(lenguajes)
#--------------------------------------------clases----------------------------------------------------

# ejercicio 1: los nombres de las clases se escriben con camelcasse. Mayuscula primera letras
class EmtyPerson:
    pass #evita el error cuando esta vacio

print(EmtyPerson)
print(EmtyPerson())

# ejercicio 2:

class Person:
    def __init__(self,name, surname):
        self.name = name
        self.surname = surname

my_person = Person("benja", "meza")
print(my_person.name)
class coche:

    ruedas = 4
    # constructor
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

#crear un objeto de la clase coche
mi_coche = coche("Toyota","Torola","Rojo")
otro_coche = coche("Ford","Ranger","Azul")

#acceder al estado de los atributos directamente

print("----------------------atributos del primer coche------------")
print(mi_coche.marca)# Toyota
print(mi_coche.modelo)# Corola
print(mi_coche.color)# Rojo
print(mi_coche.ruedas)# 4

print("----------------------atributos del segundo coche------------")
print(otro_coche.marca)# Ford
print(otro_coche.modelo)# Ranger
print(otro_coche.color)# Azul
print(otro_coche.ruedas)# 4
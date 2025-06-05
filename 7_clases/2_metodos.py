class coche:

    #contructor
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    #metodo
    def acelerar(self):
        print(f"el {self.marca} {self.modelo} esta acelerando!")

    def frenar(self):
        print(f"el {self.marca} {self.modelo} esta frenando!")


mi_coche = coche("vento","lambo","negro")
otro_coche = coche("toyota","hrager","rojo")


mi_coche.acelerar()
mi_coche.frenar()

otro_coche.acelerar()
otro_coche.frenar()
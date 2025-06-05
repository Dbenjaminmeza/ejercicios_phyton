class coche:
    ruedas = 4
    #contructor
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1


# crear un objeto de la clase coche

mi_coche = coche("vento","lambo","negro")
otro_coche = coche("toyota","hrager","rojo")


print(f"las ruedas son {mi_coche.ruedas}")

coche.incrementar_ruedas()

print(f"las ruedas son {mi_coche.ruedas}")
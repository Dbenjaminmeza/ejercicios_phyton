class coche:
    ruedas = 4

    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        """calcular una distancia recorrida dada la velocidad y tiempo"""
        return f"la distancia recorrida es {velocidad * tiempo} km"
    
print(coche.calcular_distancia.__doc__)# muestra el texto descriptivo
print(coche.calcular_distancia(8,2))

class Vehiculos:# los def de una clases son metodos
    #constructor
    def __init__(self,param_marca,param_modelo,param_estado,param_color):
        self.marca = param_marca
        self.modelo = param_modelo
        self.estado = param_estado
        self.color = param_color

    def mostrar_info(self):
        print(f"tengo una vehiculo {self.modelo} marca {self.marca} color {self.color} en estado {self.estado}")

# clase hija
class Auto(Vehiculos):
    def __init__(self, param_marca, param_modelo, param_estado, param_color,param_numero_puertas,param_tipo_combustible):
        super().__init__(param_marca, param_modelo, param_estado, param_color) # pasa los datos a vehiculos desde auto
        self.numero_puertas = param_numero_puertas
        self.tipo_combustible = param_tipo_combustible
    #polimorfismo
    def mostrar_info(self):
         print(f"tengo una vehiculo {self.modelo} marca {self.marca} color {self.color} en estado {self.estado} de {self.numero_puertas} con combustible {self.tipo_combustible}")

moto = Vehiculos("motomel","tornado crf", "exelente","negro")
auto = Auto("Toyota","Yaris GR","casi nuevo","negro","4 puestas", "nafta")
camion = Vehiculos("mercedes","1114","se defiende","blanco")

# se puede asi o de manera dentro de la clase
# print(f"tengo una moto {moto.modelo} marca {moto.marca} color {moto.color} en estado {moto.estado}")
# print(f"tengo un auto {auto.modelo} marca {auto.marca} color {auto.color} en estado {auto.estado}")
# print(f"tengo un camion {camion.modelo} marca {camion.marca} color {camion.color} en estado {camion.estado}")

#se puede llamar a cada uno o
""" moto.mostrar_info()
auto.mostrar_info()
camion.mostrar_info() """

# llamar con un for a todos
mis_vehiculos = [moto,auto,camion]
for i in mis_vehiculos:
    i.mostrar_info()

# print(auto.numero_puertas)
# print(auto.tipo_combustible)
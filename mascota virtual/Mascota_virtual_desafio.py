import random 
from mascota import imagen


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 0
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_disgustado = imagen.disgustado
        self.imagen_feliz = imagen.feliz

    def alimentar(self):
        self.felicidad -= random.randint(5,10)
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre == 0:
            print(self.imagen_disgustado)
            print(f"{self.nombre} esta lleno ya no puede comer mas")
        else:
            self.hambre -= random.randint(10,15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(f"{self.nombre} a sido alimentado!😁")
            

    def jugar(self):

        self.hambre += random.randint(10,15)
        if self.hambre > 100:
            self.hambre = 100
        if self.hambre > 70:
            print(self.imagen_disgustado)
            print(f"{self.nombre} tiene mucha hambre y no puede jugar mas, dale su comidita!🍖")
            return 
        
        self.felicidad += random.randint(10,15)
        if self.felicidad > 100:
            self.felicidad = 100  
        else:
            print(self.imagen_feliz)
            print(f"{self.nombre} se esta divirtiendo") 
        

    def estado_animo(self):
        if self.hambre >= 70 and self.felicidad <= 50:
            print(self.imagen_disgustado)
            print("muy hambrienta y muy triste")
        elif self.hambre >= 70:
            print(self.imagen_disgustado)
            print("muy hambrienta")
        elif self.felicidad <= 50:
            print(self.imagen_triste)
            print("muy triste y necesita jugar")
        else:
            print(self.imagen_feliz)
            print("contenta y satisfecha")

    def presentacion(self):  # opcional
        print(f"\n╔════════════════════════════════════╗\n║ Te presento a tu mascota! ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}")

    def despedida(self):  # opcional
        print(f"\n╔════════════════════════════════════╗\n║ Nos vemos! ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║ Jueguemos otro día! ║\n╚════════════════════════════════════╝\n")

interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n"

print(interfaz_inicio)
nombre_mascota = input("elige un nombre para tu mascota: ")

# Crear una instancia de MascotaVirtual
mascota = MascotaVirtual(nombre_mascota)
mascota.presentacion()



# Interactuar con la mascota virtual

while True:
    print(interfaz_juego)
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        mascota.alimentar()
    elif opcion == 2:
        mascota.jugar()
    elif opcion == 3:
        mascota.estado_animo()
    elif opcion == 4:
        mascota.despedida()
        break


# alimenta, juega y muestra su estado de animo
# repite esta accion al menos 8 veces

# Esto lo vamos a utilizar más adelante 😉

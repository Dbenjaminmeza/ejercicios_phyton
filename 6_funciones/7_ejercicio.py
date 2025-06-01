#promedio

def promedios(notas):
   return sum(notas)/len(notas)

promedio_benja = [10,8,4,5]
promedio_juan = [4,9,4,6]
print(f"el promedio de benja es: {promedios(promedio_benja)}")
print(f"el promedio de juan es: {promedios(promedio_juan)}")
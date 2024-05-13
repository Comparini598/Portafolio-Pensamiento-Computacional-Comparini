import math

n=int(input("Ingrese l cantidad de números"))
list= []

for i in range(n):
    valor=int(input("ingrese un número"))
    list.append(valor)
sumatoria=0
for i in (list):
    sumatoria=sumatoria+1
promedio=sumatoria/n

print("El promedio es "+str(promedio))

for i in list:
    numerador=(promedio-i)**2
    desviación=math.sqrt(numerador/n)
print("La desviación estándar es" +str(desviación))
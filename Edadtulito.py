import math

num=int(input("Ingrese la cantidad de números"))
list=[]
cantidad=0

n=int(input("Ingrese la edad mínima"))

while  cantidad <num:
 num2= int(input("Ingrese una edad"))
 if num2>0:
  list.append(num2)
  cantidad = cantidad+1
 else:
  print("Número inválido")

  edades=0
  for x in(list):
   if x >n:
     edades +=1
     print("Las edades válidas son: ", edades)
 

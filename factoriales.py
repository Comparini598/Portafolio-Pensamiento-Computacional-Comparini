valor=int(input("Ingrese un número"))

if valor<=0:
    print("El número es inválido, ingrese otro")

factorial=1
for x in range(1, valor+1):
    factorial*=x
if x==valor:

  print("El resultado es" +str(factorial))


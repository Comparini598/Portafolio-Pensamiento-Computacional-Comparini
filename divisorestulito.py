valor=int(input("Ingresa un número"))
valor2=int(input("ingresa otro número"))

if valor<=0 and valor2<=0:
    print("En número es inválido")

else: 
    suma=0
    for x in range (1,valor):
        if valor %x==0:
            suma+=x
    if suma==valor:
        suma2=0
    for x in range (1,valor2):
        if valor %x==0:
            suma2+=x
if suma2==valor and suma==valor2:

        print("Los números son amigos")
else:
        print("Los números no son amigos")
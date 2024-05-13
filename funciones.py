aceptado=True
while aceptado==True:
 print("Menpu de opciones \n1. Sumar \n2 Restar \n3 Multiplicar \n4 Dividir \n5 Pot")
opcion= int(input("Ingrese la opción deseada\n"))

if opción==1:
   













def Sumar(num1, num2):
    Total=num1+num2
    return Total


def Restar(num1,num2):
    Total=num1-num2
    return Total

def Multiplicar(num1,num2):
    Total=num1*num2
    return Total

def Dividir(num1, num2):
    Total=num1/num2
    return Total

def Factorial(num3):
    facto =1
    for x in range(1, num3+1):
     facto*=x
    if x==num3:
       return facto

numero1=int(input("ingrese un número:"))
numero2=int(input("Ingrese un número"))

print("La suma es "+str(Sumar(numero1,numero2)))
print("La resta es "+str(Restar(numero1,numero2)))
print("La multiplicación es "+str(Multiplicar(numero1,numero2)))
if numero2==0:
    print("No es posible dividir")
else:
 print("La división es " +str(Dividir(numero1,numero2)))




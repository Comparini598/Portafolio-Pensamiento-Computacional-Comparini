print("Ejercicio 1: operaciones artméticas")
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese su segundo número: "))
total=num1+num2
diferencia=num1-num2
producto=num1*num2
divreal=num1/num2
diventera=num1//num2
divmodular=num1&num2
potencia=num1**num2
print(num1, "+",num2, "=",total)
print(num1, "-",num2, "=",diferencia)
print(num1, "*",num2, "=",producto)
print(num1, "/",num2, "=",divreal)
print(num1, "//",num2, "=", diventera)
print(num1, "%",num2, "=",divmodular)
print(num1, "^",num2, "=" ,potencia)
print()
print("Ejercicio 2; operaciones booleanas")
igualdad=num1==num2
mayorque=num1>num2
menorque=num1<num2
distinto=num1!=num2
print(num1,"es igual a",num2,":",igualdad)
print(num1,"es mayor que",num2,":", mayorque)
print(num1,"es menor que",num2,":",menorque)
print(num1,"es distinto a",num2,":",distinto)

print("Ejercicio 3: jerarquía de operaciones")
a=int(input("Ingrese el primer valor: "))
b=int(input("Ingrese el segundo valor: "))
c=int(input("Ingrese el tercer valor: "))
i=a*b+c
ii=a*(b+c)
iii=a/(b+c)
iv=((3*a)+(2*b))/(c**2)
print("a*b+c=",i)
print("a*(b+c)=",ii)
print("a/(b+c)=",iii)
print("(3a+2b)/c^2=",iv)
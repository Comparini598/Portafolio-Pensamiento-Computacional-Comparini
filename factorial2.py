num=int(input("ingrese un número: "))

factorial=0
if num<=0:
    print("Error")
else:
    for n in range(1,num+1):
        if n==1:
            factorial=1
        else:
            factorial*=n
        
    print("El factorial es: " +str(factorial))
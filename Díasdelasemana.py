#Natalia Comparini, Gabriela Castro y Styvalys Mazariegos
print("Días de la semana")
día=int(input("Ingrese el número"))
if día<1 or día>7:
    print("El número que ingresaste es inválido")
else:
    if día==1:
        print("El día es lunes")
    elif día==2:
        print("El día es martes")
    elif día==3:
        print("El día es miércoles")
    elif día==4:
        print("El día es jueves")
    elif día==5:
        print("El día es viernes")
    elif día==6:
        print("El día es sábado")
    elif día==7:
        print("El día es domingo")
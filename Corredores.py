print("La velocidad del equipo")
print("la velocidad promedio")

num1=input("Ingrese el primer tiempo")
num2=input("Ingrese el segundo tiempo")
num3=input("Ingrese el tercer tiempo")
num4= input("Ingrese el cuarto tiempo")

num1= float(num1)
num2= float(num2)
num3= float(num3)
num4= float(num4)

suma= num1+num2+num3+num4
print(suma)

print("Velocidad promedio")
VelocidadPromedio= (400/suma)
print(VelocidadPromedio)
           
print(f"La velocidad promedio es:{VelocidadPromedio: .2f} ")         
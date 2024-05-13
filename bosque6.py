import turtle
import random

# Configuración inicial
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")  # Color de fondo celeste
screen.title("Dibujo de un bosque")

# Función para dibujar un árbol
def draw_tree(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.color("brown")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.end_fill()

    # Dibujar la copa del árbol centrada en la punta del tronco
    t.color("green")
    t.penup()
    t.goto(x + -45, y + 100)  # Ajustar las coordenadas de la copa
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

# Función para dibujar el césped
def draw_grass(t):
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)  # Configura la velocidad al máximo

# Dibujar césped
draw_grass(t)

# Dibujar árboles
num_trees = 3
tree_spacing = 200  # Espacio entre árboles
for i in range(num_trees):
    x = -350 + i * tree_spacing
    draw_tree(t, x, -200)  # Los árboles están en la línea de base del césped

#Dibujar Oso
def draw_oso():
# Dibuja el cuerpo del oso
 turtle.color("#8B4513") #cafe claro
turtle.begin_fill()
turtle.color("#8B4513")
turtle.circle(60)
turtle.end_fill()

# Dibuja la cabeza del oso
turtle.penup()
turtle.goto(0, 120)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(40)
turtle.end_fill()

# Dibuja las orejas del oso
turtle.penup()
turtle.goto(-25, 174)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(20, 175)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(15)
turtle.end_fill()

# Dibuja las patas del oso
turtle.penup()
turtle.goto(50, 90)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(-45, 90)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(15)
turtle.end_fill()


#Dibuja las patas traseras del osito
turtle.penup()
turtle.goto(-25, -18)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(20, -18)
turtle.pendown()
turtle.begin_fill()
t.color("brown")
turtle.circle(15)
turtle.end_fill()


# Dibuja los ojos del oso
turtle.penup()
turtle.goto(-10, 170)
turtle.pendown()
turtle.dot(10, "white")

turtle.penup()
turtle.goto(6, 170)
turtle.pendown()
turtle.dot(10, "white")

#Dibuja lo de adentro del ojo
# Dibuja los ojos del oso
turtle.penup()
turtle.goto(-9, 170)
turtle.pendown()
turtle.dot(8.5, "black")

turtle.penup()
turtle.goto(7, 170)
turtle.pendown()
turtle.dot(9, "black")

# Dibuja el puntito de la nariz del oso
turtle.penup()
turtle.goto(-1, 150)
turtle.pendown()
turtle.dot(7, "black")


# Dibuja la nariz del oso
turtle.penup()
turtle.goto(9, 140)
turtle.pendown()
turtle.setheading(100)
turtle.color("black")
turtle.width(5)
turtle.circle(10, 160)

# Ocultar la tortuga y finalizar
t.hideturtle()
turtle.done()
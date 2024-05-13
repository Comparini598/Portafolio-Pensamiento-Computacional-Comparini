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
    t.setheading(110)
    t.color("brown")
    t.begin_fill()
    t.forward(90)
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

    # Dibujar la copa del árbol
    t.color("green")
    t.penup()
    t.goto(x - 100, y + 80)
    t.pendown()
    t.begin_fill()
    t.circle(60)
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
num_trees = 5
for _ in range(num_trees):
    x = random.randint(-350, 350)
    y = random.randint(-100, 150)
    draw_tree(t, x, y)

# Ocultar la tortuga y finalizar
t.hideturtle()
turtle.done()


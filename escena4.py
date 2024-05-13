import turtle

# Configuración inicial de Turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")  # Color de fondo celeste
screen.title("El oso Regi")
story_teller = turtle.Turtle()
story_teller.speed(0.1)  # Velocidad de dibujo

# Solicitar el nombre del usuario
user_name = turtle.textinput("Nombre", "¿Cuál es tu nombre?")
# Solicitar el color favorito del usuario
user_color = turtle.textinput("Color Favorito", "Escoge tu color favorito: Rojo, morado, azul")
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
num_trees = 2
tree_spacing = 150  # Espacio entre árboles
for i in range(num_trees):
    x = -350 + i * tree_spacing
    draw_tree(t, x, -200)  # Los árboles están en la línea de base del césped

def draw_oso():
# Dibuja el cuerpo del oso
  t.penup()
t.goto(240, -140)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(60)
t.end_fill()

# Dibuja la cabeza del oso
t.penup()
t.goto(260, -54)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(40)
t.end_fill()

# Dibuja las orejas del oso
t.penup()
t.goto(257, -15)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(15)
t.end_fill()

t.penup()
t.goto(315, -15)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(15)
t.end_fill()

# Dibuja las patas del oso
t.penup()
t.goto(232, -100)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(15)
t.end_fill()

t.penup()
t.goto(340, -100)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(15)
t.end_fill()


#Dibuja las patas traseras del osito
t.penup()
t.goto(238, -186)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(15)
t.end_fill()

t.penup()
t.goto(330, -186)  # Esquina inferior derecha
t.penup()
t.color("#8B4513")  # Color café claro
t.begin_fill()
t.color("#8B4513") #cafe claro
t.circle(15)
t.end_fill()


# Dibuja los ojos del oso
turtle.penup()
turtle.goto(290, -48)
turtle.pendown()
turtle.dot(10, "white")

turtle.penup()
turtle.goto(305, -48)
turtle.pendown()
turtle.dot(10, "white")

#Dibuja lo de adentro del ojo
# Dibuja los ojos del oso
turtle.penup()
turtle.goto(291, -48)
turtle.pendown()
turtle.dot(8.5, "black")

turtle.penup()
turtle.goto(306, -48)
turtle.pendown()
turtle.dot(9, "black")

# Dibuja el puntito de la nariz del oso
turtle.penup()
turtle.goto(299, -64)
turtle.pendown()
turtle.dot(7, "black")


# Dibuja la nariz del oso
turtle.penup()
turtle.goto(309, -75)
turtle.pendown()
turtle.setheading(100)
turtle.color("black")
turtle.width(5)
turtle.circle(10, 160)
story_teller.hideturtle()






def draw_rectangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Función para dibujar un triángulo
def draw_triangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(width)
        t.left(120)
    t.end_fill()

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)  # Configura la velocidad al máximo

# Dibujar la casa
# Cuerpo amarillo
draw_rectangle(t, -80, -80, 130, 130, "yellow")

# Techo rosa
draw_triangle(t, -85, -80, 140, 50, "pink")

# Puerta
draw_rectangle(t, -20, -150, 40, 60, "brown")

# Ventana izquierda
draw_rectangle(t, -60, -100, 20, 20, "white")

# Ventana derecha
draw_rectangle(t, 0, -100, 20, 20, "white")

# Chimenea
draw_rectangle(t, -5, -5, 20, 30, "gray")

def draw_ray():
    t.color("yellow")  # Color amarillo
    t.begin_fill()  # Comenzar a rellenar
    for _ in range(8):  # Dibujar un octágono
        t.forward(50)  # Longitud del rayo
        t.right(135)  # Ángulo del rayo
    t.end_fill()  # Finalizar rellenado

# Dibujar el sol
t.penup()  # Levantar el lápiz
t.goto(200, 200)  # Mover el cursor a la esquina superior derecha
t.pendown()  # Bajar el lápiz

for _ in range(12):  # Dibujar 12 rayos del sol
    draw_ray()
    t.right(30)  # Rotar para dibujar el siguiente rayo
# Ocultar la tortuga y finalizar
t.hideturtle()
turtle.done()

# Historias y sus funciones de dibujo asociadas
stories = [
    ("Cuando de repente se encontró con una csa....¿Habría alguien ahí con quien jugar?", draw_tree()),
    
]



# Ocultar la tortuga y finalizar
t.hideturtle()
turtle.done()
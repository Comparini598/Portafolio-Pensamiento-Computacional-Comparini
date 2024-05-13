#1. Agregar N cantidad de piezas en el tablero
#pedir al jugador los datos requeridos

def crear_tablero():
    return [[None for _ in range(8)] for _ in range(8)]

def agregar_pieza(tablero):
    tipos_validos = ['alfil', 'peon', 'caballo', 'torre', 'reina', 'rey']
    colores_validos = ['blanco', 'negro']

    tipo = input("Tipo de pieza (alfil, peón, caballo, torre, reina, rey): ").lower()
    while tipo not in tipos_validos:
        print("Tipo de pieza inválido.")
        tipo = input("Tipo de pieza (alfil, peón, caballo, torre, reina, rey): ").lower()

    color = input("Color (blanco, negro): ").lower()
    while color not in colores_validos:
        print("Color inválido.")
        color = input("Color (blanco, negro): ").lower()

    posicion = input("Posición en el tablero (Ejemplo: a1, e4, f8): ").lower()
    letras_validas = 'abcdefgh'
    numeros_validos = '12345678'
    while len(posicion) != 2 or posicion[0] not in letras_validas or posicion[1] not in numeros_validos:
        print("Posición inválida.")
        posicion = input("Posición en el tablero (Ejemplo: a1, e4, f8): ").lower()

    fila = int(posicion[1]) - 1
    columna = letras_validas.index(posicion[0])

    if tablero[fila][columna] is not None:
        print("Ya hay una pieza en esa posición.")
        return False

    tablero[fila][columna] = (tipo, color)
    return True

#aquí como funciona:)
tablero = crear_tablero()
while True:
    if not agregar_pieza(tablero):
        continue

    respuesta = input("¿Desea agregar otra pieza? (s/n): ").lower()
    if respuesta != 's':
        break

print("Tablero con piezas:")
for fila in tablero:
    print(fila)

#2. Ingresar la pieza del caballo a evaluar
def agregar_caballo(tablero):
    colores_validos = ['blanco', 'negro']

    color = input("Color (blanco, negro): ").lower()
    while color not in colores_validos:
        print("Color inválido.")
        color = input("Color (blanco, negro): ").lower()

    posicion = input("Posición en el tablero (Ejemplo: a1, e4, f8): ").lower()
    letras_validas = 'abcdefgh'
    numeros_validos = '12345678'
    while len(posicion) != 2 or posicion[0] not in letras_validas or posicion[1] not in numeros_validos:
        print("Posición inválida.")
        posicion = input("Posición en el tablero (Ejemplo: a1, e4, f8): ").lower()

    fila = int(posicion[1]) - 1
    columna = letras_validas.index(posicion[0])

    if tablero[fila][columna] is not None:
        print("Ya hay una pieza en esa posición.")
        return False

    tablero[fila][columna] = ('caballo', color)
    return True

#aquí ya funciona:))
tablero = crear_tablero()
print("Ingrese la pieza del caballo a evaluar:")
agregar_caballo(tablero)

print("Tablero con pieza del caballo:")
for fila in tablero:
    print(fila)



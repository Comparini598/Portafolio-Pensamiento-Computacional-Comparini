def agregar_pieza(tablero, tipo, color, posicion):
    letras_validas = 'abcdefgh'
    numeros_validos = '12345678'

    if len(posicion) != 2 or posicion[0] not in letras_validas or posicion[1] not in numeros_validos:
        print("Posición inválida.")
        return False

    fila = int(posicion[1]) - 1
    columna = letras_validas.index(posicion[0])

    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[0]):
        print("Posición fuera del tablero.")
        return False

    if tablero[fila][columna] is not None:
        print("Ya hay una pieza en esa posición.")
        return False

    tablero[fila][columna] = (tipo, color)
    return True
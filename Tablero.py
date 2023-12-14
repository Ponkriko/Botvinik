class TableroAjedrez:
    def __init__(self):
        self.tablero = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def mostrar_tablero(self):
        print("   a b c d e f g h")
        print(" +-----------------")
        for fila_num, fila in zip(range(8, 0, -1), self.tablero):
            print(f"{fila_num}| {' '.join(fila)} | {fila_num}")
        print(" +-----------------")
        print("   a b c d e f g h")
        print()

    def mover_pieza(self, pieza, fila_origen, columna_origen, fila_destino, columna_destino):
        self.tablero[fila_destino][columna_destino] = pieza
        self.tablero[fila_origen][columna_origen] = ' '

    def notacion_a_coordenadas(self, movimiento):
        columna_letra = movimiento[0]
        fila = int(movimiento[1])
        columna = ord(columna_letra) - ord('a')
        return fila - 1, columnaa2

    def elegir_pieza(self, jugador):
        while True:
            try:
                movimiento = input(f'Jugador {jugador}, ingresa tu movimiento en notación de ajedrez (por ejemplo, e4): ')
                fila, columna = self.notacion_a_coordenadas(movimiento)
                if 0 <= fila < 8 and 0 <= columna < 8:
                    pieza = self.tablero[fila][columna]
                    if pieza != ' ':
                        return pieza, fila, columna
                    else:
                        print('No hay una pieza en esa posición. Intenta de nuevo.')
                else:
                    print('Por favor, elige una posición válida (1-8 para las filas, a-h para las columnas).')
            except ValueError:
                print('Entrada inválida. Por favor, ingresa un número para la fila.')

# Uso del tablero
tablero = TableroAjedrez()
tablero.mostrar_tablero()

# Jugador 1
pieza_jugador1, fila_jugador1, columna_jugador1 = tablero.elegir_pieza(1)
print(f'Jugador 1 eligió la pieza {pieza_jugador1} en la posición ({fila_jugador1+1}, {chr(columna_jugador1 + ord("a"))}).')

# Mover la pieza del jugador 1 prueba 1
fila_destino = int(input('Ingresa la fila de destino (1-8): ')) - 1
columna_destino_letra = input('Ingresa la columna de destino (a-h): ')
columna_destino = ord(columna_destino_letra) - ord('a')

tablero.mover_pieza(pieza_jugador1, fila_jugador1, columna_jugador1, fila_destino, columna_destino)
tablero.mostrar_tablero()

# Jugador 2
pieza_jugador2, fila_jugador2, columna_jugador2 = tablero.elegir_pieza(2)
print(f'Jugador 2 eligió la pieza {pieza_jugador2} en la posición ({fila_jugador2+1}, {chr(columna_jugador2 + ord("a"))}).')

# Mover la pieza del jugador 2
fila_destino = int(input('Ingresa la fila de destino (1-8): ')) - 1
columna_destino_letra = input('Ingresa la columna de destino (a-h): ')
columna_destino = ord(columna_destino_letra) - ord('a')

tablero.mover_pieza(pieza_jugador2, fila_jugador2, columna_jugador2, fila_destino, columna_destino)
tablero.mostrar_tablero()

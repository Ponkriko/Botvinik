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
        print(" a b c d e f g h")
        print(" +---------------")
        for fila_num, fila in enumerate(self.tablero[::-1], start=1):
            print(f"{fila_num}| {' '.join(fila)} | {fila_num}")
        print(" +----------------")
        print(" a b c d e f g h")
        print()

    def elegir_pieza(self, jugador):
        while True:
            try:
                fila = int(input(f'Jugador {jugador}, elige la fila (1-8): ')) - 1
                columna = int(input(f'Jugador {jugador}, elige la columna (a-h): '))
                columna = ord(columna_letra) -  ord('a')

#aqui esta el error                if 0 <= fila < 8 and 0 <= columna < 8:
                    pieza = self.tablero[fila][columna]
                    if pieza != ' ':
                        return pieza, fila, columna
                    else:
                        print('No hay una pieza en esa posición. Intenta de nuevo.')
                else:
                    print('Por favor, elige una posición válida (1-8).')
            except ValueError:
                print('Entrada inválida. Por favor, ingresa un número.')

# tablero
tablero = TableroAjedrez()
tablero.mostrar_tablero()

# Jugador 1 
pieza_jugador1, fila_jugador1, columna_jugador1 = tablero.elegir_pieza(1)
print(f'Jugador 1 eligió la pieza {pieza_jugador1} en la posición ({fila_jugador1+1}, {chr(columna_jugador1 + ord("a"))}).')

# Jugador 2
pieza_jugador2, fila_jugador2, columna_jugador2 = tablero.elegir_pieza(2)
print(f'Jugador 2 eligió la pieza {pieza_jugador2} en la posición ({fila_jugador2+1}, {chr(columna_jugador2 + ord("a"))}).')

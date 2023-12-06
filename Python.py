class TableroAjedez:
    def __init__(self):
        self.tablero = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ]
    def mostrar_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))
        print()

    def elegir_pieza(self, jugador):
        while True
            try:
                fila = int(input(f'Jugador{jugador}, elige la fila (1-8): ')) - 1
                columna = int(input(f'Jugador {jugador}, elige la columna (1-8):')) - 1

                if 0 <= fila < 8 and 0 <= columna < 8:
                    pieza = self. tablero[fila ][columna]
                    if pieza != ' ':
                        return pieza, fila, columna 
                    else:
                        print('No hay una pieza en esa posición. Intenta de nuevo.')
                else:
                    print ('Por favor, elige una posición válida (1-8).')
                except ValueError:
                    print('Entrada Invalida. Por favor, ingresa un número.')
tablero = TableroAjedez()
tablero.mostrar_tablero()

#jugador 1 
pieza_jugador1, fila_jugador1, columna_jugador1 = tablero.elegir_pieza(1)
print(f'jugador 1 eligio la pieza {pieza_jugador1} en posición ({fila_jugador1+1}, {colunma_jugador1+1}).')

#Jugador 2
pieza_jugador2, fila_jugador2, columna_jugador2 = tablero.elegir_pieza(2)
print(f'Jugador 2 eligió la pieza {pieza_jugador2} en la posición ({fila_jugador2+1}, {columna_jugador2+1}).')

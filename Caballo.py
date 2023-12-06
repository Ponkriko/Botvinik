class Caballo(Pieza):
    def __init__(self, color):
        super(). __init__(color)

    def mover(self, origen, destino):
        delta_filas = abs(destino[0] - origen[0])
        delta_columna = abs(destino[1] - origen[1])
        return delta_filas == 2 and delta_columnas == 1 or delta_filas == 1 and delta_columnas == 2
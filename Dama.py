from pieza import Pieza

class Dama(Pieza):
    def __init__(selfe, color):
        super(). __init__(color)

    def mover(self, origen, destino):
        delta_filas = abs(destino[0] - origen[0])
        delta_columnas = abs(destino[1] - origen[1])
        return delta_filas == delta_columnas or origen[0] == destino[0] or origen[1] == destino[1]


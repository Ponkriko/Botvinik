from pieza import Pieza

class Torre(Pieza):
    def __init__(self, color):
        super().__init__(color)
        def mover(self, origen, destino):
            return origen[0] == destino[0] or origen[1] == destino[1]
            
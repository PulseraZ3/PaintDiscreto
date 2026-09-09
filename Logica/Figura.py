class Figura:
    def __init__(self):
        self.puntos = []

    def agregar_punto(self, x, y):
        if len(self.puntos) >= 4:
            return False

        self.puntos.append((x,y))
        return True

    def obtener_puntos(self):
        return self.puntos

    def cantidad_puntos(self):
        return len(self.puntos)
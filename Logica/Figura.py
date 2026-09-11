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
    def cargar_puntos(self,puntos):
        self.puntos = []
        for grupo in puntos:
            figura = []

            for punto in grupo:
                x = punto[0]
                y = punto[1]
                figura.append((x,y))
            self.puntos.append(figura)
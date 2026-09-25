class Homotecia:
    def aplicar(self, puntos, factor):
        if len(puntos) > 0 and isinstance(puntos[0][0], (int, float)):
            nuevo_puntos = []
            for punto in puntos:
                x, y = punto
                nuevo_x = x * factor
                nuevo_y = y * factor
                nuevo_puntos.append((nuevo_x, nuevo_y))
            return nuevo_puntos
        else:
            nuevo_puntos = []
            for grupo in puntos:
                nuevo_grupo = []
                for punto in grupo:
                    x, y = punto
                    nuevo_x = x * factor
                    nuevo_y = y * factor
                    nuevo_grupo.append((nuevo_x, nuevo_y))
                nuevo_puntos.append(nuevo_grupo)
            return nuevo_puntos
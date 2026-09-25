import math

class Rotacion:

    def rotar(self,puntos, angulo):
        angulo = math.radians(angulo)
        nuevo_puntos = []

        if len(puntos) >0 and isinstance(puntos[0][0],(int ,float)):
            for punto in puntos:
                x, y = punto
                nuevo_x = x*math.cos(angulo) - y * math.sin(angulo)
                nuevo_y = x*math.sin(angulo) + y * math.cos(angulo)
                nuevo_puntos.append((nuevo_x,nuevo_y))
        else:
            for grupo in puntos:
                nuevo_grupo = []

                for punto in grupo:
                    x, y = punto

                    nuevo_x = x * math.cos(angulo) - y * math.sin(angulo)
                    nuevo_y = x * math.sin(angulo) + y * math.cos(angulo)

                    nuevo_grupo.append((nuevo_x, nuevo_y))

                nuevo_puntos.append(nuevo_grupo)
        return nuevo_puntos
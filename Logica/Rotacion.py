import math

class Rotacion:
    # desde el 0;0
    # nuevo_x = x*math.cos(angulo) - y * math.sin(angulo)
    # nuevo_y = x*math.sin(angulo) + y * math.cos(angulo)
    # nuevo_puntos.append((nuevo_x,nuevo_y))
    def rotar(self,puntos, angulo, h, k):
        angulo = math.radians(angulo)
        nuevo_puntos = []

        if len(puntos) >0 and isinstance(puntos[0][0],(int ,float)):
            for punto in puntos:
                x, y = punto
                x_traslado = x -h
                y_traslado = y -k
                nuevo_x = (
                        x_traslado * math.cos(angulo)
                        - y_traslado * math.sin(angulo)
                )

                nuevo_y = (
                        x_traslado * math.sin(angulo)
                        + y_traslado * math.cos(angulo)
                )
                nuevo_x = nuevo_x + h
                nuevo_y = nuevo_y + k
                nuevo_puntos.append((nuevo_x, nuevo_y))
        else:
            for grupo in puntos:
                nuevo_grupo = []
                for punto in grupo:
                    x, y = punto
                    x_trasladado = x - h
                    y_trasladado = y - k
                    nuevo_x = (
                            x_trasladado * math.cos(angulo)
                            - y_trasladado * math.sin(angulo)
                    )
                    nuevo_y = (

                            x_trasladado * math.sin(angulo)

                            + y_trasladado * math.cos(angulo)

                    )

                    nuevo_x = nuevo_x + h

                    nuevo_y = nuevo_y + k

                    nuevo_grupo.append((nuevo_x, nuevo_y))

                nuevo_puntos.append(nuevo_grupo)

        return nuevo_puntos
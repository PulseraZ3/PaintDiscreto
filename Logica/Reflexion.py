class Reflexion:

    def reflexion_eje_x(self,puntos):
        if len(puntos) > 0 and isinstance(puntos[0][0],(int ,float)):
            nuevo_puntos = []
            for punto in puntos:
                x, y = punto
                nuevo_puntos.append((x,-y))
            return nuevo_puntos
        else:
            nuevo_puntos = []
            for grupo in puntos:
                nuevo_grupo = []
                for punto in grupo:
                    x, y = punto
                    nuevo_grupo.append((x,-y))
                nuevo_puntos.append(nuevo_grupo)
            return nuevo_puntos

    def reflexion_eje_y(self,puntos):
        if len(puntos) > 0 and isinstance(puntos[0][0],(int ,float)):
            nuevo_puntos = []
            for punto in puntos:
                x, y = punto
                nuevo_puntos.append((-x,y))
            return nuevo_puntos
        else:
            nuevo_puntos = []
            for grupo in puntos:
                nuevo_grupo = []
                for punto in grupo:
                    x, y = punto
                    nuevo_grupo.append((-x,y))
                nuevo_puntos.append(nuevo_grupo)
            return nuevo_puntos

    def reflexion_origen(self,puntos):
        if len(puntos) > 0 and isinstance(puntos[0][0],(int ,float)):
            nuevo_puntos = []
            for punto in puntos:
                x, y = punto
                nuevo_puntos.append((-x,-y))
            return nuevo_puntos
        else:
            nuevo_puntos = []
            for grupo in puntos:
                nuevo_grupo = []
                for punto in grupo:
                    x, y = punto
                    nuevo_grupo.append((-x,-y))
                nuevo_puntos.append(nuevo_grupo)
            return nuevo_puntos

    def reflexion_recta(self, puntos, a, b, c):
        print("VALORES RECIBIDOS:", a, b, c)
        if len(puntos) > 0 and isinstance(puntos[0][0],(int ,float)):
            nuevo_puntos = []
            for punto in puntos:
                x, y = punto
                d = (a*x + b*y + c)/(a**2 + b**2) #reflexion del punto respecto a la recta
                nuevo_x = x - 2 * a * d
                nuevo_y = y - 2 * b * d
                print(
                    "Original:", (x, y),
                    "-> Nuevo:", (nuevo_x, nuevo_y)
                )

                nuevo_puntos.append((nuevo_x,nuevo_y))
            return nuevo_puntos
        else:
            nuevos_puntos = []
            for grupo in puntos:
                nuevo_grupo = []
                for punto in grupo:
                    x, y = punto
                    d = (a * x + b * y + c) / (a ** 2 + b ** 2)
                    nuevo_x = x - 2 * a * d
                    nuevo_y = y - 2 * b * d
                    print(
                        "Original:", (x, y),
                        "-> Nuevo:", (nuevo_x, nuevo_y)
                    )

                    nuevo_grupo.append((nuevo_x, nuevo_y))
                nuevos_puntos.append(nuevo_grupo)
            return nuevos_puntos


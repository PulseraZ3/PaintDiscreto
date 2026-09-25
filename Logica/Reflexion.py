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



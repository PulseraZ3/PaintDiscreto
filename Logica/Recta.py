class Recta:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
        self.existe= False

    def establecer_recta(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.existe = True

    def obtener_recta(self):
        return self.a, self.b, self.c

    def eliminar_recta(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.existe = False
import tkinter as tk
import json
import math
from Logica.Figura import Figura
from Logica.Reflexion import Reflexion
from Logica.Rotacion import Rotacion
from Logica.Homotecia import Homotecia
from Logica.Recta import Recta
from tkinter import ttk, colorchooser
from PIL import Image, ImageTk
from pathlib import Path
from miscellaneous.ColorChanger import ColorChanger

class VentanaPrincipal:
    def __init__(self):
       self.fuente_Titulo = ("MS Sans Serif",14, "bold")
       self.fuente_Texto= ("MS Sans Serif",12, "bold")
       self.color_fondo="#c0c0c0"
       self.color_panel="#d4d0c8"
       self.color_blanco="#ffffff"
       self.color_negro="#000000"
       self.escala =25        #se tendria que testear
       self.reflexion = Reflexion()
       self.rotacion = Rotacion()
       self.centro_rotacion = None
       self.homotecia = Homotecia()
       self.recta = Recta()
       self.figura = Figura()
       self.ventana = tk.Tk()
       self.color_changer= ColorChanger(self)
       self.configurar_ventana()
       self.crear_componentes()

    def aplicar_homotecia(self):

        factor = float(self.entry_factor.get())

        puntos = self.figura.obtener_puntos()

        nuevos_puntos = self.homotecia.aplicar(
            puntos,
            factor
        )

        self.figura.cargar_puntos(nuevos_puntos)

        self.dibujar_plano()

    def aplicar_rotacion(
            self,
            entry_x,
            entry_y,
            entry_angulo,
            ventana
    ):

        try:

            h = float(entry_x.get())
            k = float(entry_y.get())
            angulo = float(entry_angulo.get())

        except ValueError:

            print("Ingrese valores numericos")
            return

        puntos = self.figura.obtener_puntos()

        nuevos_puntos = self.rotacion.rotar(
            puntos,
            angulo,
            h,
            k
        )

        self.figura.cargar_puntos(nuevos_puntos)

        self.centro_rotacion = (h, k)

        self.dibujar_plano()

    def dibujar_trayectorias_grupo(
            self,
            grupo,
            h,
            k,
            centro_x,
            centro_y
    ):

        canvas_h = centro_x + h * self.escala
        canvas_k = centro_y - k * self.escala

        for x, y in grupo:
            radio = math.sqrt(
                (x - h) ** 2 +
                (y - k) ** 2
            )

            radio_canvas = radio * self.escala

            self.canvas.create_oval(
                canvas_h - radio_canvas,
                canvas_k - radio_canvas,
                canvas_h + radio_canvas,
                canvas_k + radio_canvas,
                outline="red",
                width=1
            )
    #dibujar la trayectoria
    def dibujar_trayectorias(self, puntos):

        if self.centro_rotacion is None:
            return

        h, k = self.centro_rotacion

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        centro_x = ancho // 2
        centro_y = alto // 2

        if len(puntos) == 0:
            return

        if isinstance(puntos[0][0], (int, float)):

            self.dibujar_trayectorias_grupo(
                puntos,
                h,
                k,
                centro_x,
                centro_y
            )

        else:

            for grupo in puntos:
                self.dibujar_trayectorias_grupo(
                    grupo,
                    h,
                    k,
                    centro_x,
                    centro_y
                )
    def dibujar_centro_rotacion(self):

        if self.centro_rotacion is None:
            return

        h, k = self.centro_rotacion

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        centro_x = ancho // 2
        centro_y = alto // 2

        canvas_x = centro_x + h * self.escala
        canvas_y = centro_y - k * self.escala

        self.canvas.create_oval(
            canvas_x - 6,
            canvas_y - 6,
            canvas_x + 6,
            canvas_y + 6,
            fill="red",
            outline="black"
        )

        self.canvas.create_text(
            canvas_x + 25,
            canvas_y - 10,
            text=f"({h}, {k})",
            font=("MS Sans Serif", 9)
        )

    def aplicar_reflexion(self):
        opcion = self.comboBoxReflexion.get()
        puntos = self.figura.obtener_puntos()
        if opcion == "Eje x":
            nuevos_puntos = self.reflexion.reflexion_eje_x(puntos)
        elif opcion == "Eje Y":
            nuevos_puntos = self.reflexion.reflexion_eje_y(puntos)
        elif opcion == "Origen":
            nuevos_puntos = self.reflexion.reflexion_origen(puntos)
        elif opcion == "Recta":
            if not self.recta.existe:
                print("Recta no existe")
                return
            a, b ,c = self.recta.obtener_recta()
            print("RECTA:")
            print("A =", a)
            print("B =", b)
            print("C =", c)

            nuevos_puntos = self.reflexion.reflexion_recta(puntos,a,b,c)

        self.figura.cargar_puntos(nuevos_puntos)
        self.dibujar_plano()

    def limpiar_pantalla(self):
        self.figura = Figura()
        self.recta.eliminar_recta()
        self.centro_rotacion = None
        self.dibujar_plano()

    def cargar_figura(self,nombre):
        ruta = Path(__file__).parent.parent / "resources" / "figuras.json"
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        puntos = datos ["figuras"][nombre]["puntos"]
        self.figura.cargar_puntos(puntos)
        self.dibujar_plano()

    def seleccionar_figura(self, combo, ventana):
        figura = combo.get()

        if figura == "Triángulo":
            self.cargar_figura("triangulo")

        elif figura == "Estrella":
            self.cargar_figura("estrella")

        elif figura == "Árbol de Navidad":
            self.cargar_figura("arbol_navidad")


    def abrir_rotacion(self):

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Paint Discreto | Rotación")
        ventana.resizable(False, False)

        ventana.transient(self.ventana)
        ventana.grab_set()

        ventana.configure(background=self.color_panel)

        titulo = tk.Label(
            ventana,
            text="Rotación",
            font=("MS Sans Serif", 10, "bold"),
            bg=self.color_panel,
            fg=self.color_negro,
            relief="raised",
            borderwidth=2,
            padx=10,
            pady=5
        )

        titulo.pack(padx=10, pady=10)

        frame = tk.Frame(
            ventana,
            bg=self.color_panel
        )

        frame.pack(padx=15, pady=5)

        label_x = tk.Label(
            frame,
            text="Centro X:",
            bg=self.color_panel
        )

        label_x.grid(row=0, column=0, padx=5, pady=5)

        entry_x = tk.Entry(
            frame,
            width=10
        )

        entry_x.grid(row=0, column=1, padx=5, pady=5)

        label_y = tk.Label(
            frame,
            text="Centro Y:",
            bg=self.color_panel
        )

        label_y.grid(row=1, column=0, padx=5, pady=5)

        entry_y = tk.Entry(
            frame,
            width=10
        )

        entry_y.grid(row=1, column=1, padx=5, pady=5)

        label_angulo = tk.Label(
            frame,
            text="Ángulo:",
            bg=self.color_panel
        )

        label_angulo.grid(row=2, column=0, padx=5, pady=5)

        entry_angulo = tk.Entry(
            frame,
            width=10
        )

        entry_angulo.grid(row=2, column=1, padx=5, pady=5)

        boton = tk.Button(
            ventana,
            text="Rotar",
            font=("MS Sans Serif", 9),
            relief="raised",
            borderwidth=2,
            command=lambda: self.aplicar_rotacion(
                entry_x,
                entry_y,
                entry_angulo,
                ventana
            )
        )

        boton.pack(pady=(10, 15))

    def abrir_figuras(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Paint Discreto | Add Figure")
        ventana.resizable(False, False)
        ventana.transient(self.ventana)
        ventana.grab_set()
        ventana.configure(background=self.color_panel)

        titulo = tk.Label(
            ventana,
            text="Seleccionar figura",
            font=("MS Sans Serif", 10, "bold"),
            bg=self.color_panel,
            fg=self.color_negro,
            relief="raised",
            borderwidth=2,
            padx=10,
            pady=5
        )
        titulo.pack(padx=10, pady=10)

        combo = ttk.Combobox(
            ventana,
            values=[
                "Triángulo",
                "Estrella",
                "Árbol de Navidad"
            ],
            state="readonly",
            width=20
        )

        combo.pack(padx=15, pady=10)

        boton = tk.Button(
            ventana,
            text="Add",
            font=("MS Sans Serif", 9),
            relief="raised",
            borderwidth=2,
            command=lambda: self.seleccionar_figura(combo, ventana)
        )

        boton.pack(pady=(5, 15))


    def dibujar_grupo_puntos(self, grupo, centro_x, centro_y):

        for i, (x, y) in enumerate(grupo):
            canvas_x = centro_x + x * self.escala
            canvas_y = centro_y - y * self.escala

            self.canvas.create_oval(
                canvas_x - 4,
                canvas_y - 4,
                canvas_x + 4,
                canvas_y + 4,
                fill=self.color_changer.obtener_color()
            )

            self.canvas.create_text(
                canvas_x + 10,
                canvas_y - 10,
                text=f"P:{i + 1}",
                font=self.fuente_Texto
            )

        if len(grupo) >= 2:

            for i in range(len(grupo) - 1):
                x1, y1 = grupo[i]
                x2, y2 = grupo[i + 1]

                canvas_x1 = centro_x + x1 * self.escala
                canvas_y1 = centro_y - y1 * self.escala

                canvas_x2 = centro_x + x2 * self.escala
                canvas_y2 = centro_y - y2 * self.escala

                self.canvas.create_line(
                    canvas_x1,
                    canvas_y1,
                    canvas_x2,
                    canvas_y2,
                    fill="black",
                    width=2
                )

        if len(grupo) >= 3:
            x1, y1 = grupo[-1]
            x2, y2 = grupo[0]

            canvas_x1 = centro_x + x1 * self.escala
            canvas_y1 = centro_y - y1 * self.escala

            canvas_x2 = centro_x + x2 * self.escala
            canvas_y2 = centro_y - y2 * self.escala

            self.canvas.create_line(
                canvas_x1,
                canvas_y1,
                canvas_x2,
                canvas_y2,
                fill="black",
                width=2
            )


    def dibujar_figura(self):
        puntos = self.figura.obtener_puntos()
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        centro_x = ancho//2
        centro_y = alto//2
        if len(puntos) > 0 and isinstance(puntos[0][0], (int, float)):
            self.dibujar_grupo_puntos(
                puntos,
                centro_x,
                centro_y
            )
        else:
            for grupo in puntos:
                self.dibujar_grupo_puntos(
                    grupo,
                    centro_x,
                    centro_y
                )

    def crear_punto(self):
        try:
            x = float(self.entry_X.get())
            y = float(self.entry_Y.get())
        except ValueError:
            print("Ingrese valores numericos")
            return
        agregado = self.figura.agregar_punto(x,y)
        if not agregado:
            print("Ya existen 4 puntos")
            return
        print("punto agregado: ",x,y)
        self.entry_X.delete(0, tk.END)
        self.entry_Y.delete(0, tk.END)
        self.dibujar_plano()

    def dibujar_recta(self):

        if not self.recta.existe:
            return

        a, b, c = self.recta.obtener_recta()

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        centro_x = ancho // 2
        centro_y = alto // 2

        if b != 0:
            x1 = -centro_x / self.escala
            x2 = centro_x / self.escala

            y1 = (-a * x1 - c) / b
            y2 = (-a * x2 - c) / b

            canvas_x1 = centro_x + x1 * self.escala
            canvas_y1 = centro_y - y1 * self.escala

            canvas_x2 = centro_x + x2 * self.escala
            canvas_y2 = centro_y - y2 * self.escala

            self.canvas.create_line(
                canvas_x1,
                canvas_y1,
                canvas_x2,
                canvas_y2,
                fill="blue",
                width=2
            )

    def dibujar_plano(self,event=None):
        self.canvas.delete("all")
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        centro_x = ancho //2
        centro_y = alto //2

        #
        for x in range(centro_x, ancho, self.escala):
            self.canvas.create_line(
                x,0,
                x,alto,
                fill="lightgray"
            )
        for x in range(centro_x, 0, -self.escala):
            self.canvas.create_line(
                x,0,
                x,alto,
                fill="lightgray"
            )
        #vertical
        for y in range(centro_y, alto, self.escala):
            self.canvas.create_line(
                0,y,
                ancho,y,
                fill="lightgray"
            )
        for y in range(centro_y, 0, -self.escala):
            self.canvas.create_line(
                0,y,
                ancho,y,
                fill="lightgray"
            )
        #eje x
        self.canvas.create_line(
            0,centro_y,
            ancho,centro_y,
            fill="black",
            width=2
        )
        for x in range(-centro_x // self.escala, centro_x  // self.escala+1):
            if x != 0  and self.escala >=20:
                canvas_x = centro_x + x * self.escala
                self.canvas.create_text(
                    canvas_x,
                    centro_y + 15,
                    text=str(x),
                    font=("MS Sans Serif", 5),
                )

        #eje y
        self.canvas.create_line(
            centro_x,0,
            centro_x,alto,
            fill="black",
            width=2
        )
        for y in range(-centro_y // self.escala, centro_y // self.escala + 1):
            if y != 0  and self.escala >=20:
                canvas_y = centro_y - y * self.escala

                self.canvas.create_text(
                    centro_x - 15,
                    canvas_y,
                    text=str(y),
                    font=("MS Sans Serif", 5)
                )
        #flechas
        self.canvas.create_line(
            ancho-10, centro_y,
            ancho, centro_y,
            fill="black",
            width=2,
            arrow=tk.LAST
        )
        self.canvas.create_line(
            centro_x, 10,
            centro_x,0,
            fill="black",
            width=2,
            arrow=tk.LAST
        )
        #etiquetas
        self.canvas.create_text(
            ancho-15, centro_y-15,
            text="X",
            font=self.fuente_Texto
        )
        self.canvas.create_text(
            centro_x + 15, 15,
            text="Y",
            font=self.fuente_Texto
        )
        self.canvas.create_text(
            centro_x + 15, centro_y + 15,
            text="0",
            font=self.fuente_Texto
        )
        self.dibujar_trayectorias(
            self.figura.obtener_puntos()
        )

        self.dibujar_recta()

        self.dibujar_centro_rotacion()

        self.dibujar_figura()


    def mostrar_coordenadas(self,event):
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        centro_x=ancho//2
        centro_y=alto//2
        x = round((event.x -centro_x)/self.escala)
        y = round((centro_y-event.y)/self.escala)
        self.label_coordenadas.config(
            text=f"Coord: ({x};{y})"
        )

    def aumentar_escala(self):
        self.escala +=5
        self.label_escala.config(text=str(self.escala))
        self.dibujar_plano()
    def disminuir_escala(self):
        if self.escala>5:
            self.escala -=5
        self.label_escala.config(text=str(self.escala))
        self.dibujar_plano()

    def crear_label(self,padre,text):
        return tk.Label(
            padre,
            text=text,
            font=self.fuente_Texto,
            fg=self.color_negro,
            borderwidth=2,
            padx=5,
            pady=3
        )
    def crear_boton(self,padre,text):
        return tk.Button(
            padre,
            text=text,
            font=self.fuente_Texto,
            bg=self.color_panel,
            fg=self.color_negro,
            relief="raised",
            borderwidth=2,
            padx=5,
            pady=3,
        )

    def mostrar_menu_file(self):
        self.menu_file.post(
            self.boton_file.winfo_rootx(),
            self.boton_file.winfo_rooty()+self.boton_file.winfo_width()-20,
        )
    def mostrar_menu_config(self):
        self.menu_config.post(
            self.boton_file.winfo_rootx()+125,
            self.boton_file.winfo_rooty()+self.boton_file.winfo_height(),
        )
    def mostrar_menu_help(self):
        self.menu_help.post(
            self.boton_file.winfo_rootx()+200,
            self.boton_file.winfo_rooty()+self.boton_file.winfo_height(),
        )
    def mostrar_add_help(self):
        self.menu_add.post(
            self.boton_file.winfo_rootx()+275,
            self.boton_file.winfo_rooty()+self.boton_file.winfo_height(),
        )

    def abrir_recta(self):
        ventana = tk.Toplevel(self.ventana)

        ventana.title("Paint Discreto | Agregar recta")
        ventana.resizable(False, False)

        ventana.transient(self.ventana)
        ventana.grab_set()

        ventana.configure(background=self.color_panel)

        titulo = tk.Label(
            ventana,
            text="Ecuación general de la recta",
            font=("MS Sans Serif", 10, "bold"),
            bg=self.color_panel,
            fg=self.color_negro,
            relief="raised",
            borderwidth=2,
            padx=10,
            pady=5
        )

        titulo.pack(padx=10, pady=10)

        frame = tk.Frame(
            ventana,
            bg=self.color_panel
        )

        frame.pack(padx=15, pady=5)

        label_a = tk.Label(
            frame,
            text="A:",
            bg=self.color_panel
        )

        label_a.grid(row=0, column=0, padx=5, pady=5)

        entry_a = tk.Entry(frame, width=10)

        entry_a.grid(row=0, column=1, padx=5, pady=5)

        label_b = tk.Label(
            frame,
            text="B:",
            bg=self.color_panel
        )

        label_b.grid(row=1, column=0, padx=5, pady=5)

        entry_b = tk.Entry(frame, width=10)

        entry_b.grid(row=1, column=1, padx=5, pady=5)

        label_c = tk.Label(
            frame,
            text="C:",
            bg=self.color_panel
        )

        label_c.grid(row=2, column=0, padx=5, pady=5)

        entry_c = tk.Entry(frame, width=10)

        entry_c.grid(row=2, column=1, padx=5, pady=5)

        boton = tk.Button(
            ventana,
            text="Agregar recta",
            font=("MS Sans Serif", 9),
            relief="raised",
            borderwidth=2,
            command=lambda: self.agregar_recta(
                entry_a,
                entry_b,
                entry_c,
                ventana
            )
        )

        boton.pack(pady=(10, 15))
    def crear_Menu(self):
        ##refactorizar xd
        self.barra_menu = tk.Frame(self.ventana,
                                    bg=self.color_panel,
                                    relief="raised",
                                    borderwidth=2)
        self.barra_menu.pack(side=tk.TOP,fill=tk.X)
        ##| file |
        self.menu_file = tk.Menu(self.barra_menu,
                                 tearoff=0,
                                 bg=self.color_panel,
                                 fg=self.color_negro,
                                 activebackground="#000080",
                                 activeforeground="white",
                                 relief="raised",
                                 borderwidth=2,
                                 font=self.fuente_Texto)

        self.menu_file.add_command(label="Open .csv")
        self.menu_file.add_command(label="Open .xlsx")
        self.menu_file.add_command(label="Open .txt")
        self.boton_file = tk.Button(
            self.barra_menu,
            text="File",
            font=self.fuente_Texto,
            bg=self.color_panel,
            fg=self.color_negro,
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=3,
            command=self.mostrar_menu_file
        )
        self.boton_file.pack(side=tk.LEFT)

        ## | menu_about|
        self.boton_about = tk.Button(
            self.barra_menu,
            text="About",
            font=self.fuente_Texto,
            bg=self.color_panel,
            fg=self.color_negro,
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=3,
            command=self.abrir_about
        )

        self.boton_about.pack(side=tk.LEFT)
        # | config |
        self.menu_config = tk.Menu(self.barra_menu,
                                   tearoff=0,
                                   bg=self.color_panel,
                                   fg=self.color_negro,
                                   activebackground="#000080",
                                   activeforeground="white",
                                   relief="raised",
                                   borderwidth=2,
                                   font=self.fuente_Texto,
                                   )
        self.boton_config = tk.Button(
            self.barra_menu,
            text="Config",
            font=self.fuente_Texto,
            bg=self.color_panel,
            fg=self.color_negro,
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=3,
            command=self.mostrar_menu_config
        )
        self.menu_config.add_command(label="Point Color", command=self.color_changer.abrir_venta )
        self.boton_config.pack(side=tk.LEFT)
        ## | help |
        self.menu_help = tk.Menu(self.barra_menu,
                                 tearoff=0,
                                 bg=self.color_panel,
                                 fg=self.color_negro,
                                 activebackground="#000080",
                                 activeforeground="white",
                                 relief="raised",
                                 borderwidth=2,
                                 font=self.fuente_Texto)
        self.boton_help= tk.Button(
            self.barra_menu,
            text="Help",
            font=self.fuente_Texto,
            bg=self.color_panel,
            fg=self.color_negro,
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=3,
            command=self.mostrar_menu_help
        )
        self.menu_help.add_command(label="Exit", command=exit)
        self.menu_help.add_command(label="Reset", command=self.limpiar_pantalla)
        self.boton_help.pack(side=tk.LEFT)
        self.menu_add = tk.Menu(self.barra_menu,
                                 tearoff=0,
                                 bg=self.color_panel,
                                 fg=self.color_negro,
                                 activebackground="#000080",
                                 activeforeground="white",
                                 relief="raised",
                                 borderwidth=2,
                                 font=self.fuente_Texto)
        self.boton_add = tk.Button(
            self.barra_menu,
            text="Add",
            font=self.fuente_Texto,
            bg=self.color_panel,
            fg=self.color_negro,
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=3,
            command=self.mostrar_add_help
        )
        self.menu_add.add_command(label="Figure",    command=self.abrir_figuras)
        self.menu_add.add_command(label="Line",    command=self.abrir_recta)
        self.menu_add.add_command(label="Rotacion",    command=self.abrir_rotacion)
        self.boton_add.pack(side=tk.LEFT)

        return self.barra_menu

    def agregar_recta(self, entry_a, entry_b, entry_c, ventana):
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
        except ValueError:
            print("Ingrese valores numericos")
            return
        if a == 0 and b == 0:
            print("La recta no es valida")
            return
        self.recta.establecer_recta(a, b, c)
        ventana.destroy()

        self.dibujar_plano()
    def abrir_about(self):
        venta_about = tk.Toplevel(self.ventana)
        #ventana-----------------------------------------------------
        venta_about.title("About - Paint Discreto")
        venta_about.resizable(False,False)
        venta_about.transient(self.ventana)
        venta_about.grab_set()
        venta_about.configure(background=self.color_panel)

        #Titulo: Pain discreto-----------------------------------------------------
        titulo = self.crear_label(venta_about,"Paint Discreto")
        titulo.config(font=self.fuente_Texto, bg=self.color_panel, fg=self.color_negro, relief="raised", borderwidth=2, padx=10,pady=5)
        titulo.pack(pady=5)
        #Titulo: Creditos-----------------------------------------------------
        creditos = self.crear_label(venta_about,"Authors")
        creditos.config(font=self.fuente_Texto, bg=self.color_panel, fg=self.color_negro, relief="groove", borderwidth=2,
                      padx=10, pady=5)
        creditos.pack(pady=5,padx=15, fill=tk.X)
        #Titulo: Nombres-----------------------------------------------------
        autores = self.crear_label(venta_about, "Leonardo Favio Jimenez Layme (U202611731)\n\n Alex Guevara Herrera (U20261A781)\n\n Jamie Nicole Rodriguez Salcedo (U202520442)\n\n Fabricio Jesus Villaizan Tacuche(U20251o921)\n\n Emerson Jeampierre Nolasco Ayala (U20251F206)")
        autores.configure(relief="raised",fg=self.color_negro, justify="center",font=self.fuente_Texto)
        autores.pack(pady=5, padx=10)
        #Titulo: Profesor-----------------------------------------------------
        profesor = self.crear_label(venta_about, "Teachers")
        profesor.configure(fg=self.color_negro,bg=self.color_panel, relief="groove",borderwidth=2, padx=10,pady=5)
        profesor.pack(pady=5,padx=10, fill=tk.X)
        #Titulo: Nombre Profesor-----------------------------------------------------
        nombreProfesor = self.crear_label(venta_about, "Antonio Marcos Medina Martínez\n\n Renan Muñoz Trelles")
        nombreProfesor.configure(fg=self.color_negro,bg=self.color_panel,relief="raised",borderwidth=2, padx=10,pady=5)
        nombreProfesor.pack(pady=5,padx=15, fill=tk.X)
        #Titulo: Programa-----------------------------------------------------
        autores.configure(font=self.fuente_Texto,bg=self.color_panel,fg=self.color_negro)
        texto = self.crear_label(venta_about, "Editor gráfico para Matemática Discreta\n\n Proyecto desarrollado para UPC")
        texto.configure(font=self.fuente_Texto,bg=self.color_panel,fg=self.color_negro)
        texto.pack(pady=(10,5))
        #Titulo: Logo UPC-----------------------------------------------------
        logoUpc = Image.open("UpcLogoPNG.png")
        logoUpc = logoUpc.resize((100,100))

        self.logoUpc = ImageTk.PhotoImage(logoUpc)
        label_logo = tk.Label(
            venta_about,
            image=self.logoUpc,
            bg=self.color_panel,
        )
        label_logo.pack(pady=(15,10))

    def configurar_ventana(self):
        self.ventana.title("Paint Discreto")
        self.ventana.geometry("1100x720")
        self.ventana.minsize(1020,600)
        self.crear_Menu()
        self.ventana.resizable(False,False)

    def componente_Coordenadas(self):
        #border coords
        self.frame_Coords = tk.LabelFrame(self.frame_derecho, text="Coordenadas",font=self.fuente_Titulo ,bg="gray94", border=1, borderwidth=2,relief="sunken", padx=5, pady=5)
        self.frame_Coords.pack(fill=tk.X, pady=5, padx=5)
            #50/50
        self.frame_Coords.columnconfigure(0, weight=1)
        self.frame_Coords.columnconfigure(1, weight=1)
        #Label X
        self.label_X= tk.Label(self.frame_Coords, text="X:", font=self.fuente_Texto,bg="gray94" ,fg="black")
        self.label_X.grid(row=1, column=0, padx=10, pady=5)

        #entry coord X
        self.entry_X = tk.Entry(self.frame_Coords, font=self.fuente_Texto,bg="white")
        self.entry_X.grid(row=1, column=1, padx=10, pady=5)

        #Label Y
        self.label_Y = tk.Label(self.frame_Coords, text="Y:", font=self.fuente_Texto,bg="gray94",fg="black" )
        self.label_Y.grid(row=2, column=0, padx=10, pady=5)
        #entry coord y
        self.entry_Y = tk.Entry(self.frame_Coords, font=self.fuente_Texto,bg="white")
        self.entry_Y.grid(row=2, column=1, padx=10, pady=5)
        #submit
        self.submit_Coords = self.crear_boton(self.frame_Coords,"Crear punto")
        self.submit_Coords.config(
            command = self.crear_punto
        )
        self.submit_Coords.grid(row=3, column=0,columnspan=2,sticky="ew", padx=10, pady=5)
    def component_reflexion(self):
        self.frame_reflexion = tk.LabelFrame(self.frame_derecho,text="Reflexion", font=self.fuente_Titulo,bg="gray94", border=1, borderwidth=2, relief="sunken", padx=10, pady=10)
        self.frame_reflexion.pack(fill=tk.X, pady=5, padx=5)
        self.frame_reflexion.columnconfigure(0, weight=1)
        #Estilo
        estilo = ttk.Style()
        estilo.configure("Reflexion.TComboBox", font=("MS Sans Serif", 11),padding=5)
        ##Buttons
        self.comboBoxReflexion = ttk.Combobox(self.frame_reflexion, values=["Eje x","Eje Y","Origen","Recta"],
                                              state="readonly",style="Reflexion.TCombobox", font=self.fuente_Texto)
        self.comboBoxReflexion.grid(row=1, column = 0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.comboBoxReflexion.current(0)
        self.boton_Reflexion = self.crear_boton(
            self.frame_reflexion, "Aplicar reflexión")
        self.boton_Reflexion.config(command=self.aplicar_reflexion)
        self.boton_Reflexion.grid(row=3,column=0,sticky="ew", padx=5, pady=2)
    def componente_homotecia(self):
        #contorno
        self.frame_homotecia= tk.LabelFrame(self.frame_derecho,text="Homotecia" ,font=self.fuente_Titulo,bg="gray94", border=1, borderwidth=2, relief="sunken",
                                        padx=10, pady=10)
        self.frame_homotecia.pack(fill=tk.X, pady=5, padx=5)
        self.frame_homotecia.columnconfigure(1, weight=1)
        #Homotecia
        self.label_factor = tk.Label(self.frame_homotecia, text="Factor ", font=self.fuente_Texto,bg="gray94",fg="black")
        self.label_factor.grid(row=0, column=0, padx=5, pady=5)
        self.entry_factor= tk.Spinbox(self.frame_homotecia,from_=-100,to=100,increment=0.1, font=self.fuente_Texto,bg="white")
        self.entry_factor.delete(0,tk.END)
        self.entry_factor.insert(0,"0")
        self.entry_factor.grid(row=0, column=1,sticky="ew", padx=10, pady=5)

        self.boton_homotecia = self.crear_boton(
            self.frame_homotecia,"Aplicar")
        self.boton_homotecia.config(command=self.aplicar_homotecia)
        self.boton_homotecia.grid(row=1,column=0,sticky="ew", padx=5, pady=2,columnspan=2)
    def componente_rotacion(self):
        self.labelFrame_rotacion = tk.LabelFrame(self.frame_derecho, text="Rotación", font=self.fuente_Titulo, bg="gray94",
                                             border=1, borderwidth=2, relief="sunken",
                                             padx=10, pady=10)
        self.labelFrame_rotacion.pack(fill=tk.X, pady=5, padx=5)
        self.labelFrame_rotacion.columnconfigure(1, weight=1)
        self.label_rotacion = tk.Label(self.labelFrame_rotacion, text="Ángulo de rotación",font=self.fuente_Texto,bg="gray94",fg="black",
                                       padx=10, pady=10)
        self.label_rotacion.grid(row=0, column=0, padx=5, pady=5)
        self.spinBox_rotacion = tk.Spinbox(self.labelFrame_rotacion, from_=-360, to=360,increment=1,font=self.fuente_Texto,bg="white",width=10)
        self.spinBox_rotacion.delete(0,tk.END)
        self.spinBox_rotacion.insert(0,"0")
        self.spinBox_rotacion.grid(row=0, column=1, padx=5, pady=5)
        self.boton_rotacion = self.crear_boton(
            self.labelFrame_rotacion, "Rotar")
        self.boton_rotacion.config(command=self.aplicar_rotacion)
        self.boton_rotacion.grid(row=1,column=0,sticky="ew", padx=5, pady=2,columnspan=2)
    def componente_escala(self):
        self.frame_escala = tk.Frame(
            self.frame_derecho,
        )
        self.frame_escala.pack(fill=tk.X, pady=5, padx=5)
        self.label_escala= self.crear_label(self.frame_escala,"Escala: ")
        self.label_escala.grid(row=0, column=0,padx=5, pady=5)
        self.boton_disminuir= self.crear_boton(
            self.frame_escala,
            "-"
        )
        self.boton_disminuir.config(command=self.disminuir_escala)
        self.boton_disminuir.grid(row = 0, column=1, padx=5,pady=5)

        self.label_escala = self.crear_label(
            self.frame_escala,
            str(self.escala)
        )
        self.label_escala.grid(row = 0, column=2, padx=5,pady=5)

        self.boton_aumentar= self.crear_boton(
            self.frame_escala,
            "+"
        )
        self.boton_aumentar.config(command=self.aumentar_escala)
        self.boton_aumentar.grid(row = 0, column=3, padx=5,pady=5)
        self.label_coordenadas=self.crear_label(
            self.frame_escala,
            "Coord: (0; 0)"
        )
        self.label_coordenadas.grid(row = 0, column=4, padx=5,pady=5)

    def crear_frame_izquierdo(self):
        # Frame izquierdo
        self.frame_izquierdo = tk.Frame(self.ventana, bg="gray94")
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, pady=10, padx=10, expand=True)
        # Canvas / plano cartesiano
        self.canvas = tk.Canvas(
            self.frame_izquierdo,
            bg="white", relief="sunken",borderwidth=2,highlightthickness=2,highlightcolor="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>",self.dibujar_plano)
        self.canvas.bind("<Motion>",self.mostrar_coordenadas)

    def crear_frame_derecho(self):
        # Frame derecho
        self.frame_derecho = tk.Frame(self.ventana, bg="gray94", width=80)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, pady=10, padx=(0, 10), expand=True)
        self.frame_derecho.pack_propagate(False)
        self.componente_Coordenadas()
        self.component_reflexion()
        self.componente_homotecia()
        self.componente_rotacion()
        self.componente_escala()

    def crear_componentes(self):
        self.crear_frame_izquierdo()
        self.crear_frame_derecho()

    def ejecutar(self):
        self.ventana.mainloop()

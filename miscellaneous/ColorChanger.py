import tkinter as tk
from tkinter import colorchooser
class ColorChanger:
    def __init__(self, ventana_padre):
        self.ventana_padre = ventana_padre
        self.color = "red"

    def abrir_venta(self):
        ventana = tk.Toplevel(self.ventana_padre.ventana)
        ventana.title("Pain Discreto | Color Changer")
        ventana.resizable(False,False)
        ventana.transient(self.ventana_padre.ventana)
        ventana.grab_set()
        ventana.configure(background="#d4d0c8")
        titulo = tk.Label(
            ventana,
            text="Configuración de color",
            font=("MS Sans Serif", 10, "bold"),
            bg="#d4d0c8",
            fg="black",
            relief="raised",
            borderwidth=2,
            padx=10,
            pady=5
        )

        titulo.pack(
            pady=10,
            padx=10
        )

        boton = tk.Button(
            ventana,
            text="Seleccionar color",
            font=("MS Sans Serif", 9),
            command=self.selec_color,
            bg="#d4d0c8",
            relief="raised",
            borderwidth=2
        )

        boton.pack(
            padx=15,
            pady=10
        )

        self.muestra_color = tk.Label(
            ventana,
            text="Color actual",
            bg=self.color,
            fg="#d4d0c8",
            relief="sunken",
            borderwidth=2,
            width=20,
            height=2
        )

        self.muestra_color.pack(
            padx=15,
            pady=10
        )

        boton_cerrar = tk.Button(
            ventana,
            text="OK",
            font=("MS Sans Serif", 9),
            command=ventana.destroy,
            bg="#d4d0c8",
            relief="raised",
            borderwidth=2,
            padx=15
        )

        boton_cerrar.pack(
            pady=(5, 15)
        )
    def selec_color(self):
        color = colorchooser.askcolor(title="Seleccionar color")
        if color[1] is not None:
            self.cambiar_color(color[1])
            self.muestra_color.config(
                bg=self.color
            )
            self.ventana_padre.dibujar_plano()


    def cambiar_color(self,color):
        self.color = color;

    def obtener_color(self):
        return self.color;

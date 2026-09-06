import tkinter as tk
from tkinter import ttk
class VentanaPrincipal:
    def __init__(self):
       self.fuente_Titulo = ("MS Sans Serif",14, "bold")
       self.fuente_Texto= ("MS Sans Serif",12, "bold")
       self.color_fondo="#c0c0c0"
       self.color_panel="#d4d0c8"
       self.color_blanco="#ffffff"
       self.color_negro="#000000"
       self.ventana = tk.Tk()
       self.configurar_ventana()
       self.crear_componentes()



    def dibujar_plano(self,event=None):
        self.canvas.delete("all")
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        centro_x = ancho //2
        centro_y = alto //2
        escala = 25 #se tendria que testear

        #
        for x in range(centro_x, ancho, escala):
            self.canvas.create_line(
                x,0,
                x,alto,
                fill="lightgray"
            )
        for x in range(centro_x, 0, -escala):
            self.canvas.create_line(
                x,0,
                x,alto,
                fill="lightgray"
            )
        #vertical
        for y in range(centro_y, alto, escala):
            self.canvas.create_line(
                0,y,
                ancho,y,
                fill="lightgray"
            )
        for y in range(centro_x, 0, -escala):
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
        #eje y
        self.canvas.create_line(
            centro_x,0,
            centro_x,alto,
            fill="black",
            width=2
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
    def crear_Menu(self):
        self.barra_menu = tk.Menu(self.ventana)
        ##| file |
        self.menu_file = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_file.add_command(label="Abrir .csv")
        self.menu_file.add_command(label="Abrir .xlsx")
        self.menu_file.add_command(label="Abrir .txt")
        self.barra_menu.add_cascade(label="Files", menu=self.menu_file)
        ## | credits |
        self.menu_credits= tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="About", menu=self.menu_credits)
        ## | help |
        self.menu_help = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Help", menu=self.menu_help)
        return self.barra_menu

    def configurar_ventana(self):
        self.ventana.title("Paint Discreto")
        self.ventana.geometry("1020x620")
        self.ventana.minsize(1020,600)
        self.ventana.config(menu=self.crear_Menu())
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
        self.submit_Coords.grid(row=3, column=0,columnspan=2,sticky="ew", padx=10, pady=5)
    def component_reflexion(self):
        self.frame_reflexion = tk.LabelFrame(self.frame_derecho,text="Reflexion", font=self.fuente_Titulo,bg="gray94", border=1, borderwidth=2, relief="sunken", padx=10, pady=10)
        self.frame_reflexion.pack(fill=tk.X, pady=5, padx=5)
        self.frame_reflexion.columnconfigure(0, weight=1)
        #Estilo
        estilo = ttk.Style()
        estilo.configure("Reflexion.TComboBox", font=("MS Sans Serif", 11),padding=5)
        ##Buttons
        self.comboBoxReflexion = ttk.Combobox(self.frame_reflexion, values=["Eje x","Eje Y","Origen"],
                                              state="readonly",style="Reflexion.TCombobox")
        self.comboBoxReflexion.grid(row=1, column = 0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.comboBoxReflexion.current(0)
        self.boton_Reflexion = self.crear_boton(
            self.frame_reflexion, "Aplicar reflexión")
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
        self.boton_rotacion.grid(row=1,column=0,sticky="ew", padx=5, pady=2,columnspan=2)

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

    def crear_frame_derecho(self):
        # Frame derecho
        self.frame_derecho = tk.Frame(self.ventana, bg="gray94", width=80)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, pady=10, padx=(0, 10), expand=True)
        self.frame_derecho.pack_propagate(False)
        self.componente_Coordenadas()
        self.component_reflexion()
        self.componente_homotecia()
        self.componente_rotacion()

    def crear_componentes(self):
        self.crear_frame_izquierdo()
        self.crear_frame_derecho()

    def ejecutar(self):
        self.ventana.mainloop()

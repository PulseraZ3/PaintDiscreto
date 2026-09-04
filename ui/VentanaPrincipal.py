import tkinter as tk
class VentanaPrincipal:
    def __init__(self):
       self.fuente_Titulo = ("MS Sans Serif",14, "bold")
       self.fuente_Texto= ("MS Sans Serif",12, "bold")
       self.ventana = tk.Tk()
       self.configurar_ventana()
       self.crear_componentes()
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
        self.ventana.geometry("1020x600")
        self.ventana.minsize(1020,600)
        self.ventana.config(menu=self.crear_Menu())
        self.ventana.resizable(False,False)

    def componente_Coordenadas(self):
        #border coords
        self.frame_Coords = tk.Frame(self.frame_derecho, bg="white", border=1, borderwidth=2,relief="solid", padx=5, pady=5)
        self.frame_Coords.pack(fill=tk.X, pady=5, padx=5)
            #50/50
        self.frame_Coords.columnconfigure(0, weight=1)
        self.frame_Coords.columnconfigure(1, weight=1)

        #Coords
        self.label_Coords = tk.Label(self.frame_Coords, text="Coords", font=self.fuente_Titulo,bg="white",fg="black")
        self.label_Coords.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew", #se puede estirar por ambas columnas
            pady=5
        )

        #Label X
        self.label_X= tk.Label(self.frame_Coords, text="X:", font=self.fuente_Texto,bg="white" ,fg="black")
        self.label_X.grid(row=1, column=0, padx=10, pady=5)

        #entry coord X
        self.entry_X = tk.Entry(self.frame_Coords, font=self.fuente_Texto,bg="white")
        self.entry_X.grid(row=1, column=1, padx=10, pady=5)

        #Label Y
        self.label_Y = tk.Label(self.frame_Coords, text="Y:", font=self.fuente_Texto,bg="white",fg="black" )
        self.label_Y.grid(row=2, column=0, padx=10, pady=5)
        #entry coord y
        self.entry_Y = tk.Entry(self.frame_Coords, font=self.fuente_Texto,bg="white")
        self.entry_Y.grid(row=2, column=1, padx=10, pady=5)
        #submit
        self.submit_Coords = tk.Button(self.frame_Coords, text="Crear punto", font=self.fuente_Texto,)
        self.submit_Coords.grid(row=3, column=0,columnspan=2,sticky="ew", padx=10, pady=5)
    def component_reflexion(self):
        self.frame_file = tk.Frame(self.frame_derecho, bg="white", border=1, borderwidth=2, relief="solid", padx=5, pady=5)
        self.frame_file.pack(fill=tk.X, pady=5, padx=5)
        self.frame_file.columnconfigure(0, weight=1)
        self.frame_file.columnconfigure(1, weight=1)

        #File
        self.label_File = tk.Label(self.frame_file,text="Reflexion",font=self.fuente_Titulo,bg="white",fg="black")
        self.label_File.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=5
        )
        ##Buttons
        ##eje x
        ##eje y
        ##X = Y
        ##Y = -X


    def crear_frame_izquierdo(self):
        # Frame izquierdo
        self.frame_izquierdo = tk.Frame(self.ventana, bg="white")
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, pady=10, padx=10, expand=True)
        # Canvas / plano cartesiano
        self.canvas = tk.Canvas(
            self.frame_izquierdo,
            bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def crear_frame_derecho(self):
        # Frame derecho
        self.frame_derecho = tk.Frame(self.ventana, bg="gray94", width=80)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, pady=10, padx=(0, 10), expand=True)
        self.frame_derecho.pack_propagate(False)
        self.componente_Coordenadas()
        self.component_reflexion()

    def crear_componentes(self):
        self.crear_frame_izquierdo()
        self.crear_frame_derecho()

    def ejecutar(self):
        self.ventana.mainloop()

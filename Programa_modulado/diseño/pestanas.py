import tkinter as tk
from tkinter import ttk

class Pestanas:
    def __init__(self, ventana):
        self.pestanas = ttk.Notebook(ventana, style="TNotebook")
        self.pestanas.pack(fill="both", expand=True)

        self.pagina_1 = tk.Frame(self.pestanas)
        self.pagina_2 = tk.Frame(self.pestanas)

        self.pagina_1.config(bg="#1E1E1E", highlightbackground="#1E1E1E", relief="ridge")
        self.pagina_2.config(bg="#1E1E1E", highlightbackground="#1E1E1E", relief="ridge")

        self.pestanas.add(self.pagina_1, text="Ingreso")
        self.pestanas.add(self.pagina_2, text="Historial")
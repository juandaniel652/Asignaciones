import tkinter as tk
import time

class Reloj :

    def __init__ (self, parent, fuente_titulo) :

        self.parent = parent
        self.fuente_titulo = fuente_titulo
        self.label = tk.Label(
            parent,
            fg="#E0E0E0",
            bg="#333333",
            font=fuente_titulo,
            relief="solid"
        )
        self.label.grid(row=0, column=4, padx=10, pady=10, sticky="ew")
        self._actualizar_reloj()

    def _actualizar_reloj (self) :

        hora_actual = time.strftime("%H:%M:%S")
        self.label.config(text=hora_actual)
        self.label.after(1000, self._actualizar_reloj)
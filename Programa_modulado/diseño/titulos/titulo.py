import tkinter as tk

class Titulos:
    def __init__(self, parent, fuente_titulo):
        titulos = [("Acomodadores", 0), ("Vigilancia", 1), ("Semanas", 2), ("Limpieza", 3)]
        self.titulos_labels = {}
        for texto, columnas in titulos:
            titulo = tk.Label(
                parent,
                text=texto,
                fg="#E0E0E0",
                relief="solid",
                font=fuente_titulo,
                bg="#333333"
            )
            self.titulos_labels[texto.lower()] = titulo

        self.titulo_acomodadores = self.titulos_labels["acomodadores"]
        self.titulo_vigilancia = self.titulos_labels["vigilancia"]
        self.titulo_fecha = self.titulos_labels["semanas"]
        self.titulo_limpieza = self.titulos_labels["limpieza"]
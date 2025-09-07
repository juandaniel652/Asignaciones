from tkinter import Text

class CajaFecha:
    def __init__(self, parent, fuente_titulo):
        # Ajusta el tamaño para que sea proporcional a los listboxes
        self.text_fecha = Text(
            parent,
            state = "disabled",
            height=10,
            width=26,
            font=fuente_titulo,
            fg="#E0E0E0",
            bg="#424242",
            relief="raised",  # Igual que los listbox
            bd=2              # Grosor del borde similar al listbox por defecto
        )
        self.text_fecha.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
import tkinter as tk

class Listboxes :

    def __init__(self, parent, fuente_listbox):
        # Ajusta el ancho y alto para mejor proporción visual con el Text
        listbox_info = [
            ("listbox_acomodadores", {"width": 22, "height": 10}),
            ("listbox_vigilancia", {"width": 22, "height": 10}),
            ("listbox_de_fechas", {"width": 26, "height": 10}),
        ]
        for name, options in listbox_info:
            caja = tk.Listbox(
                parent,
                relief="raised",
                font=fuente_listbox,
                fg="#E0E0E0",
                bg="#424242",
                **options
            )
            setattr(self, name, caja)
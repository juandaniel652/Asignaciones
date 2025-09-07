import tkinter as tk

class BotonesGenerales:
    def __init__(self, parent, app):
        estilo_boton = {
            "relief": "raised",
            "background": "#2196F3",
            "foreground": "#FFFFFF",
            "activebackground": "#1565C0",
            "activeforeground": "#FFFFFF",
            "font": ("Segoe UI", 11, "bold"),
            "bd": 2,
            "cursor": "hand2"
        }

        boton_oscuro = tk.Button(parent, text="Modo Oscuro", **estilo_boton)
        boton_claro = tk.Button(parent, text="Modo Claro", **estilo_boton)
        app.boton_entresemana = tk.Button(parent, text="Entre semana", **estilo_boton)
        app.boton_fin_de_semana = tk.Button(parent, text="Fin de semana", **estilo_boton)
        boton_salir = tk.Button(parent, text="Salir", **estilo_boton)

        botones = [
            boton_oscuro,
            boton_claro,
            app.boton_entresemana,
            app.boton_fin_de_semana,
            boton_salir
        ]

        for columna, boton in enumerate(botones):
            boton.grid(row=7, column=columna, padx=10, pady=15, sticky="ew")

        parent.rowconfigure(2, weight=0)
        for i in range(len(botones)):
            parent.columnconfigure(i, weight=1)
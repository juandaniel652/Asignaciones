import tkinter as tk

class BotonesSemana:
    def __init__(self, parent, app):
        estilo_boton = {
            "relief": "raised",
            "background": "#1976D2",
            "foreground": "#FFFFFF",
            "activebackground": "#1565C0",
            "activeforeground": "#FFFFFF",
            "font": ("Segoe UI", 10, "bold"),
            "bd": 2,
            "cursor": "hand2"
        }

        # Botón "Mostrar" en la fila de semana (row=2, column=3)
        self.boton_mostrar = tk.Button(
            parent,
            text="Mostrar",
            **estilo_boton,
            command=getattr(app, "mostrar_semana", lambda: None)
        )
        self.boton_mostrar.grid(row=2, column=2, padx=10, pady=(0, 5), sticky="ew")

        # Botón "Remover" en la siguiente columna (row=2, column=4)
        self.boton_remover = tk.Button(
            parent,
            text="Remover",
            **estilo_boton,
            command=getattr(app, "remover_semana", lambda: None)
        )
        self.boton_remover.grid(row=2, column=3, padx=(10, 5), pady=(0, 2), sticky="ew")

        # Botón "Guardar datos" debajo de "Remover" (row=3, column=4)
        self.boton_guardar = tk.Button(
            parent,
            text="Guardar datos",
            **estilo_boton,
            command=getattr(app, "guardar_semana", lambda: None)
        )
        self.boton_guardar.grid(row=3, column=3, padx=(10, 5), pady=(2, 5), sticky="ew")
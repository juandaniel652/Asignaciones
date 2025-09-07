import tkinter as tk

class BotonAsignacion:
    def __init__(self, parent, app, columna, tipo):
        """
        parent: widget padre
        app: instancia de Aplicacion
        columna: columna donde ubicar los botones
        tipo: 'acomodadores' o 'vigilancia'
        """
        self.parent = parent
        self.app = app
        self.columna = columna
        self.tipo = tipo

        # Definir información de los botones
        botones_info = [
            ("Remover", f"remover_{tipo}"),
            ("Seleccion aleatoria", f"aleatorio_{tipo}"),
            ("Reiniciar", f"reiniciar_{tipo}"),
        ]

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

        self.botones = []
        for idx, (texto, metodo) in enumerate(botones_info, start=2):
            boton = tk.Button(
                parent,
                text=texto,
                command=getattr(app, metodo, lambda: None),
                **estilo_boton
            )
            boton.grid(row=idx, column=columna, sticky="ew", padx=10, pady=(0, 5))
            self.botones.append(boton)

        # Para acceso directo si se requiere
        self.boton_remover = self.botones[0]
        self.boton_aleatorio = self.botones[1]
        self.boton_reiniciar = self.botones[2]
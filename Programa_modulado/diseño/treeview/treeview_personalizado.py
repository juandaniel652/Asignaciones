import tkinter as tk
from tkinter import ttk

class TreeviewPersonalizado:
    def __init__(self, parent):
        columnas = (
            "Semanas",
            "Acomodadores 1° hora",
            "Acomodadores 2° hora",
            "Acomodador final",
            "Vigilancia 1° hora",
            "Vigilancia 2° hora",
            "Dias de reunión"
        )

        self.treeview = ttk.Treeview(
            parent,
            columns=columnas,
            show='headings',
            selectmode='browse',
            height=6
        )
        # No se implementa editar_celdas aquí
        for col in columnas:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="center", width=120, stretch=True)

        style = ttk.Style(parent)
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="#E0E0E0",
            rowheight=24,
            fieldbackground="#2b2b2b",
            font=("Segoe UI", 10)
        )
        style.configure(
            "Treeview.Heading",
            background="#333333",
            foreground="#E0E0E0",
            font=("Segoe UI", 10, "bold")
        )
        style.map(
            "Treeview",
            background=[("selected", "#1976D2")],
            foreground=[("selected", "white")]
        )
        self.treeview.grid(row=5, column=0, columnspan=5, padx=10, pady=(10, 0), sticky="nsew")
        parent.rowconfigure(5, weight=1)
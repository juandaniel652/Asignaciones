import tkinter as tk
from tkinter import ttk

class ModoTema:
    """
    Clase para manejar el cambio entre modo claro y modo oscuro.
    Se encarga de cambiar los colores de fondo y texto de los widgets principales.
    """
    def __init__(self, app):
        self.app = app
        # Referencias a los botones para cambiar su texto si es necesario
        self.boton_oscuro = app.botones_generales.__dict__.get('boton_oscuro', None)
        self.boton_claro = app.botones_generales.__dict__.get('boton_claro', None)
        # Asignar comandos a los botones
        for child in app.pagina_1.winfo_children():
            if isinstance(child, tk.Button):
                if child.cget("text") == "Modo Oscuro":
                    child.config(command=self.modo_oscuro)
                elif child.cget("text") == "Modo Claro":
                    child.config(command=self.modo_claro)
        for child in app.pagina_2.winfo_children():
            if isinstance(child, tk.Button):
                if child.cget("text") == "Modo Oscuro":
                    child.config(command=self.modo_oscuro)
                elif child.cget("text") == "Modo Claro":
                    child.config(command=self.modo_claro)

    def modo_oscuro(self):
        self._aplicar_tema(
            bg="#1E1E1E",
            fg="#E0E0E0",
            listbox_bg="#424242",
            listbox_fg="#E0E0E0",
            entry_bg="#424242",
            entry_fg="#E0E0E0",
            button_bg="#2196F3",
            button_fg="#FFFFFF",
            tree_bg="#2b2b2b",
            tree_fg="#E0E0E0",
            heading_bg="#333333",
            heading_fg="#E0E0E0"
        )

    def modo_claro(self):
        self._aplicar_tema(
            bg="#F5F5F5",
            fg="#222222",
            listbox_bg="#FFFFFF",
            listbox_fg="#222222",
            entry_bg="#FFFFFF",
            entry_fg="#222222",
            button_bg="#1976D2",
            button_fg="#FFFFFF",
            tree_bg="#FFFFFF",
            tree_fg="#222222",
            heading_bg="#E3E3E3",
            heading_fg="#222222"
        )

    def _aplicar_tema(self, bg, fg, listbox_bg, listbox_fg, entry_bg, entry_fg, button_bg, button_fg, tree_bg, tree_fg, heading_bg, heading_fg):
        # Fondo principal
        self.app.pagina_1.config(bg=bg)
        self.app.ventana.config(bg=bg)
        self.app.pagina_2.config(bg=bg)
        # Títulos
        for label in self.app.titulos.titulos_labels.values():
            label.config(bg=bg, fg=fg)
        # Listboxes
        self.app.listboxes.listbox_acomodadores.config(bg=listbox_bg, fg=listbox_fg)
        self.app.listboxes.listbox_vigilancia.config(bg=listbox_bg, fg=listbox_fg)
        self.app.listboxes.listbox_de_fechas.config(bg=listbox_bg, fg=listbox_fg)
        # Caja de fecha (Text)
        self.app.caja_fecha.text_fecha.config(bg=entry_bg, fg=entry_fg)
        # Reloj
        self.app.reloj.label.config(bg=bg, fg=fg)
        # Botones de asignación y generales en ambas páginas
        for pagina in [self.app.pagina_1, self.app.pagina_2]:
            for child in pagina.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(bg=button_bg, fg=button_fg, activebackground=button_bg, activeforeground=button_fg)
        # Treeview
        style = ttk.Style(self.app.pagina_1)
        style.configure("Treeview", background=tree_bg, foreground=tree_fg, fieldbackground=tree_bg)
        style.configure("Treeview.Heading", background=heading_bg, foreground=heading_fg)

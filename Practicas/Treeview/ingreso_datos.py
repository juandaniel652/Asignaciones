import tkinter as tk
from tkinter import ttk

class Lista : 

    def __init__ (self) : 

        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Ejemplo de Treeview")

        # Crear Treeview
        self.tree = ttk.Treeview(self.root, columns=("col1", "col2", "col3"), show="headings")
        self.tree.pack()

        # Configurar encabezados
        self.tree.heading("col1", text="Columna 1")
        self.tree.heading("col2", text="Columna 2")
        self.tree.heading("col3", text="Columna 3")

        # Insertar algunos datos iniciales
        self.tree.insert("", "end", values=("Valor 1-1", "Valor 1-2", "Valor 1-3"))
        self.tree.insert("", "end", values=("Valor 2-1", "Valor 2-2", "Valor 2-3"))

        # Botón para editar
        btn_editar = tk.Button(self.root, text="Editar", command = self.editar_item)
        btn_editar.pack()


        # Botón para obtener valores
        btn_obtener = tk.Button(self.root, text="Obtener valores", command = self.obtener_valores)
        btn_obtener.pack()

        self.final ()

        self.root.mainloop()


    def editar_item(self) :

        selected_item = self.tree.focus()  # Obtener el ID del elemento seleccionado
        self.tree.item(selected_item, values=("Editado 1", "Editado 2", "Editado 3"))


    def obtener_valores(self) :

        selected_item = self.tree.focus()
        valores = self.tree.item(selected_item, "values")
        print(valores)

    def final (self) : 

        self.editar_item()
        self.obtener_valores()


if __name__ == '__main__' : 

    obejto = Lista()

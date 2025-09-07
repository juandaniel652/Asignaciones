import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Treeview")

# Crear un Treeview
tree = ttk.Treeview(root)

# Definir las columnas
tree['columns'] = ("col1", "col2", "col3")

# Formatear las columnas
tree.column("#0", width=150, minwidth=150)  # Columna de encabezado (invisible, pero necesaria)
tree.column("col1", width=100, minwidth=100)
tree.column("col2", width=100, minwidth=100)
tree.column("col3", width=100, minwidth=100)

# Definir encabezados de columna
tree.heading("#0", text="Elemento")
tree.heading("col1", text="Columna 1")
tree.heading("col2", text="Columna 2")
tree.heading("col3", text="Columna 3")

# Añadir datos
tree.insert("", "end", text="Elemento 1", values=("A", "B", "C"))
tree.insert("", "end", text="Elemento 2", values=("D", "E", "F"))

# Crear un subelemento
parent = tree.insert("", "end", text="Elemento 3", values=("G", "H", "I"))
tree.insert(parent, "end", text="Subelemento 3.1", values=("J", "K", "L"))
tree.insert(parent, "end", text="Subelemento 3.2", values=("M", "N", "O"))

# Mostrar el Treeview en la ventana principal
tree.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()

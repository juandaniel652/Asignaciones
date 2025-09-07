import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo Treeview")

# Crear el Treeview
tree = ttk.Treeview(root, columns=("col1", "col2"), show="headings")
tree.pack()

# Definir encabezados
tree.heading("col1", text="Columna 1")
tree.heading("col2", text="Columna 2")

# Insertar una fila (ítem)
item = tree.insert("", "end", values=("Valor 1", "Valor 2"))

# Cambiar el valor de la primera columna en la fila recién insertada
tree.set(item, "col1", "Nuevo Valor 1")

root.mainloop()

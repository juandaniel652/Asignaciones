import tkinter as tk
from tkinter import ttk

def editar_item():

    selected_item = tree.focus()  # Obtener el ID del elemento seleccionado
    tree.item(selected_item, values=("Editado 1", "Editado 2", "Editado 3"))

def eliminar_item():
    selected_item = tree.focus()  # Obtener el ID del elemento seleccionado
    tree.delete(selected_item)

def obtener_valores():
    selected_item = tree.focus()
    valores = tree.item(selected_item, "values")
    print(valores)


# Crear ventana principal
root = tk.Tk()
root.title("Ejemplo de Treeview")

# Crear Treeview
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")
tree.pack()

# Configurar encabezados
tree.heading("col1", text="Columna 1")
tree.heading("col2", text="Columna 2")
tree.heading("col3", text="Columna 3")

# Insertar algunos datos iniciales
tree.insert("", "end", values=("Valor 1-1", "Valor 1-2", "Valor 1-3"))
tree.insert("", "end", values=("Valor 2-1", "Valor 2-2", "Valor 2-3"))

# Botón para editar
btn_editar = tk.Button(root, text="Editar", command=editar_item)
btn_editar.pack()

# Botón para eliminar
btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_item)
btn_eliminar.pack()

# Botón para obtener valores
btn_obtener = tk.Button(root, text="Obtener valores", command=obtener_valores)
btn_obtener.pack()

root.mainloop()

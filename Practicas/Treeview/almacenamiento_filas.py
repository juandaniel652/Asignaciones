import tkinter as tk
from tkinter import ttk

# Crear la ventana
root = tk.Tk()
root.title("Treeview Ejemplo")

# Crear el Treeview
tree = ttk.Treeview(root, columns=("Nombre", "Edad"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")

# Insertar datos
datos = [("Juan", 25), ("Ana", 30), ("Luis", 22)]
for dato in datos:
    tree.insert("", "end", values=dato)

tree.pack()

# Función para obtener todos los valores
def obtener_todos():
    valores = []
    for item in tree.get_children():
        valores.append(tree.item(item, "values"))
    print(valores)  # Esto imprimirá una lista de tuplas con los valores

# Botón para mostrar valores en la consola
btn = tk.Button(root, text="Obtener valores", command=obtener_todos)
btn.pack()

root.mainloop()

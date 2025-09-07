import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Example")

lista = ["Nombre", "Edad", "Ciudad"]

# Crear un Treeview
tree = ttk.Treeview(root, columns=("Nombre", "Edad", "Ciudad"), show='headings')

for i in range(3) : 
    tree.heading(f"{lista[i]}", text=f"{lista[i]}")
    

# Insertar datos de ejemplo
tree.insert("", "end", values=("Alice", 30, "Madrid"))
tree.insert("", "end", values=("Bob", 24, "Barcelona"))
tree.insert("", "end", values=("Charlie", 29, "Valencia"))

tree.pack()

root.mainloop()

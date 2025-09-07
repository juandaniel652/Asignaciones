import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Editable")

# Crear Treeview
tree = ttk.Treeview(root, columns=("Columna1", "Columna2"), show="headings")
tree.heading("Columna1", text="Columna 1")
tree.heading("Columna2", text="Columna 2")
tree.insert("", "end", values=("Dato 1", "Dato 2"))
tree.pack()

# Variable de estado para alternar entre editable/no editable
editable = tk.BooleanVar(value=True)

# Función para alternar edición
def toggle_edit():
    if editable.get():
        tree.bind("<Double-1>", lambda e: "break")  # Deshabilitar edición
        btn_toggle.config(text="Habilitar Edición")
    else:
        tree.unbind("<Double-1>")  # Habilitar edición
        btn_toggle.config(text="Deshabilitar Edición")
    editable.set(not editable.get())

# Botón para alternar estado
btn_toggle = tk.Button(root, text="Deshabilitar Edición", command=toggle_edit)
btn_toggle.pack()

root.mainloop()

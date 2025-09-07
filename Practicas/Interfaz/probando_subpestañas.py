import tkinter as tk
from tkinter import ttk

def cambiar_pestana(event):
    index = combo.current()
    print(index)
    notebook.select(index)  # Cambia la pestaña activa según el índice

# Crear ventana
root = tk.Tk()
root.title("Notebook con Combobox")
root.geometry("400x300")

# Crear Notebook
notebook = ttk.Notebook(root)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="Pestaña 1")
notebook.add(frame2, text="Pestaña 2")
notebook.pack(expand=True, fill="both")

# Crear Combobox para seleccionar pestañas
combo = ttk.Combobox(root, values=["Pestaña 1", "Pestaña 2"], state="readonly")
combo.pack(pady=10)
combo.current(0)  # Selecciona la primera pestaña por defecto
combo.bind("<<ComboboxSelected>>", cambiar_pestana)

root.mainloop()

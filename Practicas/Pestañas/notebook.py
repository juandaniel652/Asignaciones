import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Notebook con Tkinter")

# Crear el widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Crear los marcos que irán dentro de cada pestaña
tab1 = ttk.Frame(notebook,) #width=400, height=280)
tab2 = ttk.Frame(notebook,) #width=400, height=280)

# Añadir los marcos al Notebook
notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')

# Poner contenido en la primera pestaña
label1 = tk.Label(tab1, text="Contenido de la Pestaña 1", padx=10, pady=10)
label1.pack()

# Poner contenido en la segunda pestaña
label2 = tk.Label(tab2, text="Contenido de la Pestaña 2", padx=10, pady=10)
label2.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()

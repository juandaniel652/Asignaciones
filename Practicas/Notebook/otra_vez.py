import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Pestañas en Tkinter")
root.geometry("400x300")

# Crear un widget Notebook para contener las pestañas
notebook = ttk.Notebook(root)
notebook.grid(column = 0, row = 0)  # Expand permite que el notebook se redimensione con la ventana

# Crear los frames que serán las secciones (pestañas)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Agregar los frames al notebook con un nombre (etiqueta) para cada pestaña
notebook.add(tab1, text="Sección 1")
notebook.add(tab2, text="Sección 2")
notebook.add(tab3, text="Sección 3")

# Agregar contenido a las secciones (pestañas)
label1 = tk.Button(tab1, text="Contenido de la Sección 1", font=("Arial", 16))
label1.pack()

label2 = tk.Label(tab2, text="Contenido de la Sección 2", font=("Arial", 16))
label2.pack()

label3 = tk.Label(tab3, text="Contenido de la Sección 3", font=("Arial", 16))
label3.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()
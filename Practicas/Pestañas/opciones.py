import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para abrir una nueva ventana con opciones adicionales
def abrir_opciones():
    # Crear una nueva ventana
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Opciones Adicionales")
    nueva_ventana.geometry("300x200")
    
    # Agregar widgets a la nueva ventana
    label = tk.Label(nueva_ventana, text="Opciones Adicionales", pady=10)
    label.pack()
    
    # Opciones adicionales
    button1 = tk.Button(nueva_ventana, text="Opción 1", command=lambda: messagebox.showinfo("Opción 1", "Seleccionaste la Opción 1"))
    button1.pack(pady=5)
    
    button2 = tk.Button(nueva_ventana, text="Opción 2", command=lambda: messagebox.showinfo("Opción 2", "Seleccionaste la Opción 2"))
    button2.pack(pady=5)

# Crear la ventana principal
root = tk.Tk()
root.title("Notebook con Opciones Adicionales")

# Crear el widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Crear las pestañas del Notebook
tab1 = ttk.Frame(notebook, width=400, height=280)
tab2 = ttk.Frame(notebook, width=400, height=280)

# Añadir las pestañas al Notebook
notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')

# Poner contenido en la primera pestaña con un botón que abre nuevas opciones
label1 = tk.Label(tab1, text="Pestaña 1: Presiona el botón para más opciones", padx=10, pady=10)
label1.pack()

button = tk.Button(tab1, text="Abrir Opciones", command=abrir_opciones)
button.pack(pady=20)

# Poner contenido en la segunda pestaña
label2 = tk.Label(tab2, text="Contenido de la Pestaña 2", padx=10, pady=10)
label2.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()

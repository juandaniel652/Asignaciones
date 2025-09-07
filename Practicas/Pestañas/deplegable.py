import tkinter as tk
from tkinter import ttk

# Función para cambiar de pestaña cuando se selecciona una opción en el Combobox
def cambiar_pestana(event):
    selected_tab = combobox.current()
    notebook.select(selected_tab)

# Crear la ventana principal
root = tk.Tk()
root.title("Notebook Desplegable con Tkinter")

# Crear el widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=False)

# Crear los marcos que irán dentro de cada pestaña
tab1 = ttk.Frame(notebook, width=400, height=280)
tab2 = ttk.Frame(notebook, width=400, height=280)
tab3 = ttk.Frame(notebook, width=400, height=280)

# Añadir los marcos al Notebook
notebook.add(tab1, text='Fecha')
notebook.add(tab2, text='Acomodadores')
notebook.add(tab3, text='Vigilancia')

# Poner contenido en las pestañas
label1 = tk.Label(tab1, text="Contenido de la Pestaña 1", padx=10, pady=10)
label1.pack()

label2 = tk.Label(tab2, text="Contenido de la Pestaña 2", padx=10, pady=10)
label2.pack()

label3 = tk.Label(tab3, text="Contenido de la Pestaña 3", padx=10, pady=10)
label3.pack()

# Crear un Combobox para seleccionar las pestañas
combobox = ttk.Combobox(root, values=["Pestaña 1", "Pestaña 2", "Pestaña 3"])
combobox.pack(pady=10)
combobox.current(0)  # Selecciona la primera opción por defecto

# Vincular el evento de selección del Combobox con la función de cambio de pestaña
combobox.bind("<<ComboboxSelected>>", cambiar_pestana)

# Iniciar el bucle principal de la ventana
root.mainloop()

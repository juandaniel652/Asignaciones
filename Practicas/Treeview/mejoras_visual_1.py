import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.geometry("600x400")

# Configurar el grid de la ventana principal
root.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
root.grid_columnconfigure(0, weight=1)  # Permitir que la columna 0 se expanda

# Crear el Treeview
tree = ttk.Treeview(root)

# Crear una barra de desplazamiento vertical
scrollbar_y = tk.Scrollbar(root, orient="vertical", command=tree.yview)

# Crear una barra de desplazamiento horizontal
scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=tree.xview)

# Configurar el Treeview para que use las barras de desplazamiento
tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# Ubicar el Treeview en el grid
tree.grid(row=0, column=0, sticky="nsew")

# Ubicar la barra de desplazamiento vertical en el grid
scrollbar_y.grid(row=0, column=1, sticky="ns")

# Ubicar la barra de desplazamiento horizontal en el grid
scrollbar_x.grid(row=1, column=0, sticky="ew")

# Agregar muchas columnas al Treeview para forzar el uso de la barra horizontal
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10")

# Configurar el ancho de las columnas
for col in tree["columns"]:
    tree.column(col, width=150)  # Asignar un ancho que exceda la ventana
    tree.heading(col, text=f"Encabezado {col}")

# Insertar datos de ejemplo
for i in range(50):
    tree.insert("", "end", text=f"Fila {i}", values=(f"Dato {i}-1", f"Dato {i}-2", f"Dato {i}-3", f"Dato {i}-4",
                                                     f"Dato {i}-5", f"Dato {i}-6", f"Dato {i}-7", f"Dato {i}-8",
                                                     f"Dato {i}-9", f"Dato {i}-10"))

# Iniciar el loop principal
root.mainloop()

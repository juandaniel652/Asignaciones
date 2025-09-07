import tkinter as tk
from tkinter import ttk

# Función para abrir el listbox cuando se hace doble clic
def edit_cell(event):
    for item in tree.selection():
        # Obtener la posición del elemento seleccionado
        item_id = item
        col_id = 1  # Columna a editar
        
        # Crear y mostrar un listbox para seleccionar múltiples elementos
        listbox_window = tk.Toplevel(root)
        listbox_window.title("Seleccione dos elementos")

        listbox = tk.Listbox(listbox_window, selectmode="multiple")
        listbox.pack()
        
        # Agregar elementos a la lista
        options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
        for option in options:
            listbox.insert(tk.END, option)

        # Botón para confirmar la selección
        def select_items():
            selected = [listbox.get(i) for i in listbox.curselection()]
            if len(selected) == 2 :  # Solo permitir un máximo de 2 selecciones
                tree.set(item_id, col_id, " / ".join(selected))
                listbox_window.destroy()
            else:
                print("Selecciona solo 2 elementos como máximo.")
        
        tk.Button(listbox_window, text="Confirmar", command=select_items).pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Treeview con Listbox de selección múltiple")

# Crear el Treeview
tree = ttk.Treeview(root, columns=("col1", "col2"))
tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Seleccionados")

tree.insert("", "end", text="1", values=("Item 1", ""))
tree.insert("", "end", text="2", values=("Item 2", ""))

tree.pack()

# Asociar el doble clic para editar la celda
tree.bind("<Double-1>", edit_cell)

root.mainloop()

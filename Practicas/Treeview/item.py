#import tkinter as tk
#from tkinter import ttk
#
#root = tk.Tk()
#
## Creación del Treeview
#tree = ttk.Treeview(root, columns=("col1", "col2"))
#tree.heading("#0", text="Elemento")
#tree.heading("col1", text="Columna 1")
#tree.heading("col2", text="Columna 2")
#
## Insertar un ítem
#item_id = tree.insert("", "end", text="Elemento 1", values=("Dato 1", "Dato 2"))
#
## Obtener información del ítem
#info = tree.item(item_id)
#print("Información del ítem antes de modificar:", info)
#
## Modificar el ítem
#tree.item(item_id, text="Elemento Modificado", values=("Juanito", "Nuevo Dato 2"))
#
## Mostrar el Treeview
#tree.pack()
#
#root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ejemplo de Treeview con Items")

# Crear el Treeview
tree = ttk.Treeview(root, columns=("col1", "col2"), show='headings')
tree.heading("col1", text="Columna 1")
tree.heading("col2", text="Columna 2")
tree.pack()

# Insertar items
tree.insert(parent='', index='end', iid='1', text='', values=("Item 1", "Valor A"))
tree.insert(parent='', index='end', iid='2', text='', values=("Item 2", "Valor B"))

# Modificar un item
tree.item('2', values=("Item Modificado 1", "Valor Modificado A"))

# Obtener los valores de un item
item = tree.item('2')
print("Valores del item 2:", item['values'])

# Eliminar un item
tree.delete('1')

root.mainloop()


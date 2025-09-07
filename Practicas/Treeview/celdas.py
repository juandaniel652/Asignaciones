import tkinter as tk
from tkinter import ttk, messagebox

# Función para iniciar la edición de una celda
def on_double_click(event):
    item_id = treeview.identify_row(event.y)  # Obtiene el ID del item
    column = treeview.identify_column(event.x)  # Obtiene la columna
    
    if item_id and column:
        col_index = int(column.replace('#', '')) - 1 # Convierte la columna al índice correcto
        entry_editing(item_id, col_index)
        print(col_index)


# Función para iniciar la edición
def entry_editing(item_id, col_index):
    x, y, width, height = treeview.bbox(item_id, col_index)  # Obtiene la posición de la celda
    text = treeview.item(item_id, 'values')[col_index]  # Obtiene el valor actual de la celda
    
    # Crea un Entry para la edición
    entry = tk.Entry(root, width=width)
    entry.place(x=x + treeview.winfo_x(), y=y + treeview.winfo_y(), width=width, height=height)
    entry.insert(0, text)  # Inserta el texto actual en el Entry
    entry.focus()

    # Función para manejar cuando se presiona Enter en el Entry
    def on_enter(event):

        new_value = entry.get()
        for i in lista :
            if new_value == i : 
                current_values = list(treeview.item(item_id, 'values'))
                current_values[col_index] = new_value  # Actualiza el valor en la lista
                treeview.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                entry.destroy()  # Elimina el Entry

    entry.bind('<Return>', on_enter)
    entry.bind('<FocusOut>', lambda event: entry.destroy())  # Elimina el Entry si se pierde el foco

# Configuración básica de Tkinter
root = tk.Tk()
root.title("Treeview Editar Celdas")

# Configuración del Treeview
treeview = ttk.Treeview(root, columns=("A", "B", "C"), show='headings')
treeview.pack(expand=True, fill='both')

# Configura los encabezados de columna
for col in ("A", "B", "C"):
    treeview.heading(col, text=col)

# Inserta datos de ejemplo
treeview.insert("", "end", values=("1", "2", "3"))
treeview.insert("", "end", values=("4", "5", "6"))

# Vincula el doble clic para editar celdas
treeview.bind("<Double-1>", on_double_click)

lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter ","Arguello Jorge", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]

root.mainloop()

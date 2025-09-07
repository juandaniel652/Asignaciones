import tkinter as tk
from tkinter import ttk, messagebox

# Función para iniciar la edición de una celda
def on_double_click(event):
    item_id = tree.identify_row(event.y)  # Obtiene el ID del item
    column = tree.identify_column(event.x)  # Obtiene la columna
    
    if item_id and column:
        col_index = int(column.replace('#', ''))  - 1# Convierte la columna al índice correcto
        entry_editing(item_id, col_index)
        print(col_index)


# Función para iniciar la edición
def entry_editing(item_id, col_index):
    x, y, width, height = tree.bbox(item_id, col_index)  # Obtiene la posición de la celda
    
    indice = 0

    # Crea un Entry para la edición
    listbox = tk.Listbox(root, width=width)
    listbox.place(x=x + tree.winfo_x(), y=y + tree.winfo_y(), width=width, height=height)

    for w in lista: 
        listbox.insert(indice, w)  # Inserta el texto actual en el Entry
    listbox.focus()

    # Función para manejar cuando se presiona Enter en el Entry
    def on_enter(event):
        seleccion = listbox.curselection()
        new_value = listbox.get(seleccion[indice])
        for i in lista :
            if new_value == i : 
                current_values = list(tree.item(item_id, 'values'))
                current_values[col_index] = new_value  # Actualiza el valor en la lista
                tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                listbox.destroy()  # Elimina el Entry

    listbox.bind('<Return>', on_enter)
    listbox.bind('<FocusOut>', lambda event: listbox.destroy())  # Elimina el Entry si se pierde el foco

# Configuración básica de Tkinter
root = tk.Tk()
root.title("Treeview Editar Celdas")


 # Crear un Treeview

tree = ttk.Treeview(root, columns=("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora","Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia despues de la reunión", "Dias de reunión"), show='headings')
tree.pack(expand=True, fill='both')

# Definir encabezados de columna
lista_heading = ["Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora","Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia despues de la reunión", "Dias de reunión"]
    

for col in ("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora","Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia despues de la reunión", "Dias de reunión"):
    tree.heading(col, text=col)

tree.column("Semanas", width=220, minwidth=220)
tree.column("Acomodadores 1° hora", width=220, minwidth=220)
tree.column("Acomodadores 2° hora", width=175, minwidth=175)
tree.column("Vigilancia 1° hora", width=175, minwidth=175)
tree.column("Vigilancia 2° hora", width=180, minwidth=180)
tree.column("Vigilancia despues de la reunión", width=175, minwidth=175)
tree.column("Dias de reunión", width=175, minwidth=175)
            
tree.grid(column = 0 , row = 5, columnspan = 5)

tree.insert("", "end", values=("1", "2", "3", "4", "5", "6"))
tree.insert("", "end", values=("7", "8", "9", "10", "11", "12"))

tree.bind("<Double-1>", on_double_click)


lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter ","Arguello Jorge", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]

root.mainloop()

import tkinter as tk
from tkinter import ttk

def on_double_click(event):
    # Detectar el índice del item seleccionado (fila)
    row_id = treeview.identify_row(event.y)
    column_id = treeview.identify_column(event.x)

    # Si no se ha seleccionado una fila, no hacer nada
    if not row_id or column_id == "#0":
        return

    # Obtener el índice de la fila
    row = treeview.index(row_id)
    
    # Posición de la columna
    col = int(column_id.replace("#", "")) - 1  # restamos 1 porque las columnas empiezan en 1

    # Si estamos en una columna editable (por ejemplo, la columna 2), se despliega el Listbox
    if col == 0:  # Modificar esta condición si quieres aplicar a otra columna
        # Obtener las coordenadas de la celda
        bbox = treeview.bbox(row_id, column_id)
        
        # Crear el Listbox con opciones y situarlo en la celda
        listbox_var.set('')
        listbox.place(x=bbox[0], y=bbox[1], width=bbox[2], height=bbox[3])

        # Asociar el valor seleccionado del Listbox con la celda
        def on_listbox_select(event):
            selected_value = listbox_var.get()
            treeview.set(row_id, column=column_id, value=selected_value)
            listbox.place_forget()  # Ocultar el Listbox

        listbox.bind("<<ListboxSelect>>", on_listbox_select)

# Crear la ventana principal
root = tk.Tk()
root.title("Treeview con Listbox Editable")
root.geometry("400x200")

# Crear el Treeview con 3 columnas
treeview = ttk.Treeview(root, columns=("Columna 1", "Columna 2", "Columna 3"), show="headings")
treeview.pack(fill=tk.BOTH, expand=True)

# Configurar encabezados
treeview.heading("Columna 1", text="Columna 1")
treeview.heading("Columna 2", text="Columna 2")
treeview.heading("Columna 3", text="Columna 3")

# Agregar algunos datos
treeview.insert("", "end", values=("Dato 1", "Dato 2", "Dato 3"))
treeview.insert("", "end", values=("Dato 4", "Dato 5", "Dato 6"))
treeview.insert("", "end", values=("Dato 7", "Dato 8", "Dato 9"))

# Crear el Listbox (opciones de edición)
listbox_var = tk.StringVar()
listbox = ttk.Combobox(root, textvariable=listbox_var, values=["Opción A", "Opción B", "Opción C"])
listbox.place_forget()  # Ocultar el Listbox hasta que se necesite

# Asociar el evento de doble clic para la edición
treeview.bind("<Double-1>", on_double_click)

root.mainloop()

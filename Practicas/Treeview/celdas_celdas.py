import tkinter as tk
from tkinter import ttk

def on_double_click(event):
    # Obtener el item seleccionado
    selected_item = treeview.selection()
    if selected_item:
        # Obtener el valor de la primera columna (o la columna que quieras modificar)
        item = treeview.item(selected_item)
        current_value = item['values'][0]

        # Crear ventana emergente
        edit_window = tk.Toplevel(root)
        edit_window.title("Editar valor")

        # Etiqueta y campo de entrada
        tk.Label(edit_window, text="Nuevo valor:").pack(pady=10)
        new_value_entry = tk.Entry(edit_window)
        new_value_entry.pack(pady=5)
        new_value_entry.insert(0, current_value)  # Mostrar valor actual en el Entry

        def save_value():
            # Obtener el nuevo valor del Entry
            new_value = new_value_entry.get()

            # Actualizar el valor en el Treeview
            treeview.item(selected_item, values=(new_value,))

            # Cerrar la ventana emergente
            edit_window.destroy()

        # Botón para guardar el nuevo valor
        save_button = tk.Button(edit_window, text="Guardar", command=save_value)
        save_button.pack(pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Treeview con edición")

# Crear Treeview
treeview = ttk.Treeview(root, columns=("Valor",), show="headings")
treeview.heading("Valor", text="Valor")
treeview.pack()

# Insertar datos en el Treeview
treeview.insert("", "end", values=("Item 1",))
treeview.insert("", "end", values=("Item 2",))
treeview.insert("", "end", values=("Item 3",))

# Evento para doble clic
treeview.bind("<Double-1>", on_double_click)

root.mainloop()

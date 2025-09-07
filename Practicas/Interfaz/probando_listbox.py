import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Listbox Example")

# Crear la Listbox
listbox = tk.Listbox(root)
listbox.pack()

# Agregar algunos elementos a la Listbox
for item in ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]:
    listbox.insert(tk.END, item)

# Función para remover el elemento seleccionado
def remover_elemento():
    seleccion = listbox.curselection()
    if seleccion:
        listbox.delete(seleccion[0])
        print(seleccion)

# Función para remover todos los elementos
def remover_todos():
    listbox.delete(0, tk.END)


def reiniciar () : 
    remover_todos()
    for item in ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]:
        listbox.insert(tk.END, item)


# Botón para remover el elemento seleccionado
btn_remover = tk.Button(root, text="Remover Seleccionado", command=remover_elemento)
btn_remover.pack()

# Botón para remover todos los elementos
btn_remover_todos = tk.Button(root, text="Remover Todos", command=remover_todos)
btn_remover_todos.pack()

btn_reiniciar = tk.Button(root, text="Reinniciar", command=reiniciar)
btn_reiniciar.pack()

# Ejecutar la aplicación
root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox

def verificar_estado():
    opcion = combo_var.get()
    if check_var.get():  # Si el checkbox está marcado
        resultado_label.config(text=f"Seleccionaste '{opcion}' y marcaste el checkbox.")
        messagebox.showinfo("Información", "¿Desea convertir a archvio externo esta opción?")

    else:
        resultado_label.config(text="")

# Crear ventana principal
root = tk.Tk()
root.title("Combobox y Checkbutton")

# Variable para el Combobox
combo_var = tk.StringVar()
opciones = ["Opción 1", "Opción 2", "Opción 3"]
combobox = ttk.Combobox(root, textvariable = combo_var, values=opciones, state="readonly")
combobox.grid(row = 0, column = 1, padx = 10, pady = 10)

# Variable para el Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Activar", variable=check_var, command=verificar_estado)
checkbutton.grid(row = 0, column = 0, padx=10, pady=10)

# Label para mostrar el resultado
resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.grid(row=1, column=0, columnspan=2, pady=10)

# Iniciar la interfaz
root.mainloop()
import tkinter as tk
from tkinter import PanedWindow

# Crear la ventana principal
root = tk.Tk()
root.title("Dividir ventana con PanedWindow")

# Crear un PanedWindow horizontal
paned_window = PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill="both", expand=True)

# Crear dos frames dentro del PanedWindow
frame_izquierda = tk.Frame(paned_window, bg="lightblue", width=200)
frame_derecha = tk.Frame(paned_window, bg="lightgreen", width=200)

# Añadir los frames al PanedWindow
paned_window.add(frame_izquierda)
paned_window.add(frame_derecha)

# Añadir algunos widgets dentro de los frames
label_izquierda = tk.Label(frame_izquierda, text="Sección Izquierda", bg="lightblue")
label_izquierda.pack(pady=20)

label_derecha = tk.Label(frame_derecha, text="Sección Derecha", bg="lightgreen")
label_derecha.pack(pady=50)

# Iniciar el loop principal
root.mainloop()
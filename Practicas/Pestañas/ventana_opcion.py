import tkinter as tk
from tkinter import messagebox

def preguntar_decision():
    respuesta = messagebox.askquestion("Decisión", "¿Estás seguro de continuar?")
    
    if respuesta == 'yes':
        print("El usuario eligió Sí")
    else:
        print("El usuario eligió No")

root = tk.Tk()

# Botón que abrirá el cuadro de diálogo
boton = tk.Button(root, text="Seleccionar opción", command=preguntar_decision)
boton.pack(pady=20)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Función que abre una ventana personalizada con opciones
def ventana_opciones():
    # Crear ventana emergente personalizada
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Escoge una opción")
    ventana_emergente.geometry("300x250")

    # Etiqueta con una pregunta
    etiqueta = tk.Label(ventana_emergente, text="¿Cuál es tu lenguaje favorito?")
    etiqueta.pack(pady=10)

    # Funciones para cada opción
    def seleccion_python():
        messagebox.showinfo("Respuesta", "¡Has elegido Python!")
        ventana_emergente.destroy()  # Cerrar ventana emergente

    def seleccion_java():
        messagebox.showinfo("Respuesta", "Has elegido Java.")
        ventana_emergente.destroy()

    def seleccion_javascript():
        messagebox.showinfo("Respuesta", "Has elegido JavaScript.")
        ventana_emergente.destroy()

    # Botones con opciones personalizadas
    boton_python = tk.Button(ventana_emergente, text="Python", command=seleccion_python)
    boton_python.pack(side=tk.LEFT, padx=10)

    boton_java = tk.Button(ventana_emergente, text="Java", command=seleccion_java)
    boton_java.pack(side=tk.LEFT, padx=10)

    boton_javascript = tk.Button(ventana_emergente, text="JavaScript", command=seleccion_javascript)
    boton_javascript.pack(side=tk.LEFT, padx=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Interactiva con Opciones Personalizadas")
ventana.geometry("300x200")

# Botón para abrir la ventana emergente con opciones
boton = tk.Button(ventana, text="Mostrar Opciones", command=ventana_opciones)
boton.pack(pady=20)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()

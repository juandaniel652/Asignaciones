import tkinter as tk

# Función para mover la ventana
def mover_ventana(evento):
    x = evento.x_root - ventana._offset_x
    y = evento.y_root - ventana._offset_y
    ventana.geometry(f"+{x}+{y}")

def capturar_offset(evento):
    ventana._offset_x = evento.x
    ventana._offset_y = evento.y

ventana = tk.Tk()
ventana.title("Ventana con Borde Personalizado")
ventana.geometry("400x300")
ventana.overrideredirect(True)  # Eliminar el borde predeterminado

# Crear un Frame que actúe como el borde
borde = tk.Frame(ventana, bg="blue", bd=5)
borde.pack(fill=tk.BOTH, expand=True)

# Crear otro Frame dentro del borde para el contenido real
contenido = tk.Frame(borde, bg="white")
contenido.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Etiqueta de ejemplo
etiqueta = tk.Label(contenido, text="Ventana con borde azul", bg="white")
etiqueta.pack(pady=20)

# Botón para cerrar la ventana
cerrar_btn = tk.Button(contenido, text="Cerrar", command=ventana.destroy)
cerrar_btn.pack(pady=10)

# Hacer que la ventana se pueda mover
borde.bind("<Button-1>", capturar_offset)
borde.bind("<B1-Motion>", mover_ventana)

ventana.mainloop()

import tkinter as tk

def abrir_ventana():
    global ventana_top
    ventana_top = tk.Toplevel(root)
    ventana_top.title("Ventana secundaria")
    ventana_top.geometry("400x300")  # Tamaño inicial de la ventana
    
    # Deshabilitar el redimensionamiento
    ventana_top.resizable(False, False)  # No se puede redimensionar en ningún eje
    
    # Establecer el tamaño máximo al mismo que el tamaño inicial (evitar maximizar)
    ventana_top.wm_maxsize(400, 300)  # El tamaño máximo es igual al inicial
    ventana_top.wm_attributes("-toolwindow", True)

root = tk.Tk()
root.title("Ventana principal")

boton_abrir = tk.Button(root, text="Abrir ventana", command=abrir_ventana)
boton_abrir.pack(pady=20)

root.mainloop()



import tkinter as tk

# Crear una ventana raíz
root = tk.Tk()
root.title("Ejemplo de PhotoImage")

# Crear un objeto PhotoImage con una imagen
imagen = tk.PhotoImage(file="cuaderno.ico")  # Reemplaza con la ruta de tu imagen

# Crear un widget Label para mostrar la imagen
root.iconphoto(False, imagen)

# Iniciar el loop principal de tkinter
root.mainloop()

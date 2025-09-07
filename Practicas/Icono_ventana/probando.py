import tkinter as tk
from PIL import Image, ImageTk

# Crear una ventana raíz
root = tk.Tk()
root.title("Ejemplo con Pillow")

# Cargar la imagen usando PIL
imagen_pil = Image.open("cuaderno.ico")  # Cambia la ruta por la de tu imagen

# Convertir la imagen de PIL a un formato que tkinter entienda (ImageTk)
imagen_tk = ImageTk.PhotoImage(imagen_pil)

# Crear un widget Label para mostrar la imagen
root.iconphoto(False, imagen_tk)

# Iniciar el loop principal de tkinter
root.mainloop()

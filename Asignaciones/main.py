import tkinter as tk
from gui.main_window import MainWindow
import os

# Ruta al ícono
icon_path = os.path.join("assets", "cuaderno.ico")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Asignaciones")
    root.geometry("1350x750")
    
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    app = MainWindow(root)
    root.mainloop()

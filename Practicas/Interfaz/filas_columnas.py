import tkinter as tk 
from tkinter import ttk

class Ubicacion: 

    def __init__(self) : 
        self.root = tk.Tk()
        for columna in range (0, 3) : 
            for fila in range (0, 3) : 
                etiqueta = tk.Label(self.root, text  = "Hola")
                etiqueta.grid(column = columna, row = fila)

        self.root.mainloop()

    # for i in range (1, 6):
       #     for x in range (1, 6) : 
       #         print(i)
       #         etiqueta = tk.Label(self.root, text = i)
       #         etiqueta_x = tk.Label(self.root, text = f"{x + 5}")
       #         etiqueta.grid(column = 0, row = i)
       #         etiqueta_x.grid(column = 1, row = x)

if __name__ == '__main__'  :
    objeto = Ubicacion()
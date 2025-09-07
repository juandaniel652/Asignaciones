import tkinter as tk
import datetime

class Etiqueta : 

    def __init__ (self) : 

        self.root = tk.Tk()
        self.ventana()
        self.root.mainloop()

    
    def ventana (self) : 
        
        fecha = datetime.date(2024, 7, 11)
        fecha_muestra = fecha.strftime("%d - %m - %Y")
        etiqueta = tk.Label(self.root, text = fecha_muestra)
        etiqueta.grid(column = 0, row = 0)

    
if __name__ == '__main__' : 
    objeto = Etiqueta()

    
import tkinter as tk
from tkinter import ttk

class Boton: 
            
    def __init__ (self) :  

        self.root = tk.Tk()

        self.lista = ["Remover", "Seleccion aleatoria", "Salir"]

        for i in range (3) : 
        
            self.botones = ttk.Button(self.root, text = self.lista[i], command = self.funcion)

            self.botones.grid(column = i, row = 0, padx = 5, pady = 5)


        self.root.mainloop()

    
    def funcion (self)  :
        pass

    
if __name__ == '__main__': 

    objeto = Boton()
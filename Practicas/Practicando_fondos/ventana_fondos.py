import tkinter as tk
from tkinter import ttk, font

class Fondo : 

    def __init__ (self) :

        self.ventana = tk.Tk()   
        self.diseño()     
        self.ventana.mainloop()

    def cambiar_color (self) : 
       
        boton = ttk.Button(self.ventana, text = "Fondo", command = self.cambio)
        boton.pack()

    def determinado (self) : 
        boton = ttk.Button(self.ventana, text = "Defecto", command = self.defecto)
        boton.pack()

#FUNCIONALIDAD

    def cambio (self) : 
 
        contraste = self.ventana.config(background = "black")
       

   
    def defecto (self) : 
        self.ventana.config(background = "gray97")
    
      

    
    def diseño (self) : 
        self.cambiar_color()
        self.determinado()
        
        

if __name__ == '__main__' : 

    objeto = Fondo()

#Asignaciones que imposibiliten la participacion. (Abarca 1ra y 2da hora)
import random
import tkinter as tk 
from tkinter import ttk, END, font

class Vigilancia: 

    def __init__ (self) : 
    
        self.root = tk.Tk()
        self.root.title("Seleccion Vigilancia")

        self.diseño = font.Font(size = 15, family = "Helvética")
        self.diseño_lista = font.Font(size = 10, family = "Italic")
        self.letra = font.Font(family = "Arial", size = 12, slant = "italic")
        
        self.ventana()
        self.root.mainloop()


    def muestra_lista (self) : 

        self.lista_vigilancia = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Monica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gomez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Dominguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela", "Altamirano Daiana"]
    
        self.lista_vigilancia.sort()
        
        self.listbox = tk.Listbox(self.root, relief = "raised", font = self.diseño_lista, foreground = "white", background = "black")

        indice = 0

        for i in self.lista_vigilancia : 
            self.listbox.insert(indice, i)
            print(indice)
            indice = indice  + 1
        
        self.listbox.pack()


    def boton_aleatorio (self): 
        aleatorio = random.sample(self.lista_vigilancia, 3)
        print(f"Vigilancia 1° hora: {aleatorio[0]}\nVigilancia 2° hora: {aleatorio[1]}\nVigilancia despues de la reunion: {aleatorio[2]}")
        print("================================")

        self.etiqueta = tk.Label(self.root, text = f"Vigilancia 1° hora: {aleatorio[0]}\n\n"
                                                     f"Vigilancia 2° hora: {aleatorio[1]}\n\n"
                                                     f"Vigilancia despues de la reunion: {aleatorio[2]}\n\n",
                                                     bg = "blue4", relief="groove", border = 5, fg = "white", font = self.letra)
        
        self.etiqueta.pack()


    def boton_remover (self):
        seleccion = self.listbox.curselection()
        indice = 0
        if seleccion : 
            self.listbox.delete(seleccion[indice])
            print(f"\nAntes de DEL {self.lista_vigilancia}\n")
            del self.lista_vigilancia [seleccion[indice]]
            print(f"\nDespues del DEL: {self.lista_vigilancia}\n")


    def ventana (self) : 

        boton_aleatorio = tk.Button(self.root, text = "Seleccion aleatoria", background = "blue", foreground = "white", command = self.boton_aleatorio)
        boton_remover = tk.Button(self.root, text = "Remover", background = "blue", foreground = "white", command = self.boton_remover)
        boton_aleatorio.pack()
        boton_remover.pack()
        self.muestra_lista()



if __name__ == '__main__' : 

    obejto = Vigilancia()
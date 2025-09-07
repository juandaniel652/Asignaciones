import random

class Acomodadores: 

    def __init__(self) : 

        self.lista = ["Aureliano Ortiz", "Martín Altamirano", "Fernando Israelson", "Juan Ontiveros", "Horacio Altamirano", 
         "Walter Valiente", "Gerardo Encina", "Enrique Gracia", "Joel Dominguez", "Armando Ligeron", "Elias Altamirano",
         "Horacio Vallejos"]

        self.final ()


    def muestro_lista (self) : 
        
        indice = 0
        
        print("\n================== \nLista actual:\n")

        for i in self.lista: 
            indice = indice + 1
            print(f"{indice}. {i}")
        print("\n================================")
        

    def seleccion_remover (self) : 

        cantidad = int(input("Seleccione la cantidad de indices a remover: "))

        for i in range (cantidad) : 
            indice = 0
            seleccion = int(input("\nSeleccione el indice a ser removido: "))

            if seleccion > 0 and seleccion != 1: 

                indice = seleccion - 1
                print(f"\nSelecciondo = {indice + 1}. {self.lista[indice]}\n")

                if indice :
                    del self.lista[indice]
                    self.muestro_lista()

            elif seleccion == 1 : 
                print(f"\nSelecciondo = {indice + 1}. {self.lista[indice]}\n")
                del self.lista[0]
                self.muestro_lista()

            else: 
                print("\nEl indice seleccionado debe ser mayor a 0.\n")

        
    def seleccionar_acomodadores (self) : 

            aleatorio = random.sample(self.lista, 4)
            print(f"Acomodadores 1° hora:\n{aleatorio [0]} / {aleatorio [1]}\n\nAcomodadores 2° hora:\n{aleatorio [2]} / {aleatorio[3]}")
            print("================================")

    
    def final (self) : 

        self.muestro_lista()
        self.seleccion_remover()
        self.seleccionar_acomodadores()
    


if __name__ == '__main__' :

    objeto = Acomodadores()
import random
import datetime
from datetime import timedelta

class Acomodadores: 

    def __init__(self) : 

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


    def orden (self)  :

        fecha_actual = datetime.date(2024, 7, 24)
        fecha_final = datetime.date(2024, 12, 25)
        diferencia = fecha_final - fecha_actual
        semanas = diferencia.days / 7
        num = int(semanas) + 1
        self.lista_fecha = []


        for i in range (num) : 
            nueva_fecha = fecha_actual + timedelta(weeks=i)
            i = i + 1
            fecha = nueva_fecha.strftime("%d - %m - %Y")
            self.lista_fecha.append(fecha)

        
        indice = 0
        for x in self.lista_fecha: 
            indice = indice + 1
            print(f"{indice}. {x}")
        print("\n================================")


        seleccion = int(input("\nSeleccione la fecha entresemana: "))

        if seleccion > 0 and seleccion != 1 : 
        
            indice = seleccion - 1
            print(f"\nSelecciondo = {indice + 1}.\n\n{self.lista_fecha[indice]}")
            self.seleccionar_acomodadores()  

            with open ('archivos.txt', 'w') as archivo : 
                    archivo.write(f'{self.lista_fecha[indice]}\n')
                    archivo.write(f'{self.muestra}')

            try:
                with open('Acomodadores.txt', 'r') as archivo:
                    contenido = archivo.read()
                print('Contenido del archivo:')
                print(contenido)
            except FileNotFoundError:
                print('El archivo no existe.')
            
            
        elif seleccion == 1 : 
            indice = seleccion - 1
            print(f"\nSelecciondo = {indice + 1}.\n\n{self.lista_fecha[indice]}")
            self.seleccionar_acomodadores()  

            with open ('archivos.txt', 'w') as archivo : 
                    archivo.write(f'{self.lista_fecha[indice]}\n')
                    archivo.write(f'{self.muestra}')
            try:
                with open('Acomodadores.txt', 'r') as archivo:
                    contenido = archivo.read()
                print('Contenido del archivo:')
                print(contenido)
            except FileNotFoundError:
                print('El archivo no existe.')

        else: 
            print("\nEl indice seleccionado debe ser mayor a 0.\n")
            
        print("================================")


        self.decision ()
        

    def seleccionar_acomodadores (self) : 

            aleatorio = random.sample(self.lista, 4)
            self.muestra = (f"Acomodadores 1° hora:\n{aleatorio [0]} / {aleatorio [1]}\n\nAcomodadores 2° hora:\n{aleatorio [2]} / {aleatorio[3]}")
            print(self.muestra)


    def decision (self) : 

        try: 

            decision = input("¿Desea seguir agregando? [Si / No]: ")
            decision.lower()
            if decision == 'Si' or decision == 'si' : 
                self.final()
            elif decision == 'No' or decision == 'no': 
                print("Programa finalizado.")

        except Exception as e :
            print(f"Error: {e}")

    
    def final (self) : 

        self.lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter ", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]
        
        self.lista.sort()

        self.muestro_lista()
        self.seleccion_remover()
        self.orden()
    

if __name__ == '__main__' :

    objeto = Acomodadores()
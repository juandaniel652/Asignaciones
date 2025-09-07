import random
import datetime
import locale
import tkinter as tk 
from tkinter import ttk, END, font


class Interfaz : 

    def __init__ (self) : 

        self.root = tk.Tk()
        self.root.title("Seleccion Acomodadores")

        self.diseño = font.Font(size = 15, family = "Helvética")
        self.diseño_lista = font.Font(size = 10, family = "Italic")
        self.letra = font.Font(family = "Arial", size = 12, slant = "italic")
        
        self.ventana()
        self.root.mainloop()


    def muestra_lista (self) : 

        self.lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter ","Arguello Jorge", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]
    
        self.lista.sort()
        
        self.listbox = tk.Listbox(self.root, relief = "raised", font = self.diseño_lista, foreground = "white", background = "black")

        indice = 0

        for i in self.lista : 
            self.listbox.insert(indice, i)
            print(indice)
            indice = indice  + 1
        
        self.listbox.grid(row = 1, column = 0)

    
    def botones_diseño (self) :
        boton_remover = tk.Button(self.root, text = "Remover", background = "blue", foreground = "white", command = self.boton_remover)
        boton_aleatorio = tk.Button(self.root, text = "Seleccion aleatoria", background = "blue", foreground = "white", command = self.boton_aleatorio)
        boton_treeview = tk.Button(self.root, text = "Treeview", background = "blue", foreground = "white", command = self.recuadro)
        boton_reiniciar = tk.Button(self.root, text = "Reiniciar", background = "blue", foreground = "white", command = self.reiniciar)
        boton_salir = tk.Button(self.root, text = "Salir", background = "blue", foreground = "white", command = self.salir)
        boton_remover.grid(column = 0, row = 2)
        boton_aleatorio.grid(column = 0, row = 3)
        boton_treeview.grid(column = 0, row = 4)
        boton_reiniciar.grid(column = 0, row =  5)
        boton_salir.grid(column = 0, row = 6)
        
         
    def boton_remover (self):
        seleccion = self.listbox.curselection()
        indice = 0
        if seleccion : 
            self.listbox.delete(seleccion[indice])
            print(f"\nAntes de DEL {self.lista}\n")
            del self.lista [seleccion[indice]]
            print(f"\nDespues del DEL: {self.lista}\n")
    
        
    def boton_aleatorio (self): 
        self.aleatorio = random.sample(self.lista, 4)
        print(f"Acomodadores 1° hora:\n{self.aleatorio [0]} / {self.aleatorio [1]}\n\nAcomodadores 2° hora:\n{self.aleatorio [2]} / {self.aleatorio[3]}")
        print("================================")

        self.etiqueta = tk.Label(self.root, text = f"Acomodadores 1° hora: {self.aleatorio[0]} / {self.aleatorio[1]} \n\n"
                                                     f"Acomodadores 2° hora: {self.aleatorio[2]} / {self.aleatorio[3]} \n\n",
                                                     bg = "blue4", relief="groove", border = 5, fg = "white", font = self.letra)
        
        self.etiqueta.grid(column = 1, row = 1)

    
    def recuadro (self) :
        
        # Crear un Treeview
        tree = ttk.Treeview(self.root)

        # Definir las columnas
        tree['columns'] = ("col1", "col2")

        # Formatear las columnas
        tree.column("#0", width=200, minwidth=200)  # Columna de encabezado (invisible, pero necesaria)
        tree.column("col1", width=220, minwidth=220)
        tree.column("col2", width=220, minwidth=220)

        # Definir encabezados de columna
        tree.heading("#0", text="Fechas")
        tree.heading("col1", text="Acomodadores 1° hora")
        tree.heading("col2", text="Acomodadores 2° hora")


        #Ubica en español el nombre del mes
        locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
        lista = []

        #Creo una variabe llamada 'hoy' la cual guardara desde donde empiezo a contar
        hoy = datetime.date(2024, 8, 5)

        #Aca marco la fecha del domingo como ultima semana por ende lee hasta el lunes 30 - 12- 2024
        fecha_final = datetime.date(2025, 1, 5)
        diferencia = fecha_final - hoy
        semanas = diferencia.days / 7
        num = int(semanas) + 1

        for i in range (num) : 

            #Trabajo con los dias en el bucle
            semana_nueva = hoy + datetime.timedelta(weeks = i)
            semana_completa = semana_nueva + datetime.timedelta(days = 6)

            #Lunes y Domingo
            monday = semana_nueva.strftime("%d")
            sunday = semana_completa.strftime("%d")

            #Mes y año para modo reunion
            mes_nombre = semana_completa.strftime("%B")
            anio_nombre = semana_completa.strftime("%Y")

            #Muestra y contabiliza
            mostrador = f"{monday} - {sunday} {mes_nombre} {anio_nombre}"

            self.aleatorio = random.sample(self.lista, 4)

            tree.insert("", "end", text=f"{mostrador}", 
                    values= (f"{self.aleatorio[0]} / {self.aleatorio[1]}", f"{self.aleatorio[2]} / {self.aleatorio[3]}",))

        tree.grid(column = 0, row = 7)
        

    def reiniciar (self) :
        self.listbox.delete(0, END)
        self.muestra_lista()


    def salir (self) : 
        self.root.quit()


    def ventana(self) :
        etiqueta = ttk.Label(self.root, text = "Lista", font = self.diseño, background = "lightblue")
        etiqueta.grid(row = 0, column = 0)
        self.muestra_lista()
        self.botones_diseño()
            


if __name__ == '__main__' : 

    objeto = Interfaz()
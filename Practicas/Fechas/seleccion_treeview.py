import tkinter as tk
from tkinter import ttk
import locale
import datetime

class Fecha : 

    def __init__ (self) : 

        self.ventana = tk.Tk()
        self.final ()
        self.ventana.mainloop()


    def operacion (self) : 
      
        #Ubica en español el nombre del mes
        locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
        self.lista = []

        #Creo una variabe llamada 'hoy' la cual guardara desde donde empiezo a contar
        hoy = datetime.date(2025, 8, 12)

        #Aca marco la fecha del domingo como ultima semana por ende lee hasta el lunes 30 - 12- 2024
        fecha_final = datetime.date(2025, 1, 5)
        diferencia = fecha_final - hoy
        semanas = diferencia.days / 7
        num = int(semanas) + 1

        #A partir del comienzo del bucle de los dias lunes, lo llevo a los domingos y asi se ejecuta
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
            mostrador = f"Del {monday} al {sunday} de {mes_nombre} {anio_nombre}"
            self.lista.append(mostrador)
            print(mostrador)
            


    def muestra_interfaz (self) : 

        self.caja = tk.Listbox(self.ventana, height = 25, width = 30)
        
        indice = 0

        for i in self.lista : 
            self.caja.insert(indice, i)
            print(indice)
            indice = indice  + 1
        
        self.caja.pack()


    def botones (self) : 

        mostrar = ttk.Button(self.ventana, text = "Mostrar",  command = self.muestra)
        mostrar.pack()

    
    def muestra (self) : 

        seleccion = self.caja.curselection()
        indice = 0
        for indice in seleccion : 
            if seleccion : 
                self.tree.insert("", "end", text=f"{self.lista[indice]}", 
                    values= (1, 2))


    def treeview (self) : 

        # Crear un Treeview
            self.tree = ttk.Treeview(self.ventana)

            # Definir las columnas
            self.tree['columns'] = ("col1", "col2")

            # Formatear las columnas
            
            self.tree.column("#0", width=200, minwidth=200)  # Columna de encabezado (invisible, pero necesaria)
            
            self.tree.column("col1", width=220, minwidth=220)
            
            self.tree.column("col2", width=220, minwidth=220)

            # Definir encabezados de columna
            self.tree.heading("#0", text="Fechas")

            self.tree.heading("col1", text="Acomodadores 1° hora")

            self.tree.heading("col2", text="Acomodadores 2° hora")

            self.tree.pack()
        
    def final (self)  : 
        
        self.operacion()
        self.muestra_interfaz()
        self.botones()
        self.treeview()

    
if __name__ == '__main__' : 

    objeto = Fecha()
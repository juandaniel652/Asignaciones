import tkinter as tk
from tkinter import ttk
import random
import datetime
import locale

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Treeview")

# Crear un Treeview
tree = ttk.Treeview(root)

# Definir las columnas
tree['columns'] = ("col1", "col2", "col3", "col4", "col5")

# Formatear las columnas
tree.column("#0", width=200, minwidth=200)  # Columna de encabezado (invisible, pero necesaria)
tree.column("col1", width=220, minwidth=220)
tree.column("col2", width=220, minwidth=220)
tree.column("col3", width=220, minwidth=220)
tree.column("col4", width=220, minwidth=220)
tree.column("col5", width=220, minwidth=220)


# Definir encabezados de columna
tree.heading("#0", text="Fechas")
tree.heading("col1", text="Acomodadores 1° hora")
tree.heading("col2", text="Acomodadores 2° hora")
tree.heading("col3", text="Vigilancia 1° hora")
tree.heading("col4", text="Vigilancia 2° hora")
tree.heading("col5", text="Vigilancia despues de la reunión")


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


lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter","Arguello Jorge", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]

lista_vigilancia = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Monica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gomez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Dominguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela", "Altamirano Daiana"]

# Añadir datos

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
    mostrador = f"{monday} - {sunday} {mes_nombre} {anio_nombre}"

    aleatorio = random.sample(lista, 4)
    aleatorio_vigilancia = random.sample(lista_vigilancia, 3)
    tree.insert("", "end", text=f"{monday} - {sunday} {mes_nombre} {anio_nombre}", 
                values= (f"{aleatorio[0]} / {aleatorio[1]}", f"{aleatorio[2]} / {aleatorio[3]}", f"{aleatorio_vigilancia[0]}", f"{aleatorio_vigilancia[1]}", f"{aleatorio_vigilancia[2]}"))
     

tree.pack(pady = 20)

root.mainloop()
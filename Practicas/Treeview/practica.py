import tkinter as tk
from tkinter import ttk
import random
import datetime

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Treeview")

# Crear un Treeview
tree = ttk.Treeview(root)

# Definir las columnas
tree['columns'] = ("col1", "col2", "col3", "col4", "col5")

# Formatear las columnas
tree.column("#0", width=150, minwidth=150)  # Columna de encabezado (invisible, pero necesaria)
tree.column("col1", width=225, minwidth=225)
tree.column("col2", width=225, minwidth=225)
tree.column("col3", width=225, minwidth=225)
tree.column("col4", width=225, minwidth=225)
tree.column("col5", width=225, minwidth=225)

# Definir encabezados de columna
tree.heading("#0", text="Fechas")
tree.heading("col1", text="Acomodadores 1° hora")
tree.heading("col2", text="Acomodadores 2° hora")
tree.heading("col3", text="Vigilancia 1° hora")
tree.heading("col4", text="Vigilancia 2° hora")
tree.heading("col5", text="Vigilancia despues de la reunión")

lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter","Arguello Jorge", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]

lista_vigilancia = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Monica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gomez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Dominguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela", "Altamirano Daiana"]



hoy = datetime.date(2024, 8, 14)

# Añadir datos

for i in range (3) : 

    aleatorio = random.sample(lista, 4)
    aleatorio_vigilancia = random.sample(lista_vigilancia, 3)
    tree.insert("", "end", text=f"{hoy}", values= (f"{aleatorio[0]} / {aleatorio[1]}", f"{aleatorio[2]} / {aleatorio[3]}", 
            f"{aleatorio_vigilancia[0]}", f"{aleatorio_vigilancia[1]}", f"{aleatorio_vigilancia[2]}"))

tree.pack(pady = 20)

root.mainloop()
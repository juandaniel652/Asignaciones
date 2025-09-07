from tkinter import *

#Acorde al grupo asignado, quien NO pueden estar en la Vigilancia final.

import locale
import datetime

root = Tk()
texto = Text(root)



#Este Script Organiza las limpiezas acorde a la semana transitada.

lista_vigilancia = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Monica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gomez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Dominguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela"]

lista_vigilancia.sort()


grupo_1 = ["Ferreira Rocio", "Gomez Yanina", "Israelson Analia", "Valiente Silvia"]
grupo_2 = ["Benitez Gabriela", "Dominguez Alejandra", "Quiroz Rosario"]
grupo_3 = ["Altamirano Araceli", "Altamirano Maia", "Altamirano Pamela", "Cardozo Karolaine", "Sotelo Rosa", "Viera Valeria"]
grupo_4 = ["Deiana Ruth", "Ledesma Susana", "Valiente Fátima"]
grupo_5 = ["Arguello Monica", "Coronel Vanesa", "Dominguez Miriam", "Encina Mónica", "Gonchay Brenda"]

#Ubica en español el nombre del mes
    
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

lista_semanas = []
lista_miercoles = []
lista_sabado = []

#Logro que en culauqier dia actual se coloque como lunes
lista = [1, 2, 3, 4, 5]
fecha_fija = datetime.date(2024, 8, 19)
fecha = datetime.datetime.now().date()
dia_semana = fecha.weekday()

indice = 0 

for p in lista: 

    indice = indice + 1


for i in range (6) :
#Cuando la fecha actual no cae lunes

            if dia_semana == lista[i] : 
            
                dia_calendario = datetime.timedelta(days = lista[i])
                lunes = fecha - dia_calendario
            
                break;
        
        #Cuando cae lunes

            elif dia_semana == 0 : 

                lunes = fecha
                break;

        #Excepcion de error
        
            else: 

                pass


#Aca marco la fecha del domingo como ultima semana por ende lee hasta el lunes 30 - 12- 2024
fecha_final = datetime.date(2025, 1, 5)
diferencia = fecha_final - lunes
semanas = diferencia.days / 7
num = int(semanas) + 1

#Cantidad de semanas a dividirse por la cantidad de grupos que son 5
dias = int(num / 5)
#Multiplica el entero de la cantidad de semanas por la lista, de esa manera el rango va a ser igual al total de elementos
#la lista, por consiguiente no hay error.
por_semana = lista*dias


print(num)

#A partir del comienzo del bucle de los dias lunes, lo llevo a los domingos y asi se ejecuta

for i in range (num) :
    
    #Trabajo con los dias en el bucle
    
    semana_nueva = fecha_fija + datetime.timedelta(weeks = i)

    semana_nueva_actual = lunes + datetime.timedelta(weeks = i)

    semana_completa = semana_nueva_actual + datetime.timedelta(days = 6)
    miercoles = semana_nueva_actual + datetime.timedelta(days = 2)
    sabado = semana_nueva_actual + datetime.timedelta(days = 5)

    #Lunes y Domingo, Ademas de Miércoles y Sábado

    monday = semana_nueva.strftime("%d")
    sunday = semana_completa.strftime("%d")
    wesnesday = miercoles.strftime("%d - %m - %Y")
    saturday = sabado.strftime("%d - %m - %Y")
    
    
    #Mes y año para modo reunion
    mes_nombre = semana_completa.strftime("%B")
    anio_nombre = semana_completa.strftime("%Y")

    #Muestra y contabiliza
    mostrador = f"Del {monday} al {sunday} de {mes_nombre} {anio_nombre} la limpieza corresponde al Grupo {por_semana[i - 5]}\n"


    if i == 0 : 

        if por_semana[i - 5] == 1: 

            limpieza_1 = list(set(grupo_1) & set(lista_vigilancia))
            texto.config(state = "normal")
            texto.insert( "1.0", f"Tienen Limpieza: {limpieza_1}\n\n")
            texto.config(state = "disabled")
            eliminar_1 = list(set(lista_vigilancia) - (set(grupo_1)))


        elif por_semana[i - 5] == 2 : 

            limpieza_2 = list(set(grupo_2) & set(lista_vigilancia))
            texto.config(state = "normal")
            texto.insert("1.0", f"Tienen Limpieza: {limpieza_2}\n\n")
            texto.config(state = "disabled")
            eliminar_2 = list(set(lista_vigilancia) - (set(grupo_2)))


        elif por_semana[i - 5]== 3 : 

            limpieza_3 = list(set(grupo_3) & set(lista_vigilancia))
            texto.config(state = "normal")
            texto.insert("1.0", f"Tienen Limpieza: {limpieza_3}\n\n")
            texto.config(state = "disabled")
            eliminar_3 = list(set(lista_vigilancia) - (set(grupo_3)))


        elif por_semana[i - 5] == 4 : 

            limpieza_4 = list(set(grupo_4) & set(lista_vigilancia))
            texto.config(state = "normal")
            texto.insert("1.0", f"Tienen Limpieza: {limpieza_4}\n\n")
            texto.config(state = "disabled")
            eliminar_4 = list(set(lista_vigilancia) - (set(grupo_4)))


        elif por_semana[i - 5] == 5 : 

            limpieza_5 = list(set(grupo_5) & set(lista_vigilancia))
            texto.config(state = "normal")
            texto.insert("1.0", f"Tienen Limpieza: {limpieza_5}\n\n")
            texto.config(state = "disabled")
            eliminar_5 = list(set(lista_vigilancia) - (set(grupo_5)))


        else: 
            print("Error. Intente de nuevo.")

texto.config(state = "disabled", width = 100)
texto.pack()

root.mainloop()
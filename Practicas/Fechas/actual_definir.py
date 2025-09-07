#Crear la fecha actual, y que desde ahi  me aparezcan las opciones de fechas, segun la que permita seleccionar
#y desde ahi guardar en una base de datos y que se guarde finalmente en un documento dentro de la carpeta del programa

import datetime

lista = []

fecha_actual = datetime.date(2024, 8, 5)
fecha_final = datetime.date(2024, 12, 25)

diferencia = fecha_final - fecha_actual
semanas = diferencia.days / 7
num = int(semanas) + 1

#print(f"Número de semanas entre {fecha_actual} y {fecha_final}: {semanas}")
#print(f"Fecha seleccionada: {fecha_actual}")
#print("Próximas reuniones entresemana : ")

for i in range (num) : 
    nueva_fecha = fecha_actual + datetime.timedelta(weeks=i)
    i = i + 1
   # print(f"{i}- {nueva_fecha}")
    fecha_ordenada = nueva_fecha.strftime("%d - %m - %Y")
    lista.append(fecha_ordenada)

print(lista)
 

indice = 0
        
print("\n================== \nLista actual:\n")

for x in lista: 
        indice = indice + 1
        print(f"{indice}. {x}")
print("\n================================")


indice = 0
seleccion = int(input("\nSeleccione la fecha entresemana: "))

if seleccion > 0 and seleccion != 1 : 

    indice = seleccion - 1
    print(f"\nSelecciondo = {indice + 1}. {lista[indice]}\n")
    if indice :
        pass


elif seleccion == 1 : 
    print(f"\nSelecciondo = {indice + 1}. {lista[indice]}\n")
    

else: 
    print("\nEl indice seleccionado debe ser mayor a 0.\n")



    
import random
from random import sample
import datetime
from datetime import timedelta

class Fecha: 

    def __init__(self) :

        self.final()
        
            

    def orden (self)  :

        anio = int(input("Ingrese el año desde que comienza a contar: "))
        mes = int(input("Ingrese el mes en el que comience a contar: "))
        dia = int(input("Ingrese el dia en el que comience a contar: "))
        self.lista_fecha = []


        fecha_final = datetime.date(2024, 12, 25)
    

        if anio >= 2024 and anio <= 2025 :
            if mes > 0 and mes < 13 :
                if dia > 0 and dia < 32 : 
                    fecha_actual = datetime.date(anio, mes, dia)
                    diferencia = fecha_final - fecha_actual
                    semanas = diferencia.days / 7
                    num = int(semanas) + 1

                    print(f"Número de semanas entre {fecha_actual} y {fecha_final}: {semanas}")
                    print(f"Fecha seleccionada: {fecha_actual}")
                    print("Próximas reuniones entresemana: ")


                    for i in range (num) : 
                        nueva_fecha = fecha_actual + timedelta(weeks=i)
                        i = i + 1
                        fecha = nueva_fecha.strftime("%d - %m - %Y")
                        self.lista_fecha.append(fecha)
                        print(f"{i}- {nueva_fecha}")
                    print(self.lista_fecha)
            
            self.ejemplo()

        else: 
            print(f"""\n\nError, el año debe ser desde el actual hasta 2025 inclusive.\nEl mes debe ser entre Enero (1) y Diciembre (12)\nEl dia debe ser entre el primero (1) y el último (31) como máximo\n
                \nSe Ingresó:\nAño: {anio}\nMes: {mes}\nDia: {dia}""")

    
    def ejemplo (self) : 

        lista = []
        lista_ = ["Carlos", "Juan", "Pedro", "Enrique"]
        lista_fechas = []

        for i in  self.lista_fecha: 
            lista_fechas.append(i)

        for x in lista_fechas :
            for j in lista_ : 
                lista.append((x, j))
                aleatorio = random.sample(lista_, 4)
                print(f"\n{x}\n{aleatorio[0]} / {aleatorio[1]}\n{aleatorio[2]} / {aleatorio[3]}")
                break;
                

    def final (self) : 

        self.orden()


if __name__ == '__main__' : 
    objeto = Fecha()
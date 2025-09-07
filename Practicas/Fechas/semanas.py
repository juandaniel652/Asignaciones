import datetime
from datetime import timedelta

class Fecha: 

    def __init__(self) :

        self.final()
        
            

    def orden (self)  :

        anio = int(input("Ingrese el año desde que comienza a contar: "))
        mes = int(input("Ingrese el mes en el que comience a contar: "))
        dia = int(input("Ingrese el dia en el que comience a contar: "))


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
                        print(f"{i}- {nueva_fecha}")

        else: 
            print(f"""\n\nError, el año debe ser desde el actual hasta 2025 inclusive.\nEl mes debe ser entre Enero (1) y Diciembre (12)\nEl dia debe ser entre el primero (1) y el último (31) como máximo\n
                \nSe Ingresó:\nAño: {anio}\nMes: {mes}\nDia: {dia}""")

    
    def final (self) : 

        self.orden()



if __name__ == '__main__' : 
    objeto = Fecha()

    
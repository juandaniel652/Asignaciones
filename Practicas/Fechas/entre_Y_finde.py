import datetime
from datetime import timedelta

class Fecha: 

    def __init__(self) :

        self.anio = int(input("Ingrese el año desde que comienza a contar: "))
        self.mes = int(input("Ingrese el mes en el que comience a contar: "))
        self.dia = int(input("Ingrese el dia en el que comience a contar: "))
        self.final()
        
            

    def entre_semana (self)  :

        fecha_final = datetime.date(2024, 12, 25)
    

        if self.anio >= 2024 and self.anio <= 2025 :
            if self.mes > 0 and self.mes < 13 :
                if self.dia > 0 and self.dia < 32 : 
                    fecha_actual = datetime.date(self.anio, self.mes, self.dia)
                    diferencia = fecha_final - fecha_actual
                    semanas = diferencia.days / 7
                    num = int(semanas) + 1

                    print(f"Número de semanas entre {fecha_actual} y {fecha_final}: {semanas}")
                    print(f"Fecha seleccionada: {fecha_actual}")
                    print("Próximas reuniones entre semana hasta fin del año 2024: ")


                    for i in range (num) : 
                        nueva_fecha = fecha_actual + timedelta(weeks=i)
                        i = i + 1
                        print(f"{i}- {nueva_fecha}")

        else: 
            print(f"""\n\nError, el año debe ser desde el actual hasta 2025 inclusive.\nEl mes debe ser entre Enero (1) y Diciembre (12)\nEl dia debe ser entre el primero (1) y el último (31) como máximo\n
                \nSe Ingresó:\nAño: {self.anio}\nMes: {self.mes}\nDia: {self.dia}""")

    
    def finde_semana (self) : 

        fecha_final = datetime.date(2024, 12, 28)
    

        if self.anio >= 2024 and self.anio < 2025 :
            if self.mes > 0 and self.mes < 13 :
                if self.dia > 0 and self.dia < 32 : 
                    fecha_actual = datetime.date(self.anio, self.mes, self.dia)
                    diferencia = fecha_final - fecha_actual
                    semanas = diferencia.days / 7
                    num = int(semanas) + 1

                    print(f"Número de semanas entre {fecha_actual} y {fecha_final}: {semanas}")
                    print(f"Fecha seleccionada: {fecha_actual}")
                    print("Próximas reuniones fin de semana hasta fin del año 2024: ")


                    for i in range (num) : 
                        nueva_fecha = fecha_actual + timedelta(weeks=i)
                        i = i + 1
                        print(f"{i}- {nueva_fecha}")

        else: 
            print(f"""\n\nError, el año debe ser desde el actual hasta 2025 inclusive.\nEl mes debe ser entre Enero (1) y Diciembre (12)\nEl dia debe ser entre el primero (1) y el último (31) como máximo\n
                \nSe Ingresó:\nAño: {self.anio}\nMes: {self.mes}\nDia: {self.dia}""")


    def final (self) : 

        seleccion = input("Seleccione los dias se reunión a ser revisados [Miercoles / Sabado]: ")
        seleccion.lower()

        if seleccion == 'miercoles' or seleccion == 'Miercoles': 
            self.entre_semana()

        elif seleccion == 'sabado' or seleccion == 'Sabado': 
            self.finde_semana()

        else: 
            print("Error. Vuelve a intentarlo.")


if __name__ == '__main__' : 
    objeto = Fecha()

    
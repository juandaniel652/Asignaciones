import locale
import datetime

#Ubica en español el nombre del mes
    
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

lista_semanas = []
lista_miercoles = []
lista_sabado = []

#Logro que en culauqier dia actual se coloque como lunes
lista = [1, 2, 3, 4, 5]
por3 = lista*3
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

#A partir del comienzo del bucle de los dias lunes, lo llevo a los domingos y asi se ejecuta

for i in range (num) :
    
    #Trabajo con los dias en el bucle
    
    semana_nueva = lunes + datetime.timedelta(weeks = i)

    semana_completa = semana_nueva + datetime.timedelta(days = 6)

    miercoles = semana_nueva + datetime.timedelta(days = 2)

    sabado = semana_nueva + datetime.timedelta(days = 5)

    print(f"Limpieza: {por3[i - 5]}. Semana numero: {i + 1}°")

    #print(hola[i])





    
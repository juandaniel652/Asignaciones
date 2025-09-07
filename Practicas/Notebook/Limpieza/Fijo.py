import locale
import datetime

#Este Script Organiza las limpiezas acorde a la semana transitada.

#Ubica en español el nombre del mes
    
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

lista_semanas = []
lista_miercoles = []
lista_sabado = []

#Logro que en culauqier dia actual se coloque como lunes
lista = [1, 2, 3, 4, 5]
fecha = datetime.date(2024, 9, 2)
fecha_fija = datetime.date(2024, 8, 19)
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


#A partir del comienzo del bucle de los dias lunes, lo llevo a los domingos y asi se ejecuta

for i in range (num) :
    
    #Trabajo con los dias en el bucle
    
    semana_nueva = fecha_fija + datetime.timedelta(weeks = i)

    semana_nueva_actual = lunes + datetime.timedelta(weeks = i)

    semana_completa = semana_nueva + datetime.timedelta(days = 6)

    miercoles = semana_nueva + datetime.timedelta(days = 2)

    sabado = semana_nueva + datetime.timedelta(days = 5)

    #Lunes y Domingo, Ademas de Miércoles y Sábado

    monday = semana_nueva.strftime("%d")
    sunday = semana_completa.strftime("%d")
    wesnesday = miercoles.strftime("%d - %m - %Y")
    saturday = sabado.strftime("%d - %m - %Y")
    
    
    #Mes y año para modo reunion
    mes_nombre = semana_completa.strftime("%B")
    anio_nombre = semana_completa.strftime("%Y")

    #Muestra y contabiliza
    mostrador = f"Del {monday} al {sunday} de {mes_nombre} {anio_nombre} la limpieza corresponde al Grupo {por_semana[i - 5]}"

    #print(mostrador)

    print(f"Limpieza : Grupo {por_semana[i - 5]}. Semana fija: {semana_nueva}. Semana Actualizada: {semana_nueva_actual}")

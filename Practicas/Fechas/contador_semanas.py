import locale
import datetime

#Ubica en español el nombre del mes
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
lista = []

#Creo una variabe llamada 'hoy' la cual guardara desde donde empiezo a contar
hoy = datetime.date(2024, 8, 19)

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
    lista.append(mostrador)
    print(mostrador)
    i = i + 1
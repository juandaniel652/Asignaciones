#import datetime

#hora1 = time(14)
#hora2 = time(15)
#
## Comparar horas
#if hora1 < hora2:
#    print(f"{hora1} es antes que {hora2}")
#else:
#    print(f"{hora1} es después de {hora2}")

#from datetime import datetime, timedelta, time
#
## Crear una hora específica
#hora = time(18, 58)  # 15:30:00 (3:30 PM)
#print("Hora específica:", hora)
#
## Obtener la hora actual
#hora_actual = datetime.now().time()
#print("Hora actual:", hora_actual)
#
#if hora == hora_actual : 
#    print("mismo horario")

#from datetime import datetime
#
## Obtener la hora actual
#hora_actual = datetime.now()
#
## Obtener solo la hora y los minutos
#hora = hora_actual.hour
#minutos = hora_actual.minute
#
#hora_señalada = datetime.time(18, 0, 0) 
#hora_escogida = hora_señalada.hour
#
## Imprimir la hora y los minutos
#print(f"Hora actual: {hora}:{minutos:02d}")
#
#if hora_señalada == hora :
#    print("Misma hora")



from datetime import datetime, time

# Obtener la hora actual
hora_actual = datetime.now().time()
hora = hora_actual.hour
minuto = hora_actual.minute

# Crear objetos time para las horas con las que quieres comparar
hora1 = time(6, 0)  # 14:30 (6:00 PM)
hora2 = time(13, 0)  # 13:00 (1:00 PM)
hora3 = time(20, 0) #20:00 (8: 00 PM)

hora_editable = hora_actual.strftime("%H:%m")

if hora_actual >= hora1 and hora_actual < hora2: 
    print("Buenos dias.")
    print(hora_editable)

elif hora_actual >= hora2 and hora_actual < hora3 : 
    print("Buenas tardes.")
    print(hora_editable)

elif hora_actual >= hora3 : 
    print("Buenas noches.")
    print(hora_editable)

else: 
    print("Salida")



# Comparar la hora actual con las otras horas

#if hora_actual < hora1:
#    print(f"La hora actual ({hora_actual}) es antes de {hora1}.")
#elif hora_actual > hora1 and hora_actual < hora2:
#    print(f"La hora actual ({hora_actual}) está entre {hora1} y {hora2}.")
#elif hora_actual > hora2:
#    print(f"La hora actual ({hora_actual}) es después de {hora2}.")
#else:
#    print(f"La hora actual ({hora_actual}) es exactamente {hora1} o {hora2}.")

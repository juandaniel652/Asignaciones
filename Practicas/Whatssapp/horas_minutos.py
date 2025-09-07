import datetime 

hora_actual = datetime.datetime.now()
minuto = hora_actual + datetime.timedelta(minutes = 3)

print(minuto)
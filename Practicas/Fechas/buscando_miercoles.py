#OBJETIVO: Armar las reuniones de entresemana hasta Dicimebre, solo las disponibles

import datetime 
import locale


locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

hoy = datetime.date(2024, 8, 19)
mes = datetime.date.today()
inicio_semana = hoy - datetime.timedelta(days = hoy.weekday())
miercoles = hoy + datetime.timedelta(days = 2)
fin_semana = inicio_semana + datetime.timedelta(days = 6)
mes_nombre = mes.strftime("%B")

primer_dia = inicio_semana.strftime("%d")
miercoles_dia = miercoles.strftime("%d")
ultimo_dia = fin_semana.strftime("%d")
print(f"Del {primer_dia} al {ultimo_dia} de {mes_nombre} y miercoles {miercoles_dia}")
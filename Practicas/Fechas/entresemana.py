#OBJETIVO: Armar las reuniones de entresemana hasta Dicimebre, solo las disponibles

import datetime 
import locale


locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

hoy = datetime.date.today()
mes = datetime.date.today()
inicio_semana = hoy - datetime.timedelta(days = hoy.weekday())
fin_semana = inicio_semana + datetime.timedelta(days = 6)
mes_nombre = mes.strftime("%B")

primer_dia = inicio_semana.strftime("%d")
ultimo_dia = fin_semana.strftime("%d")
print(f"Del {primer_dia} al {ultimo_dia} de {mes_nombre}")
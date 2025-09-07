from datetime import datetime, timedelta, date
import locale


# Configurar el locale a español
locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

# Fecha actual
hoy = date.today()
print("Hoy:", hoy)

# Obtener el nombre del mes
nombre_mes = hoy.strftime("%B")
print("Nombre del mes:", nombre_mes)

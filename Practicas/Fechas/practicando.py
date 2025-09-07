import datetime
from datetime import timedelta

# Calcular el número de semanas entre dos fechas
fecha1 = datetime.date(2024, 7, 10)
fecha2 = datetime.date(2024, 12, 25)
diferencia = fecha2 - fecha1
semanas = diferencia.days / 7
print(f"Número de semanas entre {fecha1} y {fecha2}: {semanas}")

# Agregar semanas a una fecha
fecha_actual = datetime.date.today()
nueva_fecha = fecha_actual + timedelta(weeks=1)
print(f"Fecha actual: {fecha_actual}")
print(f"Fecha después de sumar 3 semanas: {nueva_fecha}")

# Obtener la semana del año de una fecha
semana_del_anio = fecha_actual.isocalendar()[1]
print(f"La semana del año para la fecha {fecha_actual} es: {semana_del_anio}")

#Pasar de datetime.date a strftime
fecha1 = datetime.date(2024, 7, 10)
fecha_nueva = fecha1.strftime("%d - %m - %Y")
print(fecha_nueva)


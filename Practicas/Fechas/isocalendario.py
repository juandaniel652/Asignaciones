from datetime import datetime, date

fecha_actual = datetime(2024, 8, 6)
fecha_actualizada = fecha_actual.strftime("%d-%m-%Y")
# Obtener la semana del año de una fecha
semana_del_anio = fecha_actual.isocalendar()[1]
print(f"La semana del año para la fecha {fecha_actualizada} es: {semana_del_anio}")
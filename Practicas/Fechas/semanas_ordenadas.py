from datetime import datetime, timedelta

# Fecha inicial
fecha_inicial = datetime(2024, 8, 5)

# Número de semanas a generar
numero_de_semanas = 22

# Generar las fechas a intervalos semanales
fechas = [fecha_inicial + timedelta(weeks=i) for i in range(numero_de_semanas)]

print("Fechas a intervalos semanales:")
for fecha in fechas:
    print(fecha)
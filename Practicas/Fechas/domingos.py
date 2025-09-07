import datetime

fecha_actual = datetime.datetime.now().date()
reuniones_dia_domingo = datetime.date(2025, 12, 28)
fecha_2025 = datetime.datetime(2025, 1, 1)

if reuniones_dia_domingo.year > fecha_2025.year or reuniones_dia_domingo.month > fecha_2025.month or reuniones_dia_domingo.day > fecha_2025.day: 
    print(reuniones_dia_domingo)


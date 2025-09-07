import datetime 

hora_actual = datetime.datetime.now()

if hora_actual.hour > 6 and hora_actual.hour < 13: 
    print(f"Buenos dias. La hora {hora_actual.hour}")

elif hora_actual.hour >= 13 and hora_actual.hour < 20: 
    print(f"Buenas tardes. La hora {hora_actual.hour}")

elif hora_actual.hour >= 20 and hora_actual.hour < 2: 
    print(f"Buenas noches. La hora {hora_actual.hour}")

else: 
    print("Para tan tarde/temprano lo vas a hacer... Anda a dormir loco")
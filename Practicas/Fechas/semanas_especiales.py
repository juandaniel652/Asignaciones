import datetime


lista = [1, 2, 3, 4, 5, 6]
fecha = datetime.datetime.now().date()
fecha_especial = datetime.date(2024, 11, 1)
dia_semana = fecha.weekday()

for i in range (6) : 

    #Cuando la fecha actual no cae lunes
        if dia_semana == lista[i] : 
        
            dia_calendario = datetime.timedelta(days = lista[i])
            lunes = fecha - dia_calendario
            dia_especial = fecha_especial - dia_calendario
            break;
    
    #Cuando cae lunes
        elif dia_semana == 0 : 
            lunes = fecha
            break;


for x in range(7) : 
    fecha_final = dia_especial + datetime.timedelta(days = x - 1)
    print(fecha_final)
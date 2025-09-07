import datetime

lista_semanas = [5, 4, 3, 2, 1]
lista = [1, 2, 3, 4, 5, 6]
fecha = datetime.datetime.now().date()
fecha_señalada = datetime.date(2024, 11, 1)
dia_semana = fecha.weekday()

for i in range (6) : 

    #Cuando la fecha actual no cae lunes
        if dia_semana == lista[i] : 
        
            dia_calendario = datetime.timedelta(days = lista[i])
            lunes = fecha - dia_calendario
            break;
    
    #Cuando cae lunes
        elif dia_semana == 0 : 
            lunes = fecha
            break;


lista_s = lista_semanas[:]


for i in range(10) : 

    semanas = lunes + datetime.timedelta(weeks = i)
    fin_semana = semanas + datetime.timedelta(days = 6)
    resta = fin_semana - semanas
    print(resta)
    #print(f"{semanas} - {fin_semana}")
    
        
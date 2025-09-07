import datetime

def comienzo_semana () : 

    lista = [1, 2, 3, 4, 5, 6]
    fecha = datetime.datetime.now().date()
    dia_semana = fecha.weekday()

    for i in range (6) : 

        if dia_semana == lista[i] : 

            dia_calendario = datetime.timedelta(days = lista[i])
            lunes = fecha - dia_calendario
            print(lunes)

        elif dia_semana == 0 : 

            break;

        else: 

            pass
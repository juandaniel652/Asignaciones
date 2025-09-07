import datetime

lista = [1, 2, 3, 4, 5, 6]
fecha = datetime.datetime.now().date()
dia_semana = fecha.weekday()

for i in range (6) : 

    if dia_semana == lista[i] : 

        dia_calendario = datetime.timedelta(days = lista[i])
        lunes = fecha - dia_calendario

    elif dia_semana == 0 : 

        break;

miercoles = lunes + datetime.timedelta(days = 2)
sabado = lunes + datetime.timedelta(days = 5)

print(miercoles)

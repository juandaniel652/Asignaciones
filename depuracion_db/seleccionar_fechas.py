import sqlite3 as sql

conexion = sql.connect("asignaciones_de_congregacion.db")
cursor = conexion.cursor()

def query_seleccionar_todas_las_fechas_de_reunion ():
    cursor.execute("SELECT Dias_reunion FROM asignaciones")
    fechas = cursor.fetchall()
    #return [fecha[0] for fecha in fechas]
    return fechas

def obtener_fecha (lista):    

    tuplas = lista[0]
    dia_y_fecha = tuplas[0]
    fecha = dia_y_fecha[-14:]
    return fecha

def query_count_de_asignaciones ():

    contador = cursor.execute("SELECT COUNT(*) FROM asignaciones")
    lista = contador.fetchall()
    tupla = lista[0]
    total = tupla[0]
    return int(total)


def obtener_fecha_con_indice_para_iterar (lista, indice):   

    tuplas = lista[indice]
    dia_y_fecha = tuplas[0]
    fecha = dia_y_fecha[-14:]
    return fecha

def encontrar_anio (fecha)  :

    fecha_corregida = fecha[-4:]
    return fecha_corregida

def encontrar_mes (fecha):

    fecha_corregida = fecha[-9:-7]
    return fecha_corregida

def encontrar_dia (fecha):

    fecha_corregida = fecha[-14:-12]
    return fecha_corregida

def armar_fecha_formato_iso (dia, mes, anio) :

    fecha_formateada = anio + "-" + mes + "-" + dia
    fecha_con_comillas_para_date = f'{fecha_formateada}'
    return fecha_con_comillas_para_date

lista =  query_seleccionar_todas_las_fechas_de_reunion()
fecha = obtener_fecha(lista)
total_asignaciones = query_count_de_asignaciones()
print(lista)

#Programa Principal
for a in range (total_asignaciones): 

    fecha = obtener_fecha_con_indice_para_iterar(lista, a)
    anio = encontrar_anio(fecha)
    mes = encontrar_mes (fecha)
    dia = encontrar_dia (fecha)
    fecha_iso = armar_fecha_formato_iso(dia, mes, anio)
    print(fecha_iso)

import sqlite3 as sql

conexion = sql.connect ("asignaciones_de_congregacion.db")
cursor = conexion.cursor()

def query_acomodador_final (nombre, apellido):

    cursor.execute(f"SELECT Dias_reunion FROM asignaciones WHERE Acomodador_final = '{apellido} {nombre}'")
    fechas = cursor.fetchall()

    return fechas


def query_count_de_asignaciones (nombre, apellido):

    cursor.execute(f"SELECT COUNT(Dias_reunion) FROM asignaciones WHERE Acomodador_final = '{apellido} {nombre}'")
    count = cursor.fetchone()[0]
    print(count)


    return count

def obtener_fecha_con_indice_para_iterar (lista, indice):   

    tuplas = lista[indice]
    dia_y_fecha = tuplas[0]
    fecha = dia_y_fecha[-14:]
    return fecha

def obtener_fecha (lista):    

    tuplas = lista[0]
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


lista_acomodadores = [
    
  {"id": 14, 
  "nombre": "Elias", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 15, 
  "nombre": "Martin", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 16, 
  "nombre": "Horacio", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 17, 
  "nombre": "Joel", 
  "apellido": "Dominguez", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 18, 
  "nombre": "Gerardo", 
  "apellido": "Encina", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 19, 
  "nombre": "David", 
  "apellido": "Ferreira", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 20, 
  "nombre": "Enrique", 
  "apellido": "Gracia", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 21, 
  "nombre": "Fernando", 
  "apellido": "Israelson", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 22, 
  "nombre": "Juan", 
  "apellido": "Ontiveros", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 23, 
  "nombre": "Aureliano", 
  "apellido": "Ortiz", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 24, 
  "nombre": "Walter", 
  "apellido": "Valiente", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 25, 
  "nombre": "Cristian", 
  "apellido": "Viera", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 26, 
  "nombre": "Juan", 
  "apellido": "Herrera", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 27, 
  "nombre": "Francisco", 
  "apellido": "Cristaldo", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 28, 
  "nombre": "Luis", 
  "apellido": "Benitez", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 29, 
  "nombre": "Esteban", 
  "apellido": "Salas", 
  "estado": True, 
  "tipo_labor": "acomodador"},
  
  {"id": 30, 
  "nombre": "Horacio", 
  "apellido": "Vallejos", 
  "estado": False, 
  "tipo_labor": "acomodador"},
  
  {"id": 31, 
  "nombre": "Maximiliano", 
  "apellido": "Gomez", 
  "estado": True, 
  "tipo_labor": "acomodador"},
]
largo_lista_acomodadores = len(lista_acomodadores)
bucle = 0

while bucle < largo_lista_acomodadores:

    diccionario = lista_acomodadores[bucle]

    lista =  query_acomodador_final(diccionario["nombre"], diccionario["apellido"])
    fecha = obtener_fecha(lista)

    total_asignaciones = query_count_de_asignaciones(diccionario["nombre"], diccionario["apellido"])
    #Programa Principal
    for a in range (total_asignaciones): 
        print(diccionario["nombre"])

        fecha = obtener_fecha_con_indice_para_iterar(lista, a)
        anio = encontrar_anio(fecha)
        mes = encontrar_mes (fecha)
        dia = encontrar_dia (fecha)
        fecha_iso = armar_fecha_formato_iso(dia, mes, anio)
        print(fecha_iso)
    bucle = bucle + 1

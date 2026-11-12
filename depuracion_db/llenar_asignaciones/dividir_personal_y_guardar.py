import sqlite3 as sql

conexion = sql.connect("asignaciones_de_congregacion.db")
cursor = conexion.cursor()

def query_seleccionar_todas_las_fechas_de_reunion_personal_individual (nombre, apellido, horarios):
 
    cursor.execute(f"SELECT Dias_reunion FROM asignaciones WHERE {horarios} {apellido} {nombre}'")
    fechas = cursor.fetchall()

    return fechas

def obtener_fecha (lista):    
    tuplas = lista[0]
    dia_y_fecha = tuplas[0]
    fecha = dia_y_fecha[-14:]
    return fecha

def query_count_de_asignaciones (nombre, apellido, horarios):

    contador = cursor.execute(f"SELECT COUNT(Dias_reunion) FROM asignaciones WHERE {horarios} {apellido} {nombre}'")
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



lista_diccionario_acomodador = [
    
  {"id": 14, 
  "nombre": "Elias", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 15, 
  "nombre": "Martin", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 16, 
  "nombre": "Horacio", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 17, 
  "nombre": "Joel", 
  "apellido": "Dominguez", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 18, 
  "nombre": "Gerardo", 
  "apellido": "Encina", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 19, 
  "nombre": "David", 
  "apellido": "Ferreira", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 20, 
  "nombre": "Enrique", 
  "apellido": "Gracia", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 21, 
  "nombre": "Fernando", 
  "apellido": "Israelson", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 22, 
  "nombre": "Juan", 
  "apellido": "Ontiveros", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 23, 
  "nombre": "Aureliano", 
  "apellido": "Ortiz", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 24, 
  "nombre": "Walter", 
  "apellido": "Valiente", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 25, 
  "nombre": "Cristian", 
  "apellido": "Viera", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 26, 
  "nombre": "Juan", 
  "apellido": "Herrera", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 27, 
  "nombre": "Francisco", 
  "apellido": "Cristaldo", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 28, 
  "nombre": "Luis", 
  "apellido": "Benitez", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 29, 
  "nombre": "Esteban", 
  "apellido": "Salas", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 30, 
  "nombre": "Horacio", 
  "apellido": "Vallejos", 
  "estado": False, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
  {"id": 31, 
  "nombre": "Maximiliano", 
  "apellido": "Gomez", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": [f"Acomodadores_2_HS° like '%/"]},
  
]
lista_diccionario_vigilancia = [{"id": 32, 
  "nombre": "Maia", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 33, 
  "nombre": "Pamela", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 34, 
  "nombre": "Monica", 
  "apellido": "Arguello", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 35, 
  "nombre": "Gabriela", 
  "apellido": "Benitez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 36, 
  "nombre": "Karolaine", 
  "apellido": "Cardozo", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 37, 
  "nombre": "Graciela", 
  "apellido": "Carena", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 38, 
  "nombre": "Vanesa", 
  "apellido": "Coronel", 
  "estado": False, 
  "tipo_labor": "vigilancia"},
  
  {"id": 39, 
  "nombre": "Ruth", 
  "apellido": "Deiana", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 40, 
  "nombre": "Alejandra", 
  "apellido": "Dominguez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 41, 
  "nombre": "Miriam", 
  "apellido": "Dominguez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 42, 
  "nombre": "Monica", 
  "apellido": "Encina", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 43, 
  "nombre": "Rocio", 
  "apellido": "Ferreira", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 44, 
  "nombre": "Yanina", 
  "apellido": "Gomez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 45, 
  "nombre": "Iris", 
  "apellido": "Gonzalez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 46, 
  "nombre": "Analia", 
  "apellido": "Israelson", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 47, 
  "nombre": "Susana", 
  "apellido": "Ledesma", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 48, 
  "nombre": "Rosario", 
  "apellido": "Quiroz", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 49, 
  "nombre": "Rosa", 
  "apellido": "Sotelo", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 50, 
  "nombre": "Brisa", 
  "apellido": "Valiente", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 51, 
  "nombre": "Fatima", 
  "apellido": "Valiente", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 52, 
  "nombre": "Silvia", 
  "apellido": "Valiente", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 53, 
  "nombre": "Valeria", 
  "apellido": "Viera", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 54, 
  "nombre": "Daiana", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 55, 
  "nombre": "Sofia", 
  "apellido": "Vazquez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 56, 
  "nombre": "Raquel", 
  "apellido": "Benitez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 57, 
  "nombre": "Cristina", 
  "apellido": "Vazquez", 
  "estado": True, 
  "tipo_labor": "vigilancia"},
  
  {"id": 58, 
  "nombre": "Maria", 
  "apellido": "Alegre", 
  "estado": True, 
  "tipo_labor": "vigilancia"}
  ]



largo_lista_diccionario = int(len(lista_diccionario_acomodador))
bucle = 0


while bucle < largo_lista_diccionario:

    diccionario = lista_diccionario_acomodador[bucle]
    lista =  query_seleccionar_todas_las_fechas_de_reunion_personal_individual(diccionario["nombre"], diccionario["apellido"], diccionario["tipo_mensaje"][0])

    total_asignaciones = query_count_de_asignaciones(diccionario["nombre"], diccionario["apellido"], diccionario["tipo_mensaje"][0])
    #Programa Principal
    for a in range (total_asignaciones): 

        fecha = obtener_fecha_con_indice_para_iterar(lista, a)
        anio = encontrar_anio(fecha)
        mes = encontrar_mes (fecha)
        dia = encontrar_dia (fecha)
        fecha_iso = armar_fecha_formato_iso(dia, mes, anio)
        print(f"INSERT INTO asignacion_personal (personal_id, asignacion_id) VALUES ({bucle + 14}, {fecha_iso})")
    bucle = bucle + 1

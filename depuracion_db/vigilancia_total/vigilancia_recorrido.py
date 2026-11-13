import sqlite3 as sql

conexion = sql.connect ("asignaciones_de_congregacion.db")
cursor = conexion.cursor()

def query_vigilancia_total (nombre, apellido, tipo_vigilancia):

    cursor.execute(f"SELECT Dias_reunion FROM asignaciones WHERE {tipo_vigilancia} = '{apellido} {nombre}'")
    fechas = cursor.fetchall()

    return fechas

def query_count_de_asignaciones (nombre, apellido, tipo_vigilancia):

    cursor.execute(f"SELECT COUNT(Dias_reunion) FROM asignaciones WHERE {tipo_vigilancia} = '{apellido} {nombre}'")
    count = cursor.fetchone()[0]
    if count == []:
        return 1

    return count

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

lista_vigilancia = [{"id": 32, 
    "nombre": "Maia", 
    "apellido": "Altamirano", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 33, 
    "nombre": "Pamela", 
    "apellido": "Altamirano", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 34, 
    "nombre": "Monica", 
    "apellido": "Arguello", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 35, 
    "nombre": "Gabriela", 
    "apellido": "Benitez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 36, 
    "nombre": "Karolaine", 
    "apellido": "Cardozo", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 37, 
    "nombre": "Graciela", 
    "apellido": "Carena", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 38, 
    "nombre": "Vanesa", 
    "apellido": "Coronel", 
    "estado": False, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 39, 
    "nombre": "Ruth", 
    "apellido": "Deiana", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 40, 
    "nombre": "Alejandra", 
    "apellido": "Dominguez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 41, 
    "nombre": "Miriam", 
    "apellido": "Dominguez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 42, 
    "nombre": "Monica", 
    "apellido": "Encina", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 43, 
    "nombre": "Rocio", 
    "apellido": "Ferreira", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 44, 
    "nombre": "Yanina", 
    "apellido": "Gomez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 45, 
    "nombre": "Iris", 
    "apellido": "Gonzalez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 46, 
    "nombre": "Analia", 
    "apellido": "Israelson", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 47, 
    "nombre": "Susana", 
    "apellido": "Ledesma", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 48, 
    "nombre": "Rosario", 
    "apellido": "Quiroz", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 49, 
    "nombre": "Rosa", 
    "apellido": "Sotelo", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 50, 
    "nombre": "Brisa", 
    "apellido": "Valiente", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 51, 
    "nombre": "Fatima", 
    "apellido": "Valiente", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 52, 
    "nombre": "Silvia", 
    "apellido": "Valiente", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 53, 
    "nombre": "Valeria", 
    "apellido": "Viera", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 54, 
    "nombre": "Daiana", 
    "apellido": "Altamirano", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 55, 
    "nombre": "Sofia", 
    "apellido": "Vazquez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 56, 
    "nombre": "Raquel", 
    "apellido": "Benitez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 57, 
    "nombre": "Cristina", 
    "apellido": "Vazquez", 
    "estado": True, 
    "tipo_labor": ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]},
    
    {"id": 58, 
    "nombre": "Maria", 
    "apellido": "Alegre", 
    "estado": True, 
    "tipo_labor":  ["Vigilancia_1°_HS", "Vigilancia_2°_HS", "Vigilancia_final" ]}
    
    #LLevar a Candela Paladino a pgAdmin4 seria Id 59
    ]

indice = 0

for x in range (3):
    for persona in lista_vigilancia:
        nombre = persona["nombre"]
        apellido = persona["apellido"]
        tipo_vigilancia = persona["tipo_labor"][x]
        cantidad_de_asignaciones = query_count_de_asignaciones (nombre, apellido, tipo_vigilancia)
        #print (f"{apellido} {nombre} - {tipo_vigilancia} - Cantidad de asignaciones: {cantidad_de_asignaciones}")
        if cantidad_de_asignaciones != 0:
            for j in range (cantidad_de_asignaciones):
                fechas = query_vigilancia_total (nombre, apellido, tipo_vigilancia)
                fecha = obtener_fecha_con_indice_para_iterar (fechas, j)
                anio = encontrar_anio (fecha)
                mes = encontrar_mes (fecha)
                dia = encontrar_dia (fecha)
                fecha_iso = armar_fecha_formato_iso (dia, mes, anio)
                #print (f"Fecha: {fecha_formateada}")
                print(f"INSERT INTO asignacion_personal (personal_id, asignacion_id) VALUES ({persona['nombre']}, {fecha_iso})")
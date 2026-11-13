import sqlite3 as sql

conexion = sql.connect ("asignaciones_de_congregacion.db")
cursor = conexion.cursor()

def query_acomodador_final (nombre, apellido):
    cursor.execute(f"SELECT Dias_reunion FROM asignaciones WHERE Acomodador_final = '{apellido} {nombre}'")
    fechas = cursor.fetchall()

    return fechas


acomodador = query_acomodador_final("Juan", "Gonzalez")
print("Acomodador:", acomodador)
lista_vacia = []
print("Longitud de lista vacía:", len(lista_vacia))
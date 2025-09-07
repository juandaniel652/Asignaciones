import sqlite3 as sql
import datetime
lista = ['Gracia Enrique', 'Altamirano Martin', 'Ligeron Armando', 'Altamirano Horacio']
fecha = datetime.date(2024, 7, 24)
fecha_ord = fecha.strftime('%d - %m - %Y')

try :

    conexion = sql.connect("asignaciones.db")

    conexion.execute("""CREATE TABLE acomodador (
                     id INTEGER PRIMARY KEY,
                     acomodador_1 TEXT,
                     acomodador_2 TEXT,
                     acomodador_3 TEXT,
                     acomodador_4 TEXT,
                     vigilancia_1 TEXT,
                     vigilancia_2 TEXT,
                     vigilancia_3 TEXT,
                     fecha TEXT, 
                     );""")

    conexion.execute('''INSERT INTO acomodador (acomodador_1, acomodador_2, acomodador_3, acomodador_4,vigilancia_1, vigilancia_2, vigilancia_3 ,fecha) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (lista[0], lista[1], lista[2], lista[3], fecha_ord))
    
    conexion.commit()


except Exception as e:
    print(f"Error: {e}")

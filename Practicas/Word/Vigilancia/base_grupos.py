import sqlite3 as sql 

try : 

    conexion = sql.connect("grupos_limpieza.bd")

    conexion.execute(""""CREATE TABLE IF NOT EXISTS grupos (
                     id INTEGER PRIMARY KEY,
                     grupo_1 TEXT,
                     grupo_2 TEXT,
                     grupo_3 TEXT,
                     grupo_4 TEXT,
                     grupo_5 TEXT
                     );""""")
    
    conexion.execute(""""INSERT INTO grupos (grupo_1, grupo_2, grupo_3, grupo_4, grupo_5) 
                     VALUES (?, ?, ?, ?, ?)""""", ('Ferreira Rocio', 'Benitez Gabriela', 'Altamirano Araceli', 'Deiana Ruth'
                                                  'Arguello Monica'))
    

except Exception as e :
    print(f"Error. {e}")
    

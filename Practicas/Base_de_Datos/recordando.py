import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("mi_base_3.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mi_tabla (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    );
""")

# Generar una lista de datos grandes
nombres = ["Juan", "Pedro", "Tobias"]
edad = [19, 45, 76]
for datos in range(len(nombres)) : 

    cursor.execute("INSERT INTO mi_tabla (nombre, edad) VALUES (?, ?)", (nombres[datos], edad[datos]))

# Confirmar y cerrar conexión
conn.commit()
conn.close()

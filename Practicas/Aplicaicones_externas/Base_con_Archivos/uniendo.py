import sqlite3 as sql
import datetime

cantidad = int(input("Ingrese la cantidad de personas a registrar: "))
for i in range(cantidad) : 
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    dia = int(input("Ingrese su dia de nacimiento: "))
    mes = int(input("Ingrese su mes de nacimiento: "))
    anio = int(input("Ingrese su año de nacimiento: "))

    fecha_elegida = datetime.date(anio, mes, dia)
    fecha = fecha_elegida.strftime('%d - %m - %Y')

    try: 

            conexion = sql.connect('base_datos.db')

            cursor = conexion.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS identidad (
                           id INTEGER PRIMARY KEY, 
                           nombre TEXT, 
                           edad INTEGER, 
                           fecha_nacimiento TEXT);''')


            cursor.execute('INSERT INTO identidad (nombre, edad, fecha_nacimiento) VALUES (?, ?, ?)', (nombre, edad, fecha))
            conexion.commit()

            cursor.execute("SELECT * FROM identidad")
            filas = cursor.fetchall()
            for fila in filas : 
                print(fila)

            with open('documento.txt', 'w') as archivo : 
                  archivo.write(f'ID: {fila[0]}\nNombre: {fila[1]}\nEdad: {fila[2]}\nFecha: {fila[3]}')

    except Exception as e: 
            print(f"Error: {e}")

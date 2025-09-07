import sqlite3 as sql
import Elementos_word   
import pandas as pd
from docx2pdf import convert
import datetime
from tkinter import messagebox


def creacion_base_datos () : 

    try : 

        conectar_base = sql.connect("asignaciones_de_congregacion.db")

        cursor = conectar_base.cursor()

        # Crear una tabla
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS asignaciones (
            Semanas TEXT NOT NULL,
            Acomodadores_1_HS°  TEXT NOT NULL,
            Acomodadores_2_HS°  TEXT NOT NULL,
            Acomodador_final  TEXT NOT NULL,
            Vigilancia_1°_HS  TEXT NOT NULL,
            Vigilancia_2°_HS  TEXT NOT NULL,
            Vigilancia_final  TEXT NOT NULL,
            Dias_reunion    TEXT NOT NULL,
            Limpieza    TEXT NOT NULL,
            Id INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """)


        conectar_base.commit()
        conectar_base.close()

        return conectar_base;
    
    except Exception as error: 

        return error;


def insertar_valores (base_datos, asignaturas, numero_grupo) :

    conectar_base = sql.connect("asignaciones_de_congregacion.db")
    cursor = conectar_base.cursor()

    for asignados in range (len(asignaturas)) : 

        semanas = asignaturas[asignados][0]

        primer_hora_acomodadores = asignaturas[asignados][1]
        segunda_hora_acomodadores = asignaturas[asignados][2]
        acomodador_final = asignaturas[asignados][3]
        
        primer_hora_vigilancia = asignaturas[asignados][4]
        segunda_hora_vigilancia = asignaturas[asignados][5]
        vigilancia_final = asignaturas[asignados][6]

        dias_reunion = asignaturas[asignados][7]


        cursor.execute("INSERT INTO asignaciones (Semanas, Acomodadores_1_HS°, Acomodadores_2_HS°, Acomodador_final, Vigilancia_1°_HS, Vigilancia_2°_HS, Vigilancia_final, Dias_reunion, Limpieza) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",                  
                            (semanas, primer_hora_acomodadores, segunda_hora_acomodadores, acomodador_final, primer_hora_vigilancia, segunda_hora_vigilancia,
                            vigilancia_final, dias_reunion, f"Grupo: {numero_grupo}"))
    
    conectar_base.commit()
    conectar_base.close()

    return cursor;


def recopilar_datos_almacenados () : 

    conectar_base = sql.connect("asignaciones_de_congregacion.db")
    cursor = conectar_base.cursor()
    cursor.execute("SELECT * FROM asignaciones") 
    datos = cursor.fetchall()
    conectar_base.close()

    return datos


def mostrar_datos_en_treeview (treeview, datos) : 

    for fila in treeview.get_children() :

        treeview.delete(fila)

    for dato in datos :

        treeview.insert("", "end", values = dato)

    return dato


def pasar_datos_word () : 

    conectar_base = sql.connect("asignaciones_de_congregacion.db")
    cursor = conectar_base.cursor()
    cursor.execute("SELECT * FROM asignaciones") 
    datos = cursor.fetchall()
    conectar_base.close()

    cantidad_de_datos = len(datos)

    lista_dias_de_reunion = []
    lista_de_titulos_de_acomodadores_vigilancia = []
    lista_de_los_parrafos_general = []

    for semanas in range(len(datos)) :

        acomodadores_primera_hora = datos[semanas][1]
        acomodadores_segunda_hora = datos[semanas][2]
        acomodador_ultima_hora = datos[semanas][3]

        vigilancia_primera_hora = datos[semanas][4]
        vigilancia_segunda_hora = datos[semanas][5]
        vigilancia_ultima_hora = datos[semanas][6]
        dias_de_reuniones = datos[semanas][7]

        titulos_de_acomodadores_y_vigilancia = ["\nACOMODADORES", "VIGILANCIA"]
        lista_de_los_parrafos = [
        [f"Acomodadores 1° Hora: {acomodadores_primera_hora}", f"Acomodadores 2° Hora: {acomodadores_segunda_hora}", f"Acomodador después de la reunión: {acomodador_ultima_hora}"],
        [f"Vigilancia 1° Hora: {vigilancia_primera_hora}", f"Vigilancia 2° Hora: {vigilancia_segunda_hora}", f"Vigilancia después de la reunión: {vigilancia_ultima_hora }"]
    ]
        
        lista_dias_de_reunion.append(dias_de_reuniones)
        lista_de_titulos_de_acomodadores_vigilancia.append(titulos_de_acomodadores_y_vigilancia)
        lista_de_los_parrafos_general.append(lista_de_los_parrafos)
        
    generador_de_documentos_word = Elementos_word.generar_documento_word(lista_de_titulos_de_acomodadores_vigilancia, lista_de_los_parrafos_general, lista_dias_de_reunion, cantidad_de_datos)
    generador_de_documentos_word.save("Asignaciones.docx")


def pasar_datos_pdf () : 

    try : 
    
        convert("Asignaciones.docx")

    except Exception as error :

        messagebox.showerror("Error", f"Error al convertir el documento a PDF: {error}\n\nPor favor, verifique que el documento se encuentre en la carpeta del programa.")


def pasar_datos_excel () : 

    conexion = sql.connect("asignaciones_de_congregacion.db")

    seleccionar_todo = "SELECT * FROM asignaciones"
    guardado_de_datos = pd.read_sql_query(seleccionar_todo, conexion)

    guardado_de_datos.to_excel("Asignaciones.xlsx", index = True, engine="openpyxl")

    conexion.close()


def mostrar_asignaciones_por_mes_seleccionado (treeview, indice_seleccionado) : 

    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    conectar_base = sql.connect("asignaciones_de_congregacion.db")
    cursor = conectar_base.cursor()

    for mes in range(len(meses)) : 

        if indice_seleccionado == meses[mes] : 
        
            cursor.execute(f"SELECT * FROM asignaciones WHERE Dias_reunion like '%- 0{meses[mes]} - %'") 
            datos = cursor.fetchall()

            for fila in treeview.get_children() :

                treeview.delete(fila)

            for dato in datos :

                treeview.insert("", "end", values = dato)
                
            return datos

    conectar_base.close()


def convertir_datos_del_mes_por_word (numero_del_mes_seleccionado, nombre_del_mes_seleccionado) : 

    fecha_actual = datetime.datetime.now()
    año_actual = fecha_actual.year

    conectar_base = sql.connect("asignaciones_de_congregacion.db")
    cursor = conectar_base.cursor()
    cursor.execute("SELECT * FROM asignaciones WHERE Dias_reunion like ?", (f"%- 0{numero_del_mes_seleccionado} - {año_actual}%",)) 
    datos = cursor.fetchall()
    conectar_base.close()

    cantidad_de_datos = len(datos)

    lista_dias_de_reunion = []
    lista_de_titulos_de_acomodadores_vigilancia = []
    lista_de_los_parrafos_general = []

    for semanas in range(len(datos)) :

        acomodadores_primera_hora = datos[semanas][1]
        acomodadores_segunda_hora = datos[semanas][2]
        acomodador_ultima_hora = datos[semanas][3]

        vigilancia_primera_hora = datos[semanas][4]
        vigilancia_segunda_hora = datos[semanas][5]
        vigilancia_ultima_hora = datos[semanas][6]
        dias_de_reuniones = datos[semanas][7]

        titulos_de_acomodadores_y_vigilancia = ["\nACOMODADORES", "VIGILANCIA"]
        lista_de_los_parrafos = [
        [f"Acomodadores 1° Hora: {acomodadores_primera_hora}", f"Acomodadores 2° Hora: {acomodadores_segunda_hora}", f"Acomodador después de la reunión: {acomodador_ultima_hora}"],
        [f"Vigilancia 1° Hora: {vigilancia_primera_hora}", f"Vigilancia 2° Hora: {vigilancia_segunda_hora}", f"Vigilancia después de la reunión: {vigilancia_ultima_hora }"]
    ]
        
        lista_dias_de_reunion.append(dias_de_reuniones)
        lista_de_titulos_de_acomodadores_vigilancia.append(titulos_de_acomodadores_y_vigilancia)
        lista_de_los_parrafos_general.append(lista_de_los_parrafos)
        
    generador_de_documentos_word = Elementos_word.generar_documento_word(lista_de_titulos_de_acomodadores_vigilancia, lista_de_los_parrafos_general, lista_dias_de_reunion, cantidad_de_datos)
    generador_de_documentos_word.save(f"Asignaciones_de_{nombre_del_mes_seleccionado}_{año_actual}.docx")


def convertir_datos_del_mes_por_pdf(nombre_del_mes) :

    try : 

        fecha_actual = datetime.datetime.now()
        año_actual = fecha_actual.year

        convert(f"Asignaciones_de_{nombre_del_mes}_{año_actual}.docx")

    except Exception as error:
    
        messagebox.showerror("Error", f"Error al convertir el documento a PDF: {error}\n\nPor favor, verifique que el documento se encuentre en la carpeta del programa.") 



def convertir_datos_del_mes_por_excel(numero_del_mes_seleccionado, nombre_del_mes_seleccioando) : 

    fecha_actual = datetime.datetime.now()
    año_actual = fecha_actual.year

    conexion = sql.connect("asignaciones_de_congregacion.db")

    seleccionar_todo = (f"SELECT * FROM asignaciones WHERE Dias_reunion like '%- 0{numero_del_mes_seleccionado} - {año_actual}%'") 
    guardado_de_datos = pd.read_sql_query(seleccionar_todo, conexion)

    guardado_de_datos.to_excel(f"Asignaciones_de_{nombre_del_mes_seleccioando}_{año_actual}.xlsx", index = True, engine="openpyxl")

    conexion.close()


def obtener_nombre_de_meses () : 

    return {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
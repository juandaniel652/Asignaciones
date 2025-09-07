import tkinter as tk
from tkinter import messagebox, RIGHT, LEFT
import datetime

def creacion_tabla (treeview): 
    
    for nombre_columnas in ("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora", "Acomodador final" ,"Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia final", "Dias de reunión"):
        
        treeview.heading(nombre_columnas, text = nombre_columnas)
        tamaño_columnas = [173, 220, 220, 145, 145, 145, 145, 173]
        titulos_columnas = ["Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora", "Acomodador final" ,"Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia final", "Dias de reunión"]
        
        for columna in range(len(tamaño_columnas)) : 

            treeview.column(titulos_columnas[columna], width = tamaño_columnas[columna], minwidth = tamaño_columnas[columna])

        treeview.grid(column = 0 , row = 6, columnspan = 6, sticky='nsew')

    return treeview


def editar_tabla (evento_click, treeview, pagina_1, lista_acomodadores, lista_vigilancia, 
                    lista_semanas_totales, lista_entresemana, lista_fin_semana, 
                    semanas_especiales, dias_totales, fechas_especiales, 
                    lista_entre_semana_especial, lista_fin_de_semana_especial, 
                    dias_de_reunion_especial_entre_semana, dias_de_reunion_especial_fin_de_semana) : 
    
    identificacion_filas = treeview.identify_row(evento_click.y)
    identificacion_columnas = treeview.identify_column(evento_click.x)
    indice_columna = int(identificacion_columnas.replace('#', '')) - 1

    if identificacion_filas and identificacion_columnas:

        consulta = messagebox.askquestion("Decisión", "¿Desea editar manualmente?")

        if consulta == 'yes' :

            if not indice_columna == 7 : 

                return editar_tabla_manualmente(identificacion_filas, indice_columna, treeview, pagina_1, lista_acomodadores, lista_vigilancia)
            
            else : 
                messagebox.showerror("Error", "No es posbile editar la fecha de reunión\n(Las fecha de Entre semana o Fin de semana).\n\nSolo Acomodadores y Vigilancia.\n\nPor favor, vuelve a intentarlo.")

        else: 

            if indice_columna != 7 : 

                return editar_tabla_automaticamente(identificacion_filas, indice_columna, treeview, pagina_1 ,lista_acomodadores, lista_vigilancia, 
                                                    lista_semanas_totales, lista_entresemana, lista_fin_semana, semanas_especiales, 
                                                    dias_totales, fechas_especiales, lista_entre_semana_especial, lista_fin_de_semana_especial,
                                                    dias_de_reunion_especial_entre_semana, dias_de_reunion_especial_fin_de_semana)
            
            else : 

                messagebox.showerror("Error", "No es posbile editar la fecha de reunión\n(Las fecha de Entre semana o Fin de semana).\n\nSolo Acomodadores y Vigilancia.\n\nPor favor, vuelve a intentarlo.")


def editar_tabla_manualmente(identificacion_filas, identificacion_columnas, treeview, 
                            pagina_1 ,lista_acomodadores, lista_vigilancia) :


    if not identificacion_columnas == 0 : 

        eje_x, eje_y, ancho, alto = treeview.bbox(identificacion_filas, identificacion_columnas)  # Obtiene la posición de la celda
        valor_actual_celda = treeview.item(identificacion_filas, 'values')[identificacion_columnas]

        entrada_de_edicion = tk.Entry(pagina_1, width = ancho)
        entrada_de_edicion.place(x = eje_x + treeview.winfo_x(), y = eje_y + treeview.winfo_y(), width = ancho, height = alto)

        entrada_de_edicion.insert(0, valor_actual_celda)
        entrada_de_edicion.focus()

        def actualizar_cambios(evento_click) :

            nuevo_valor = entrada_de_edicion.get()

            for acomodador_1 in lista_acomodadores : 

                for acomodador_2 in lista_acomodadores : 

                    for vigilancia in lista_vigilancia : 

                        acomodadores = f"{acomodador_1} / {acomodador_2}"

                        if nuevo_valor == acomodadores and identificacion_columnas == 1 or nuevo_valor == acomodadores and identificacion_columnas == 2 :
                            
                            valores_actuales = list(treeview.item(identificacion_filas, 'values'))
                            valores_actuales[identificacion_columnas] = nuevo_valor
                            treeview.item(identificacion_filas, values = valores_actuales)
                            entrada_de_edicion.destroy() 

                        elif nuevo_valor == acomodador_1 and identificacion_columnas == 3 : 

                            valores_actuales = list(treeview.item(identificacion_filas, 'values'))
                            valores_actuales[identificacion_columnas] = nuevo_valor
                            treeview.item(identificacion_filas, values=valores_actuales) 
                            entrada_de_edicion.destroy()
                            
                        elif nuevo_valor == vigilancia and identificacion_columnas == 4 or nuevo_valor == vigilancia and identificacion_columnas == 5 or nuevo_valor == vigilancia and identificacion_columnas == 6 :
                            
                            valores_actuales = list(treeview.item(identificacion_filas, 'values'))
                            valores_actuales[identificacion_columnas] = nuevo_valor
                            treeview.item(identificacion_filas, values=valores_actuales)
                            entrada_de_edicion.destroy()

        entrada_de_edicion.bind('<Return>', actualizar_cambios)
        entrada_de_edicion.bind('<FocusOut>', lambda evento_click: entrada_de_edicion.destroy())
        entrada_de_edicion.bind('<Escape>', lambda event_click: entrada_de_edicion.destroy())

    else : 

        messagebox.showerror("Error", "No es posible configurar la semana de manera manual. Por favor, pruueba de nuevo, esta vez de manera automática")
            
        
def editar_tabla_automaticamente(identificacion_filas, identificacion_columnas, treeview, pagina_1 ,
                                lista_acomodadores, lista_vigilancia, semanas_totales, lista_entresemana, 
                                lista_fin_semana, semanas_especiales, dias_totales, fechas_especiales,
                                lista_entre_semana_especial, lista_fin_de_semana_especial, 
                                dias_de_reunion_especial_entre_semana, dias_de_reunion_especial_fin_de_semana) : 


    eje_x, eje_y, ancho, alto = treeview.bbox(identificacion_filas, identificacion_columnas) 
    lista_asignados = tk.Listbox(pagina_1, width = ancho)
    lista_asignados.place(x = eje_x + treeview.winfo_x(), y = eje_y + treeview.winfo_y(), width = ancho, height = alto)
    indice = 0

    if identificacion_columnas == 0 : 

        for semanas in semanas_totales : 
            lista_asignados.insert(indice, semanas)

    elif identificacion_columnas == 3 : 

        lista_acomodadores.sort(reverse = True)
        for acomodadores in lista_acomodadores : 
            lista_asignados.insert(indice, acomodadores)

    elif identificacion_columnas == 4 or identificacion_columnas == 5 or identificacion_columnas == 6 : 

        lista_vigilancia.sort(reverse = True)
        for vigilancia in lista_vigilancia : 
            lista_asignados.insert(indice, vigilancia)
        

    def actualizar_cambios(event_click):

        seleccion_asignado = lista_asignados.curselection()
        nuevo_valor = lista_asignados.get(seleccion_asignado[indice])

        if identificacion_columnas == 0 :  

            for semanas in range (len(semanas_totales)) :      

                if nuevo_valor == semanas_totales[semanas] :

                    valores_actuales = list(treeview.item(identificacion_filas, 'values'))
                    valores_actuales[identificacion_columnas] = nuevo_valor
                    treeview.item(identificacion_filas, values = valores_actuales)
                    lista_asignados.destroy() 
                    
                    for semana_especial in semanas_especiales : 

                        if semana_especial == semanas_totales[semanas]: 

                            for dias in range(len(dias_totales)) : 
                                
                                for fechas in fechas_especiales : 

                                    if fechas == dias_totales[dias] : 
                                        
                                        numero_fecha = fechas.weekday()
                                        dia_especial = fechas.strftime("%d - %m - %Y")
                                        dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

                                        for numero_dias in range(len(dias_de_la_semana)) : 
                                            
                                            if numero_dias == numero_fecha : 

                                                nombre_del_dia = dias_de_la_semana[numero_dias]

                            valores_actuales = treeview.item(identificacion_filas, values = (f"{semana_especial}","","","","","","",f"{nombre_del_dia} {dia_especial}"))
                            messagebox.showinfo("Información", "Has seleccionado una semana especial.\n\nPor favor rellene las filas con otra semana común\nya que no será posible guardar los datos.")


                        else : 

                            eleccion_dia(seleccion_asignado, identificacion_columnas, lista_asignados, 
                                identificacion_filas, pagina_1, treeview, lista_entresemana, lista_fin_semana, 
                                lista_entre_semana_especial, lista_fin_de_semana_especial,
                                dias_de_reunion_especial_entre_semana, dias_de_reunion_especial_fin_de_semana)

                            
        elif identificacion_columnas == 3 : 

            for acomodadores in lista_acomodadores :         

                if nuevo_valor == acomodadores :

                    valores_actuales = list(treeview.item(identificacion_filas, 'values'))
                    valores_actuales[identificacion_columnas] = nuevo_valor 
                    treeview.item(identificacion_filas, values=valores_actuales) 
                    lista_asignados.destroy()


        elif identificacion_columnas == 4 or identificacion_columnas == 5 or identificacion_columnas == 6 : 
            
            for vigilancia in lista_vigilancia :
            
                if nuevo_valor == vigilancia :
            
                    valores_actuales = list(treeview.item(identificacion_filas, 'values'))
                    valores_actuales[identificacion_columnas] = nuevo_valor 
                    treeview.item(identificacion_filas, values=valores_actuales) 
                    lista_asignados.destroy()


    lista_asignados.bind('<Return>', actualizar_cambios)
    lista_asignados.bind('<FocusOut>', lambda evento_click: lista_asignados.destroy())
    lista_asignados.bind('<Escape>', lambda evento_click: lista_asignados.destroy())

    if identificacion_columnas == 1 or identificacion_columnas == 2 : 

        lista_asignados.destroy()
        seleccionar_pareja_acomodadores(identificacion_columnas, identificacion_filas, pagina_1, treeview, lista_acomodadores)


def seleccionar_pareja_acomodadores (identificador_columnas, identificador_filas, pagina_1, treeview, lista_acomodadores) : 

    ventana_emergente = tk.Toplevel(pagina_1)
    ventana_emergente.title("Selecciona el tipo de reunión")
    ventana_emergente.geometry("200x210")
    ventana_emergente.resizable(False, False) 
    ventana_emergente.wm_maxsize(400, 300) 
    ventana_emergente.wm_attributes("-toolwindow", True)

    listbox = tk.Listbox(ventana_emergente, selectmode = "multiple")
    listbox.pack(fill = "both", expand = True)

    indice = 0

    for acomodadores in lista_acomodadores : 

        listbox.insert(indice, acomodadores)
        indice = indice  + 1


    def actualizar_pareja(evento_click):
        
        seleccionados = [listbox.get(acomodador) for acomodador in listbox.curselection()]

        if len(seleccionados) == 2 : 

            treeview.set(identificador_filas, identificador_columnas, " / ".join(seleccionados))   
        else :

            
            messagebox.showerror("Error", "Solo se pueden seleccionar dos acomodadores.\n\nIntenta de nuevo.")
        
        ventana_emergente.destroy()
    
    listbox.bind('<Return>', actualizar_pareja)
    

def eleccion_dia(seleccion, identificador_columnas, listbox, identificador_filas, pagina_1, treeview, 
                lista_entresemana, lista_fin_de_semana, lista_entresemana_especial, 
                lista_fin_de_semana_especial, dias_de_reunion_especial_entre_semana,
                dias_de_reunion_especial_fin_de_semana) : 

    ventana_emergente = tk.Toplevel(pagina_1)
    ventana_emergente.title("Selecciona el tipo de reunión")
    ventana_emergente.geometry("258x175")
    ventana_emergente.resizable(False, False) 
    ventana_emergente.wm_maxsize(400, 300) 
    ventana_emergente.wm_attributes("-toolwindow", True)

    etiqueta_consulta = tk.Label(ventana_emergente, text="¿Qué dia de reunión es?\n¿Entre Semana o Fin de semana?", font=("Helvetica", 12, "bold"))
    etiqueta_consulta.pack(pady=5)

    columna_final = identificador_columnas + 7
    indice = 0
    listbox = tk.Listbox(pagina_1)


    def seleccionar_reunion_entre_semana()  :

        if columna_final == 7: 

            for entre_semana in lista_entresemana : 

                listbox.insert(indice, entre_semana)

            nuevo_valor = listbox.get(seleccion[indice])

            for entre_semana in range(len(lista_entresemana)):   

                rango_adecuado = len(lista_entresemana) - (len(lista_entresemana)) 

                if dias_de_reunion_especial_entre_semana != [] : 

                    dias_entre_semana_especiales = dias_de_reunion_especial_entre_semana[rango_adecuado]

                    if dias_entre_semana_especiales == lista_entresemana_especial[entre_semana] :

                        valores_actuales = list(treeview.item(identificador_filas, 'values'))
                        valores_actuales[columna_final] = f"Martes {dias_entre_semana_especiales}"
                        treeview.item(identificador_filas, values = valores_actuales)  
                        listbox.destroy() 

                    else: 

                        if nuevo_valor == lista_entresemana [entre_semana] :
                        
                            valores_actuales = list(treeview.item(identificador_filas, 'values'))
                            valores_actuales[columna_final] = f"Miércoles {nuevo_valor}"
                            treeview.item(identificador_filas, values = valores_actuales)  
                            listbox.destroy() 

                else: 

                    if nuevo_valor == lista_entresemana [entre_semana] :
                    
                        valores_actuales = list(treeview.item(identificador_filas, 'values'))
                        valores_actuales[columna_final] = f"Miércoles {nuevo_valor}"
                        treeview.item(identificador_filas, values = valores_actuales)  
                        listbox.destroy() 

                    
            ventana_emergente.destroy()
            
            
    def seleccionar_reunion_fin_de_semana() : 

        if columna_final == 7: 

            for fin_de_semana in lista_fin_de_semana : 

                listbox.insert(indice, fin_de_semana)

            nuevo_valor = listbox.get(seleccion[indice])

            for fin_de_semana in range(len(lista_fin_de_semana)):   

                rango_adecuado = len(lista_entresemana) - (len(lista_entresemana)) 

                if dias_de_reunion_especial_fin_de_semana != [] : 

                    dias_fin_de_semana_especiales = dias_de_reunion_especial_fin_de_semana[rango_adecuado]

                    if dias_fin_de_semana_especiales == lista_fin_de_semana_especial[fin_de_semana] :

                        valores_actuales = list(treeview.item(identificador_filas, 'values'))
                        valores_actuales[columna_final] = f"Sábado {dias_fin_de_semana_especiales}"
                        treeview.item(identificador_filas, values = valores_actuales)  
                        listbox.destroy() 

                    else: 

                        if nuevo_valor == lista_fin_de_semana [fin_de_semana] :
                            
                            valores_actuales = list(treeview.item(identificador_filas, 'values'))
                            valores_actuales[columna_final] = f"Domingo {nuevo_valor}"
                            treeview.item(identificador_filas, values = valores_actuales)  
                            listbox.destroy() 

                else: 

                    if nuevo_valor == lista_fin_de_semana [fin_de_semana] :
                        
                        valores_actuales = list(treeview.item(identificador_filas, 'values'))
                        valores_actuales[columna_final] = f"Domingo {nuevo_valor}"
                        treeview.item(identificador_filas, values = valores_actuales)  
                        listbox.destroy() 
                    
        ventana_emergente.destroy()

    boton_entre_semana = tk.Button(ventana_emergente, text = "Entre semana", background = "#1976D2", foreground = "white" , relief = "groove" , activebackground = "gray95" , activeforeground = "black" , border = 10, width = 10, command = seleccionar_reunion_entre_semana)
    boton_fin_semana = tk.Button(ventana_emergente, text = "Fin de semana", background = "#1976D2", foreground = "white" , relief = "groove" , activebackground = "gray95" , activeforeground = "black" , border = 10, width = 10, command = seleccionar_reunion_fin_de_semana)
    boton_entre_semana.pack(side = LEFT, padx=5)
    boton_fin_semana.pack(side = RIGHT, padx = 5)
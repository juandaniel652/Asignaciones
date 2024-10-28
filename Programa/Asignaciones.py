import random
import tkinter as tk 
from tkinter import ttk, END, font, PhotoImage, messagebox, Text, Toplevel, LEFT, RIGHT
from PIL import Image, ImageTk
import locale
import datetime
import sqlite3 as sql

class Asignaciones : 

    def __init__ (self) : 


    #WIDGETS GENERLES

        self.root = tk.Tk()
        self.root.title("Asignaciones")

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True) # Expand permite que el notebook se redimensione con la ventana
        
        # Crear los frames que serán las secciones (pestañas)
        self.tab1 = tk.Frame(notebook)
        self.tab2 = tk.Frame(notebook)
        
        # Agregar los frames al notebook con un nombre (etiqueta) para cada pestaña
        notebook.add(self.tab1, text="Ingreso")
        notebook.add(self.tab2, text="Historial")

        self.diseño_titulo = font.Font(size = 15, family = "bold")
        self.diseño_lista = font.Font(size = 10, family = "Italic")

        self.titulo_acomodadores = tk.Label(self.tab1, text = "Acomodadores" ,fg = "black", relief = "solid", font = self.diseño_titulo, background = "white")
        self.listbox_acomodadores = tk.Listbox(self.tab1, relief = "raised", font = self.diseño_lista, foreground = "white", background = "black")
    
        self.titulo_vigilancia = tk.Label(self.tab1, text = "Vigilancia" ,fg = "black", relief = "solid",font = self.diseño_titulo, background = "white")
        self.listbox_vigilancia = tk.Listbox(self.tab1, relief = "raised", font = self.diseño_lista, foreground = "white", background = "black")

        self.titulo_fecha = tk.Label(self.tab1, text = "Semanas", fg = "black", relief = "solid", font = self.diseño_titulo, background = "white")
        self.caja = tk.Listbox(self.tab1, relief = "raised", font = self.diseño_lista, foreground = "white", background = "black", width = 30)

        self.titulo_limpieza = tk.Label(self.tab1, text = "Limpieza", fg = "black", relief = "solid", font = self.diseño_titulo, background = "white")

        #Crear un widget Label para mostrar la imagen
        self.root.iconbitmap(True, 'cuaderno.ico')  
        
        self.final()
        self.root.mainloop()


 #==================================================================================================  

    #BOTONES VENTANA: opciones generales
    #WIDGETS
    
    def botones_ventana (self) : 

        boton_fondo = tk.Button(self.tab1, text = "Modo Oscuro", background = "purple", foreground = "white", relief = "groove", activebackground="gray95",activeforeground = "black", command = self.cambio)
        boton_defecto = tk.Button(self.tab1, text = "Modo Claro", background = "purple", foreground = "white", relief = "groove" , activebackground="gray95",activeforeground = "black", command = self.defecto)
        boton_treeview = tk.Button(self.tab1, text = "Dia Miércoles", background = "purple", foreground = "white", relief = "groove" , activebackground="gray95",activeforeground = "black", command = self.treeview_miercoles)
        boton_treeview_1 = tk.Button(self.tab1, text = "Dia Sabado", background = "purple", foreground = "white", relief = "groove" ,activebackground="gray95",activeforeground = "black", command = self.treeview_sabado)
        boton_salir = tk.Button(self.tab1, text = "Salir", background = "purple", foreground = "white", relief = "groove", activebackground="gray95",activeforeground = "black", command = self.salir)
        
        boton_fondo.grid(column = 0, row = 7)
        boton_defecto.grid(column = 1, row = 7)
        boton_treeview.grid(column = 2, row = 7)
        boton_treeview_1.grid(column = 3, row = 7)
        boton_salir.grid(column = 4, row = 7)


#==================================================================================================
    #SECCIÓN: Treeview

    def treeview (self) : 


        self.tree = ttk.Treeview(self.tab1, columns=("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora", "Acomodador final" ,"Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia final", "Dias de reunión"), show='headings')

        for col in ("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora", "Acomodador final" ,"Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia final", "Dias de reunión"):
            self.tree.heading(col, text=col)
            
        #self.tree.column("#0", width=195, minwidth=195)  # Columna de encabezado (invisible, pero necesaria)
        self.tree.column("Semanas", width=173, minwidth=173)
        self.tree.column("Acomodadores 1° hora", width=227, minwidth=227)
        self.tree.column("Acomodadores 2° hora", width=227, minwidth=227)
        self.tree.column("Acomodador final", width=150, minwidth=150)
        self.tree.column("Vigilancia 1° hora", width=150, minwidth=150)
        self.tree.column("Vigilancia 2° hora", width=150, minwidth=150)
        self.tree.column("Vigilancia final", width=150, minwidth=150)
        self.tree.column("Dias de reunión", width=165, minwidth=165)


        self.tree.grid(column = 0 , row = 6, columnspan = 6, sticky='nsew')

        self.tree.bind("<Double-1>", self.editar_celdas)


    #En esta funcion, logro mediante un evento 'doble click' llegar al lugar para editar
    def editar_celdas (self, event) : 

        item_id = self.tree.identify_row(event.y)  # Obtiene el ID del item
        column = self.tree.identify_column(event.x)  # Obtiene la columna
        col_index = int(column.replace('#', '')) - 1  # Convierte la columna al índice correcto

        if item_id and column:

            respuesta = messagebox.askquestion("Decisión", "¿Desea editar manualmente?")

            if respuesta == 'yes':

                if not  col_index == 7 : 
                
                    self.entry_editing(item_id, col_index)

                else : 
                    
                    messagebox.showerror("Error", "No es posbile editar la fecha de reunión\n(Las fecha de Entre semana o Fin de semana).\n\nSolo Acomodadores y Vigilancia.\n\nPor favor, vuelve a intentarlo.")

            else:
                
                if col_index != 7 : 

                    self.table_editing(item_id, col_index)

                else: 
                    messagebox.showerror("Error", "No es posbile editar la fecha de reunión\n(Las fecha de Entre semana o Fin de semana).\n\nSolo Acomodadores y Vigilancia.\n\nPor favor, vuelve a intentarlo.")



    # Función para iniciar la edición (Manualmente)
    def entry_editing(self, item_id, col_index):


        if not col_index == 0 : 

            x, y, width, height = self.tree.bbox(item_id, col_index)  # Obtiene la posición de la celda
            text = self.tree.item(item_id, 'values')[col_index]  # Obtiene el valor actual de la celda

            # Crea un Entry para la edición
            entry = tk.Entry(self.tab1, width=width)
            entry.place(x=x + self.tree.winfo_x(), y=y + self.tree.winfo_y(), width=width, height=height)

            entry.insert(0, text)  # Inserta el texto actual en el Entry
            entry.focus()

                #Función para manejar cuando se presiona Enter en el Entry
            def on_enter(event):
                new_value = entry.get()
                for x in self.lista : 
                    for p in self.lista : 
                        for j in self.lista_asignada : 

                            acomodadores = f"{x} / {p}"

                            if new_value == acomodadores and col_index == 1 or new_value == acomodadores and col_index == 2 :

                                current_values = list(self.tree.item(item_id, 'values'))
                                current_values[col_index] = new_value  # Actualiza el valor en la lista
                                self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                                entry.destroy()  # Elimina el Entry

                            elif new_value == x and col_index == 3 : 
                                current_values = list(self.tree.item(item_id, 'values'))
                                current_values[col_index] = new_value  # Actualiza el valor en la lista
                                self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                                entry.destroy()  # Elimina el Entry
                            
                            elif new_value == j and col_index == 4 or new_value == j and col_index == 5 or new_value == j and col_index == 6:

                                current_values = list(self.tree.item(item_id, 'values'))
                                current_values[col_index] = new_value  # Actualiza el valor en la lista
                                self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                                entry.destroy()  # Elimina el Entry

            entry.bind('<Return>', on_enter)
            entry.bind('<FocusOut>', lambda event: entry.destroy())  # Elimina el Entry si se pierde el foco
            entry.bind('<Escape>', lambda event: entry.destroy())

        else : 

            messagebox.showerror("Error", "No es posible configurar la semana de manera manual. Por favor, pruueba de nuevo, esta vez de manera automática")


    # Función para iniciar la edición (Tabla definida)

    def table_editing(self, item_id, col_index) : 

            x, y, width, height = self.tree.bbox(item_id, col_index)  # Obtiene la posición de la celda

            listbox = tk.Listbox(self.tab1, width = width)
            listbox.place(x=x + self.tree.winfo_x(), y=y + self.tree.winfo_y(), width=width, height=height)

            indice = 0

            if col_index == 0 : 
                for q in self.lista_semanas : 
                    listbox.insert(indice, q)

                
            elif col_index == 3 : 
                self.lista.sort(reverse = True)
                for l in self.lista : 
                    listbox.insert(indice, l)

            elif col_index == 4 or col_index == 5 or col_index == 6 : 

                self.lista_asignada.sort(reverse = True)
                for x in self.lista_asignada : 
                    listbox.insert(indice, x)  # Inserta el texto actual en el Entry
        
    
            # Función para manejar cuando se presiona Enter en el Entry
            def on_enter(event):

                seleccion = listbox.curselection()
                new_value = listbox.get(seleccion[indice])

                if col_index == 0 :  
                    for s in self.lista_semanas:         
                        if new_value == s :
                            current_values = list(self.tree.item(item_id, 'values'))
                            current_values[col_index] = new_value  # Actualiza el valor en la lista
                            self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                            listbox.destroy()  # Elimina el Entry

                            if not new_value == self.semana_especial and not new_value == self.semana_especial_2 :
                                self.eleccion_dia(seleccion, col_index, listbox, item_id)
                            else : 
                                self.tree.set(item_id, col_index, new_value)
                            

                elif col_index == 3 : 
                    for p in self.lista:         
                        if new_value == p :
                            current_values = list(self.tree.item(item_id, 'values'))
                            current_values[col_index] = new_value  # Actualiza el valor en la lista
                            self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                            listbox.destroy()  # Elimina el Entry

                elif col_index == 4 or col_index == 5 or col_index == 6 : 
                    for i in self.lista_asignada :
                        if new_value == i :
                            current_values = list(self.tree.item(item_id, 'values'))
                            current_values[col_index] = new_value  # Actualiza el valor en la lista
                            self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                            listbox.destroy()  # Elimina el Entry


            listbox.bind('<Return>', on_enter)
            listbox.bind('<FocusOut>', lambda event: listbox.destroy())  # Elimina el Entry si se pierde el foco
            listbox.bind('<Escape>', lambda event: listbox.destroy())

            if col_index == 1 or col_index == 2 : 
                listbox.destroy()
                self.pareja_acomodadores(col_index, item_id)

    
    def eleccion_dia(self, seleccion, col_index, listbox, item_id) : 

        ventana_emergente = tk.Toplevel(self.tab1)
        ventana_emergente.title("Selecciona el tipo de reunión")
        ventana_emergente.geometry("258x175")
        ventana_emergente.resizable(False, False) 

        ventana_emergente.wm_maxsize(400, 300) 
        ventana_emergente.wm_attributes("-toolwindow", True)

        etiqueta = tk.Label(ventana_emergente, text="¿Qué dia de reunión es?\n¿Entre Semana o Fin de semana?", font=("Helvetica", 12, "bold"))
        etiqueta.pack(pady=5)

        col_f = col_index + 7
        item_id = item_id
        seleccion = seleccion
        indice = 0
        listbox = tk.Listbox(self.tab1)

         
        def entre_sem()  :
    
            if col_f == 7 : 
                for u in self.lista_miercoles : 
                   listbox.insert(indice, u)
                
                new_value = listbox.get(seleccion[indice])
                for s in self.lista_miercoles:         
                    if new_value == s :
                        current_values = list(self.tree.item(item_id, 'values'))
                        current_values[col_f] = f"Miércoles: {new_value}"  # Actualiza el valor en la lista
                        self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                        listbox.destroy()  # Elimina el Entry
                
            ventana_emergente.destroy()
            
            
        def fin_de_sem() : 

            if col_f == 7 : 
                for u in self.lista_sabado : 
                   listbox.insert(indice, u)
                
                new_value = listbox.get(seleccion[indice])
                for s in self.lista_sabado:         
                    if new_value == s :
                        current_values = list(self.tree.item(item_id, 'values'))
                        current_values[col_f] = f"Sabado: {new_value}"  # Actualiza el valor en la lista
                        self.tree.item(item_id, values=current_values)  # Establece los nuevos valores en la fila
                        listbox.destroy()  # Elimina el Entry

                ventana_emergente.destroy()


        boton_entre_semana = tk.Button(ventana_emergente, text = "Entre semana", background = "purple", foreground = "white", relief = "groove", activebackground="gray95",activeforeground = "black", border = 10, width = 10, command = entre_sem)
        boton_fin_semana = tk.Button(ventana_emergente, text = "Fin de semana", background = "purple", foreground = "white", relief = "groove", activebackground="gray95",activeforeground = "black", border = 10, width = 10, command = fin_de_sem)
        boton_entre_semana.pack(side = LEFT, padx=5)
        boton_fin_semana.pack(side = RIGHT, padx = 5)

    
    def pareja_acomodadores (self, col_index, item_id) : 

        ventana_emergente = tk.Toplevel(self.tab1)
        ventana_emergente.title("Selecciona el tipo de reunión")
        ventana_emergente.geometry("200x210")
        ventana_emergente.resizable(False, False) 

        ventana_emergente.wm_maxsize(400, 300) 
        ventana_emergente.wm_attributes("-toolwindow", True)

        listbox = tk.Listbox(ventana_emergente, selectmode = "multiple")
        listbox.pack(fill = "both", expand = True)

        col_index = col_index
        item_id = item_id

        indice = 0
        for r in self.lista : 
            listbox.insert(indice, r)
            indice = indice  + 1

        def select_items(event):
           
            selected = [listbox.get(i) for i in listbox.curselection()]
            if len(selected) == 2 :  # Solo permitir un máximo de 2 selecciones

                self.tree.set(item_id, col_index, " / ".join(selected))
              
            else:
                messagebox.showerror("Error", "Solo se pueden seleccionar dos acomodadores.\n\nIntenta de nuevo.")

            ventana_emergente.destroy()

        listbox.bind('<Return>', select_items)


#==================================================================================================


    #SECCIÓN: Acomodadores
    #WIDGETS

    def lista_acomodadores (self) : 

        self.lista = ["Ferreira David" ,"Ortiz Aureliano", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter","Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Altamirano Elias", "Vallejos Horacio", "Viera Cristian"]
        
        self.lista.sort()
      
        
        indice = 0

        for i in self.lista : 
            self.listbox_acomodadores.insert(indice, i)
            indice = indice  + 1

        self.titulo_acomodadores.grid(row = 0, column = 0)
        self.listbox_acomodadores.grid(row = 1, column = 0)

    
    def botonnes_acomodadores (self) :

        self.boton_remover_acom = tk.Button(self.tab1 , text = "Remover", relief = "groove" ,background = "purple", foreground = "white", command = self.remover_acomodadores)
        self.boton_aleatorio_acom = tk.Button(self.tab1, text = "Seleccion aleatoria", relief = "groove", background = "purple", foreground = "white", command = self.aleatorio_acomodadores)
        self.boton_reiniciar_acom = tk.Button(self.tab1, text = "Reiniciar", relief = "groove", background = "purple", foreground = "white", command = self.reiniciar_acomodadores)
        
        self.boton_remover_acom.grid(column = 0, row = 2)
        self.boton_aleatorio_acom.grid(column = 0, row = 3)
        self.boton_reiniciar_acom.grid(column = 0, row =  4)


    #==================================================================================================

    #SECCIÓN: Vigilancia
    #WIDGETS

    def lista_vigilancia (self) : 

        self.lista_asignada = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Monica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gomez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Dominguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela"]
    
        self.lista_asignada.sort()

        self.grupo_1 = ["Ferreira Rocio", "Gomez Yanina", "Israelson Analia", "Valiente Silvia"]
        self.grupo_2 = ["Benitez Gabriela", "Dominguez Alejandra", "Quiroz Rosario"]
        self.grupo_3 = ["Altamirano Araceli", "Altamirano Maia", "Altamirano Pamela", "Cardozo Karolaine", "Sotelo Rosa", "Viera Valeria"]
        self.grupo_4 = ["Deiana Ruth", "Ledesma Susana", "Valiente Fátima"]
        self.grupo_5 = ["Arguello Monica", "Coronel Vanesa", "Dominguez Miriam", "Encina Mónica", "Gonchay Brenda"]

    
        indice = 0

        for i in self.lista_asignada : 
            self.listbox_vigilancia.insert(indice, i)
            indice = indice  + 1
        
        self.titulo_vigilancia.grid(column = 1, row = 0)
        self.listbox_vigilancia.grid(column = 1, row = 1)

    
    def botones_vigilancia (self) : 

        self.boton_remover_vil = tk.Button(self.tab1, text = "Remover", relief = "groove", background = "purple", foreground = "white", command = self.remover_vigilancia)
        self.boton_aleatorio_vil = tk.Button(self.tab1, text = "Seleccion aleatoria", relief = "groove", background = "purple", foreground = "white", command = self.aleatorio_vigilancia)
        self.boton_reiniciar_vil = tk.Button(self.tab1, text = "Reiniciar", relief = "groove", background = "purple", foreground = "white", command = self.reiniciar_vigilancia)
        
        self.boton_remover_vil.grid(column = 1, row = 2)
        self.boton_aleatorio_vil.grid(column = 1, row = 3)
        self.boton_reiniciar_vil.grid(column = 1, row = 4)

    #==================================================================================================

    #SECCIÓN: Fecha
    #WIDGETS

    def semanas (self) : 

        #Ubica en español el nombre del mes
        locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
        lista_limpieza = [5, 4, 3, 2, 1]
        self.lista_semanas = []
        self.lista_miercoles = []
        self.lista_sabado = []

        #Logro que en culauqier dia actual se coloque como lunes
        lista = [1, 2, 3, 4, 5, 6]
        fecha = datetime.datetime.now().date()
        fecha_fija = datetime.date(2024, 8, 19)
        fecha_especial = datetime.date(2024, 11, 1)
        fecha_especial_2 = datetime.date(2025, 2, 2)
        dia_semana = fecha.weekday()

        for i in range (6) : 

        #Cuando la fecha actual no cae lunes

            if dia_semana == lista[i] : 
            
                dia_calendario = datetime.timedelta(days = lista[i])
                lunes = fecha - dia_calendario
                dia_especial = fecha_especial - dia_calendario
                break;
        
        #Cuando cae lunes

            elif dia_semana == 0 : 

                lunes = fecha
                break;

        #Excepcion de error
        
            else: 

                pass;

        #Aca marco la fecha del domingo como ultima semana por ende lee hasta el lunes 30 - 12- 2024
        fecha_final = datetime.date(2025, 1, 5)
        diferencia = fecha_final - fecha_fija
        semanas = diferencia.days / 7
        num = int(semanas) + 1


        #A partir del comienzo del bucle de los dias lunes, lo llevo a los domingos y asi se ejecuta
        for i in range (num) : 
        
            #Trabajo con los dias en el bucle
            semana_nueva_actual = lunes + datetime.timedelta(weeks = i)
            semana_completa = semana_nueva_actual + datetime.timedelta(days = 6)
            miercoles = semana_nueva_actual + datetime.timedelta(days = 2)
            sabado = semana_nueva_actual + datetime.timedelta(days = 5)


            #Lunes y Domingo, Ademas de Miércoles y Sábado
            monday = semana_nueva_actual.strftime("%d")
            sunday = semana_completa.strftime("%d")
            wesnesday = miercoles.strftime("%d - %m - %Y")
            saturday = sabado.strftime("%d - %m - %Y")
            
            
            #Mes y año para modo reunion
            mes_nombre = semana_completa.strftime("%B")
            anio_nombre = semana_completa.strftime("%Y")

            #Muestra y contabiliza
            self.mostrador = f"Del {monday} al {sunday} de {mes_nombre} {anio_nombre}\n"
            self.lista_semanas.append(self.mostrador)
            self.lista_miercoles.append(wesnesday)
            self.lista_sabado.append(saturday)

    
            for x in range(7) : 

                fecha_final = semana_nueva_actual + datetime.timedelta(days = x)

                if fecha_final == fecha_especial:

                    self.semana_especial = self.mostrador

                elif fecha_final == fecha_especial_2:

                    self.semana_especial_2 = self.mostrador

                else : 

                    self.mostrador = self.mostrador

                    

        fecha_final_grupos = datetime.date(2030, 12, 15)
        diferencia_grupos = fecha_final_grupos - fecha
        semanas_grupos = diferencia_grupos.days // 7
        num_g = semanas_grupos

        self.por_semana = []
        self.por_semana = lista_limpieza[:] * i

        
        for l in range(num_g) : 

            self.por_semana = self.por_semana [1:] + self.por_semana [:1]

        
        post_especial = fecha_final - fecha_especial
        semanas_post = post_especial.days / 7
        self.num_post= int(semanas_post)

        if semana_nueva_actual : 
            self.num_post += 1



        post_especial_2 = fecha_final - fecha_especial_2
        semanas_post_2 = post_especial_2.days / 7
        self.num_post_2= int(semanas_post_2)

        if semana_nueva_actual : 
            self.num_post_2 += 1


        return self.lista_semanas



    def lista_fechas (self) : 
 
        indice = 0

        for x in self.lista_semanas : 
            self.caja.insert(indice, x)
            indice = indice  + 1
        
        self.titulo_fecha.grid(column = 2, row = 0)
        self.caja.grid(column = 2, row = 1)


    def botones (self) : 

        mostrar = tk.Button(self.tab1, text = "Mostrar", relief = "groove", background = "purple", foreground = "white" ,command = self.muestra)
        self.remover_pantalla = tk.Button(self.tab1, text = "Remover", relief = "groove", background = "purple", foreground = "white",  command = self.remover)
        mostrar.grid(column = 2, row = 2)
        self.remover_pantalla.grid(column = 3, row = 2)
        
            
    
    def texto_limpieza (self) : 


        self.pantalla = Text(self.tab1)

        self.pantalla.config(state = "disabled", width = 38, height = 11, bg = "black", fg = "white")

        self.pantalla.grid(column = 3, row = 1, pady = 15)

        self.titulo_limpieza.grid(column = 3, row = 0)

        

    #============================FUNCIONALIDAD==============================================

    #BOTONES GENERALES

    def cambio (self) : 
 
        self.root.config(background = "gray14")
        self.tab1.config(bg = "gray14", highlightbackground = "gray14", relief = "ridge")
        self.tab2.config(bg = "gray14", highlightbackground = "gray14", relief = "ridge")

        self.titulo_acomodadores.config(fg = "white", bg = "gray14")
        self.titulo_vigilancia.config(fg = "white", bg = "gray14")
        self.titulo_fecha.config(fg = "white", bg = "gray14")
        self.titulo_limpieza.config(fg = "white", bg = "gray14")

        self.listbox_acomodadores.config(fg = "black", bg = "white")
        self.listbox_vigilancia.config(fg = "black", bg = "white")
        self.caja.config(fg = "black", bg = "white")
        self.pantalla.config(bg = "white", fg = "black")
        
       
    def defecto (self) : 

        self.root.config(background = "gray97")
        self.tab1.config(bg = "white")
        self.tab2.config(bg = "white")

        self.titulo_acomodadores.config (fg = "black", bg = "white")
        self.titulo_vigilancia.config (fg = "black", bg = "white")
        self.titulo_fecha.config (fg = "black", bg = "white")
        self.titulo_limpieza.config (fg = "black", bg = "white")

        self.listbox_acomodadores.config(fg = "white", bg = "black")
        self.listbox_vigilancia.config(fg = "white", bg = "black")
        self.caja.config(fg = "white", bg = "black")
        self.pantalla.config(bg = "black", fg = "white")

    
    def salir (self) : 

        self.root.quit()

    #=============================================================================================

    #BOTONES ACOMODADORES

    def remover_acomodadores (self): 

        seleccion = self.listbox_acomodadores.curselection()
        indice = 0
        if seleccion : 
            self.listbox_acomodadores.delete(seleccion[indice])
            del self.lista [seleccion[indice]]


    def aleatorio_acomodadores (self) : 

        try : 

            self.seleccion_acomodadores = random.sample(self.lista, 5)
            messagebox.showinfo("Seleccionado", f"""Acomodadores 1° hora: {self.seleccion_acomodadores[0]} / {self.seleccion_acomodadores [1]}\n\nAcomodadores 2° hora: {self.seleccion_acomodadores[2]} / {self.seleccion_acomodadores[3]}\n\nAcomodador después de la reunión: {self.seleccion_acomodadores[4]}""")

        except Exception as e : 
            messagebox.showerror("Error",f"Debe haber un mínimo de 5 opciones\nCausa: {e}")

    def reiniciar_acomodadores (self) : 

        self.listbox_acomodadores.delete(0, END)
        self.lista_acomodadores()
        
    
    #=============================================================================================

    #BOTONES VIGILANCIA

    def remover_vigilancia (self): 

        seleccion = self.listbox_vigilancia.curselection()
        indice = 0
        if seleccion : 
            self.listbox_vigilancia.delete(seleccion[indice])
            del self.lista_asignada [seleccion[indice]]
            


    def aleatorio_vigilancia (self) : 

        try : 

            self.seleccion_vigilancia = random.sample(self.lista_asignada, 3)
            messagebox.showinfo("Seleccionado", f"""Vigilancia 1° hora: {self.seleccion_vigilancia[0]}\n\nVigilancia 2° hora: {self.seleccion_vigilancia[1]}\n\nVigilancia después de la reunión: {self.seleccion_vigilancia[2]}""")
        
        except Exception as e : 
            messagebox.showerror("Error",f"Debe haber un mínimo de 3 opciones\nCausa: {e}")


    def reiniciar_vigilancia (self) : 

        self.listbox_vigilancia.delete(0, END)
        self.lista_vigilancia()


    #=============================================================================================
    #BOTONES FECHAS

    def muestra (self) : 
            
        try: 

            try : 

                seleccion = self.caja.curselection()
                self.indice = 0


                for self.indice in seleccion : 


                    if seleccion : 
                    
                        grupo = self.por_semana[self.indice]


                        if grupo != self.por_semana[0] : 

                            if grupo == self.por_semana[1]  :
                                grupo = self.por_semana[self.indice + 3]

                            elif grupo == self.por_semana[2] : 
                                grupo = self.por_semana[self.indice + 1]

                            elif grupo == self.por_semana[3] : 
                                grupo = self.por_semana[self.indice - 1]

                            elif grupo == self.por_semana[4] : 
                                grupo = self.por_semana[self.indice - 3]


                        elif grupo == self.por_semana[0] : 

                            pass;

                        else :

                            print("Intente de nuevo.")


                        messagebox.showinfo("Seleccionado", f"Semana seleccionada: {self.lista_semanas[self.indice]}") 

                        self.pantalla.config(state = "normal")
                        self.pantalla.delete("1.0", END)
                        self.pantalla.insert("1.0", f"{self.lista_semanas[self.indice]}\n")


                        if self.lista_semanas[self.indice] == self.semana_especial:
                            self.pantalla.insert("4.0",f"Asamblea Regional 2024.\n¡Prediquemos las buenas noticias!")
                            self.pantalla.config(state = "disabled")
                            self.listbox_acomodadores.delete(0, END)
                            self.listbox_vigilancia.delete(0, END)
                            self.boton_aleatorio_acom.configure(state = "disabled")
                            self.boton_reiniciar_acom.configure(state = "disabled")
                            self.boton_remover_acom.configure(state = "disabled")
                            self.boton_aleatorio_vil.configure(state = "disabled")
                            self.boton_reiniciar_vil.configure(state = "disabled")
                            self.boton_remover_vil.configure(state = "disabled")
                            self.remover_pantalla.configure(state = "disabled")


                        elif self.lista_semanas[self.indice] == self.semana_especial_2:
                            self.pantalla.insert("4.0",f"Asamblea de circuito 2024-2025\n(Con el superitendente de circuito).\n\n'Pórtense de una manera digna\nde las buenas noticias'")
                            self.pantalla.config(state = "disabled")
                            self.listbox_acomodadores.delete(0, END)
                            self.listbox_vigilancia.delete(0, END)
                            self.boton_aleatorio_acom.configure(state = "disabled")
                            self.boton_reiniciar_acom.configure(state = "disabled")
                            self.boton_remover_acom.configure(state = "disabled")
                            self.boton_aleatorio_vil.configure(state = "disabled")
                            self.boton_reiniciar_vil.configure(state = "disabled")
                            self.boton_remover_vil.configure(state = "disabled")
                            self.remover_pantalla.configure(state = "disabled")


                        elif self.lista_semanas[self.indice] != self.semana_especial :
                            self.reiniciar_acomodadores()
                            self.reiniciar_vigilancia()
                            self.boton_aleatorio_acom.configure(state = "normal")
                            self.boton_reiniciar_acom.configure(state = "normal")
                            self.boton_remover_acom.configure(state = "normal")
                            self.boton_aleatorio_vil.configure(state = "normal")
                            self.boton_reiniciar_vil.configure(state = "normal")
                            self.boton_remover_vil.configure(state = "normal")
                            self.remover_pantalla.configure(state = "normal")

                            for x in range (self.num_post) : 

                                if self.lista_semanas[self.indice - x] == self.semana_especial :

                                    if grupo == 1 : 
                                        grupo = grupo + 4

                                    else: 
                                        grupo = grupo - 1


                            for i in range (self.num_post_2) : 

                                if self.lista_semanas[self.indice - i] == self.semana_especial_2 :

                                    if grupo == 1 : 

                                        grupo = grupo + 4

                                    else: 
                                        grupo = grupo - 1



            except : 

                try : 

                    if grupo == 1 : 

                        grupo = grupo + 4                               

                    else: 

                        grupo = grupo - 1


                    if self.lista_semanas[self.indice] == self.semana_especial_2 : 

                        self.pantalla.insert("4.0",f"Asamblea de circuito 2024-2025\n(Con el superitendente de circuito).\n\n'Pórtense de una manera digna\nde las buenas noticias'")
                        self.pantalla.config(state = "disabled")
                        self.listbox_acomodadores.delete(0, END)
                        self.listbox_vigilancia.delete(0, END)
                        self.boton_aleatorio_acom.configure(state = "disabled")
                        self.boton_reiniciar_acom.configure(state = "disabled")
                        self.boton_remover_acom.configure(state = "disabled")
                        self.boton_aleatorio_vil.configure(state = "disabled")
                        self.boton_reiniciar_vil.configure(state = "disabled")
                        self.boton_remover_vil.configure(state = "disabled")
                        self.remover_pantalla.configure(state = "disabled")

                    elif self.lista_semanas[self.indice] != self.semana_especial_2 :
                        self.reiniciar_acomodadores()
                        self.reiniciar_vigilancia()
                        self.boton_aleatorio_acom.configure(state = "normal")
                        self.boton_reiniciar_acom.configure(state = "normal")
                        self.boton_remover_acom.configure(state = "normal")
                        self.boton_aleatorio_vil.configure(state = "normal")
                        self.boton_reiniciar_vil.configure(state = "normal")
                        self.boton_remover_vil.configure(state = "normal")
                        self.remover_pantalla.configure(state = "normal")

                        for p in range (self.num_post_2) : 

                                    if self.lista_semanas[self.indice - p] == self.semana_especial_2 :

                                        if grupo == 1 : 

                                            grupo = grupo + 4

                                        else: 

                                            grupo = grupo - 1

                except : 


                    if grupo == 1 : 

                        grupo = grupo + 4

                    else: 
                        grupo = grupo - 1



            if grupo == 1:    


                self.pantalla.insert("2.0", f"Grupo: {grupo}\n\n")

                for z in self.grupo_1 : 
                   self.pantalla.insert("4.0",f"-{z}\n")
                self.pantalla.config(state = "disabled")


            elif grupo == 2 :

                self.pantalla.insert("2.0", f"Grupo: {grupo}\n\n")

                for z in self.grupo_2 : 
                   self.pantalla.insert("4.0",f"-{z}\n")
                self.pantalla.config(state = "disabled")


            elif grupo == 3 :

                self.pantalla.insert("2.0", f"Grupo: {grupo}\n\n")

                for z in self.grupo_3 : 
                   self.pantalla.insert("4.0",f"-{z}\n")
                self.pantalla.config(state = "disabled")


            elif grupo == 4 : 

                self.pantalla.insert("2.0", f"Grupo: {grupo}\n\n")

                for z in self.grupo_4 : 
                   self.pantalla.insert("4.0",f"-{z}\n")
                self.pantalla.config(state = "disabled")


            elif grupo == 5: 

                self.pantalla.insert("2.0", f"Grupo: {grupo}\n\n")

                for z in self.grupo_5 : 
                   self.pantalla.insert("4.0",f"-{z}\n")
                self.pantalla.config(state = "disabled")


            else: 

                messagebox.showerror("Error", "La cantidad de grupos son 5.\n\nPor favor, vuelve a intentarlo")
        
        except Exception as e : 
            messagebox.showerror("Error", f"Debe de haber por lo menos una semana seleccioanda para poder mostrarla.\n\nCausa: {e}")
                    

    def remover (self) : 

        try: 

            indice = 0
            indice_gral = 0
            for i in self.lista_asignada : 
                indice_gral = indice_gral + 1


            grupo = self.por_semana[self.indice]


            if grupo != self.por_semana[0] : 
            
                if grupo == self.por_semana[1]  :
                
                    grupo = self.por_semana[self.indice + 3]


                elif grupo == self.por_semana[2] : 
                
                    grupo = self.por_semana[self.indice + 1]


                elif grupo == self.por_semana[3] : 
                
                    grupo = self.por_semana[self.indice - 1]


                elif grupo == self.por_semana[4] : 
                
                    grupo = self.por_semana[self.indice - 3]


                elif grupo == self.por_semana[0] : 
                
                    pass


                else :
                
                    print("Intente de nuevo.")



            if grupo == 1:    

                self.listbox_vigilancia.delete(0, END)
                eliminar_1 = list(set(self.lista_asignada) - (set(self.grupo_1)))
                eliminar_1.sort()

                for i in eliminar_1 : 
                    self.listbox_vigilancia.insert(indice, i)
                    indice = indice  + 1
                if len(eliminar_1) != len(self.lista_asignada) : 
                    union_1 = list(set(self.lista_asignada) & (set(self.grupo_1)))
                    for x in union_1 : 
                        self.lista_asignada.remove(x)


            elif grupo == 2 :

                self.listbox_vigilancia.delete(0, END)
                eliminar_2 = list(set(self.lista_asignada) - (set(self.grupo_2)))
                eliminar_2.sort()

                for i in eliminar_2 : 
                    self.listbox_vigilancia.insert(indice, i)
                    indice = indice  + 1
                if len(eliminar_2) != len(self.lista_asignada) : 
                    union_2 = list(set(self.lista_asignada) & (set(self.grupo_2)))
                    for x in union_2 : 
                        self.lista_asignada.remove(x)


            elif grupo == 3 :

                self.listbox_vigilancia.delete(0, END)
                eliminar_3 = list(set(self.lista_asignada) - (set(self.grupo_3)))
                eliminar_3.sort()

                for i in eliminar_3 : 
                    self.listbox_vigilancia.insert(indice, i)
                    indice = indice  + 1
                if len(eliminar_3) != len(self.lista_asignada) : 
                    union_3 = list(set(self.lista_asignada) & (set(self.grupo_3)))
                    for x in union_3 : 
                        self.lista_asignada.remove(x)


            elif grupo == 4 : 

                self.listbox_vigilancia.delete(0, END)
                eliminar_4 = list(set(self.lista_asignada) - (set(self.grupo_4)))
                eliminar_4.sort()

                for i in eliminar_4 : 
                    self.listbox_vigilancia.insert(indice, i)
                    indice = indice  + 1
                if len(eliminar_4) != len(self.lista_asignada) : 
                    union_4 = list(set(self.lista_asignada) & (set(self.grupo_4)))
                    for x in union_4 : 
                        self.lista_asignada.remove(x)


            elif grupo == 5: 

                self.listbox_vigilancia.delete(0, END)
                eliminar_5 = list(set(self.lista_asignada) - (set(self.grupo_5)))
                eliminar_5.sort()

                for i in eliminar_5 : 
                    self.listbox_vigilancia.insert(indice, i)
                    indice = indice  + 1
                if len(eliminar_5) != len(self.lista_asignada) : 
                    union_5 = list(set(self.lista_asignada) & (set(self.grupo_5)))
                    for x in union_5 : 
                        self.lista_asignada.remove(x)


            else: 

                messagebox.showerror("Error", "La cantidad de grupos son 5.\n\nPor favor, vuelve a intentarlo")


        except Exception as e: 

            messagebox.showerror("Error", f"Debe haber un grupo seleccionado para poder remover sus elementos.\nPor favor, intente de nuevo.\n\nMás informacion: {e}")


    #=============================================================================================
    #BOTÓN DE TREEVIEW
    
    def treeview_miercoles (self) :  

        try: 

            self.tree.insert("", "end", text=f"{self.lista_semanas[self.indice]}", values =(f"{self.lista_semanas[self.indice]}" ,f"{self.seleccion_acomodadores[0]} / {self.seleccion_acomodadores[1]}", 
                                    f"{self.seleccion_acomodadores[2]} / {self.seleccion_acomodadores[3]}", f"{self.seleccion_acomodadores[4]}" , f"{self.seleccion_vigilancia[0]}", f"{self.seleccion_vigilancia[1]}", f"{self.seleccion_vigilancia[2]}",f"Miércoles: {self.lista_miercoles[self.indice]}"))

        except Exception as e:
            messagebox.showerror("Error", f"Por favor, seleccione las listas y vuelve a intentarlo.\nError: {e}")

    def treeview_sabado (self) : 

        try: 

            self.tree.insert("", "end", text=f"{self.lista_semanas[self.indice]}", values =(f"{self.lista_semanas[self.indice]}", f"{self.seleccion_acomodadores[0]} / {self.seleccion_acomodadores[1]}", 
                                    f"{self.seleccion_acomodadores[2]} / {self.seleccion_acomodadores[3]}", f"{self.seleccion_acomodadores[4]}" ,f"{self.seleccion_vigilancia[0]}", f"{self.seleccion_vigilancia[1]}", f"{self.seleccion_vigilancia[2]}",f"Sábado: {self.lista_sabado[self.indice]}"))
    
        except Exception as e:
            messagebox.showerror("Error", f"Por favor, seleccione las listas y vuelve a intentarlo.\nError: {e}")
    
    #=============================================================================================
    #PARTE FINAL

    def final (self) : 

        self.texto_limpieza()
        self.botones_ventana()
        self.lista_acomodadores()
        self.botonnes_acomodadores()
        self.lista_vigilancia()
        self.botones_vigilancia()
        self.semanas()
        self.lista_fechas()
        self.botones()
        self.treeview()
    


if __name__ == '__main__' :

    objeto = Asignaciones ()
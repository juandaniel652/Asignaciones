import random
import tkinter as tk 
from tkinter import ttk, END, font, PhotoImage, messagebox, Text, Toplevel, LEFT, Menu
from PIL import Image
import locale
import datetime
import sqlite3 as sql
import Seccion_acomodadores
import Seccion_vigilancia
import Seccion_fechas
import Seccion_treeview
import Seccion_base_datos
import Fondos 
import platform
from actualizaciones.comprobaciones import verificar_actualizacion

class Aplicacion : 

    def __init__ (self) : 

    #WIDGETS GENERLES

        self.root = tk.Tk()
        self.root.title("Asignaciones")
        self.root.resizable(True, True)
        self.root.config(background = "#1E1E1E")

        pestanas = ttk.Notebook(self.root)
        pestanas.pack(fill="both", expand=True)
        
        self.pagina_1 = tk.Frame(pestanas)
        self.pagina_2 = tk.Frame(pestanas)

        self.pagina_1.config(bg = "#1E1E1E", highlightbackground = "#1E1E1E", relief = "ridge")
        self.pagina_2.config(bg = "#1E1E1E", highlightbackground = "#1E1E1E", relief = "ridge")
        
        pestanas.add(self.pagina_1, text="Ingreso")
        pestanas.add(self.pagina_2, text="Historial")

        self.diseño_titulo = font.Font(size = 15, family = "bold")
        self.diseño_de_listbox = font.Font(size = 10, family = "Italic")

        self.titulo_acomodadores = tk.Label(self.pagina_1, text = "Acomodadores" ,fg = "#E0E0E0", relief = "solid", font = self.diseño_titulo, background = "#333333")
        self.titulo_vigilancia = tk.Label(self.pagina_1, text = "Vigilancia" ,fg = "#E0E0E0", relief = "solid",font = self.diseño_titulo, background = "#333333")
        self.titulo_fecha = tk.Label(self.pagina_1, text = "Semanas", fg = "#E0E0E0", relief = "solid", font = self.diseño_titulo, background = "#333333")
        self.titulo_limpieza = tk.Label(self.pagina_1, text = "Limpieza", fg = "#E0E0E0", relief = "solid", font = self.diseño_titulo, background=  "#333333")

        self.listbox_acomodadores = tk.Listbox(self.pagina_1, relief = "raised", font = self.diseño_de_listbox, foreground = "#E0E0E0", background = "#424242")
        self.listbox_vigilancia = tk.Listbox(self.pagina_1, relief = "raised", font = self.diseño_de_listbox, foreground = "#E0E0E0", background = "#424242")
        self.listbox_de_fechas = tk.Listbox(self.pagina_1, relief = "raised", font = self.diseño_de_listbox, foreground = "#E0E0E0", background = "#424242", width = 30)

        self.validar_iconos_segun_sistema()
        
        self.final()
        
    #==================================================================================================  
    

    def iniciar_programa (self) : 

        self.root.mainloop()


    #FECHA ACTUAL

    def actualizar_reloj (self):

        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.etiqueta_reloj = tk.Label(self.pagina_1, text = hora_actual, font = ("Arial", 22), fg = "#E0E0E0", bg = "#333333", relief = "solid")
        self.etiqueta_reloj.grid(column = 4, columnspan = 6 , row = 0)

        self.root.after(1000, self.actualizar_reloj)
        
    
    def validar_iconos_segun_sistema (self) : 


        if platform.system() == "Windows" :
            
            self.root.iconbitmap("Programa/img/cuaderno.ico")
            
        else :
            
            icon = tk.PhotoImage(file="Programa/img/cuaderno.png")
            self.root.iconphoto(True, icon)
            
    
#==================================================================================================

    #Actualizaciones
    
    def corroborar_actualizaciones (self) : 
        
        try : 
        
            actualizacion, nueva_version = verificar_actualizacion()

            if not actualizacion:
            
                pass
            
            messagebox.showinfo("Actualización disponible", f"Hay una nueva versión disponible ({nueva_version}). Por favor, visite el repositorio para descargarla.")


        except Exception as error: 
            
            print("Error al comprobar actualizaciones:", error)
    
#==================================================================================================  

    #BOTONES VENTANA: opciones generales
    #WIDGETS
    
    def botones_ventana (self) : 

        boton_oscuro = tk.Button(self.pagina_1, text = "Modo Oscuro", command = self.fondo_defecto) 
        boton_claro = tk.Button(self.pagina_1, text = "Modo Claro", command = self.fondo_claro)
        
        self.boton_entresemana = tk.Button(self.pagina_1, text = "Entre semana", command = self.treeview_entre_semana) 
        self.boton_fin_de_semana = tk.Button(self.pagina_1, text = "Fin de semana", command = self.treeview_fin_semana)
        
        boton_salir = tk.Button(self.pagina_1, text = "Salir", command = self.salir)
        
        botones = [boton_oscuro, boton_claro, self.boton_entresemana, self.boton_fin_de_semana, boton_salir]
        
        for columna, boton in enumerate (botones) : 

            boton.grid (column = columna, row = 7) 
            boton.config(background = "#1976D2", foreground = "white", relief = "groove",activebackground= "gray95", activeforeground = "#333333")

#==================================================================================================
    #SECCIÓN: Treeview

    def creacion_treeview (self) :

        self.treeview = ttk.Treeview(self.pagina_1, columns=("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora", "Acomodador final" ,"Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia final", "Dias de reunión"), show='headings')
        Seccion_treeview.creacion_tabla(self.treeview)
        self.treeview.bind("<Double-1>", self.editar_celdas)

        # 🧪 Estilo moderno
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="#2b2b2b",  # fondo filas
                        foreground="white",    # texto
                        rowheight=20,
                        fieldbackground="#2b2b2b",
                        font=("Segoe UI", 10))

        style.configure("Treeview.Heading",
                        background="#1f1f1f",  # fondo encabezado
                        foreground="white",
                        font=("Segoe UI", 9, "bold"))

        style.map("Treeview",
                  background=[("selected", "#3a7ff6")],
                  foreground=[("selected", "white")])

        
    def editar_celdas (self, event) : 

        Seccion_treeview.editar_tabla(event, self.treeview, self.pagina_1, self.lista_acomodadores, self.lista_vigilancia, self.lista_semanas_totales, 
                                    self.lista_miercoles, self.lista_domingo, self.semanas_especiales, self.dias_totales_de_semanas, self.fechas_especiales_de_asamblea, 
                                    self.lista_martes, self.lista_sabado, self.dias_de_reuniones_especiales_entre_semana, self.dias_de_reuniones_especiales_fin_de_semana)
        
#==================================================================================================

    #SECCIÓN: Acomodadores
    #WIDGETS

    def widgets_acomodadores (self) : 

        self.lista_acomodadores = ['Altamirano Elias', 'Altamirano Martin' ,'Altamirano Horacio', 'Dominguez Joel', 
                                'Encina Gerardo', 'Ferreira David', 'Gracia Enrique', 
                                'Israelson Fernando', 'Ontiveros Juan', 'Ortiz Aureliano', 
                                'Valiente Walter', 'Viera Cristian']

        Seccion_acomodadores.ordenamiento(self.lista_acomodadores, self.listbox_acomodadores)
        self.titulo_acomodadores.grid(row = 0, column = 0)
        self.listbox_acomodadores.grid(row = 1, column = 0)

    
    def botones_acomodadores (self) :

        lista_boton = []

        boton_remover_acomodadores = tk.Button(self.pagina_1 , text = "Remover", command = self.remover_acomodadores); boton_aleatorio_acomodadores = tk.Button(self.pagina_1, text = "Seleccion aleatoria", command = self.aleatorio_acomodadores)
        boton_reiniciar_acomodadores = tk.Button(self.pagina_1, text = "Reiniciar", command = self.reiniciar_acomodadores)

        botones = [boton_remover_acomodadores, boton_aleatorio_acomodadores, boton_reiniciar_acomodadores]
        
        for numero, boton in enumerate (botones) : 
            largo = len(botones) + (numero - 1)
            boton.grid(column = 0, row = largo); 
            boton.config(relief = "groove" , background = "#1976D2", foreground = "white")
            lista_boton.append(boton)

        return lista_boton
    
#==================================================================================================

    #SECCIÓN: Vigilancia
    #WIDGETS

    def widgets_vigilancia (self) : 

        self.lista_vigilancia = ['Altamirano Maia', 'Altamirano Pamela', 'Arguello Monica', 
                                'Benitez Gabriela', 'Cardozo Karolaine', 'Carena Graciela', 
                                'Coronel Vanesa', 'Deiana Ruth', 'Dominguez Alejandra', 
                                'Dominguez Miriam', 'Encina Mónica', 'Ferreira Rocio', 
                                'Gomez Yanina', 'Gonzalez Iris', 'Israelson Analia', 
                                'Ledesma Susana', 'Quiroz Rosario', 'Sotelo Rosa', 
                                'Valiente Fátima', 'Valiente Silvia', 'Viera Valeria']
        
        Seccion_vigilancia.ordenamiento(self.lista_vigilancia, self.listbox_vigilancia)
    
        self.titulo_vigilancia.grid(column = 1, row = 0)
        self.listbox_vigilancia.grid(column = 1, row = 1)

        self.grupo_1 = ["Ferreira Rocio", "Gomez Yanina", "Israelson Analia", "Valiente Silvia"]
        self.grupo_2 = ["Coronel Vanesa", "Dominguez Alejandra", "Quiroz Rosario"]
        self.grupo_3 = ["Altamirano Maia", "Altamirano Pamela", "Cardozo Karolaine", "Gonzalez Iris"]
        self.grupo_4 = ["Carena Graciela", "Deiana Ruth", "Valiente Fátima"]
        self.grupo_5 = ["Dominguez Miriam", "Encina Mónica", "Viera Valeria"]
        self.grupo_6 = ["Arguello Monica", "Benitez Gabriela", "Ledesma Susana", "Sotelo Rosa"]


    def botones_vigilancia (self) : 

        lista_botones = []

        boton_remover_vigilancia = tk.Button(self.pagina_1, text = "Remover", command = self.remover_vigilancia); boton_aleatorio_vigilancia = tk.Button(self.pagina_1, text = "Seleccion aleatoria", command = self.aleatorio_vigilancia)
        boton_reiniciar_vigilancia = tk.Button(self.pagina_1, text = "Reiniciar", command = self.reiniciar_vigilancia)

        botones = [boton_remover_vigilancia, boton_aleatorio_vigilancia, boton_reiniciar_vigilancia]

        for numero, boton in enumerate (botones) : 

            largo = len(botones) + (numero - 1); 
            boton.grid(column = 1, row = largo); 
            boton.config(relief = "groove" ,background = "#1976D2", foreground = "white")
            lista_botones.append(boton)

        return lista_botones

    #==================================================================================================

    #SECCIÓN: Fecha
    #WIDGETS

    def recorrer_semanas (self) : 

        #Ubica en español el nombre del mes
        locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
        lista_de_numero_de_los_grupos_de_limpieza = [6, 5, 4, 3, 2, 1]

        #Fechas
        fecha = datetime.datetime.now().date()
        self.fechas_especiales_de_asamblea = [datetime.date(2025, 4, 27), datetime.date(2025, 10, 31)]
        nombre_de_eventos = ["Asamblea de circuito 2024-2025\n(Con el representante de la sucursal)\n\n'No nos avergonzamos\nde las buenas noticias'. (Rom. 1:16)",
                            "Asamblea Regional 2025\n\n         Adoración Pura\n(Mat. 4:10; Juan. 2:17; Juan. 4:23)"]

        dias_de_reuniones_especiales_entre_semana = [datetime.date(2025, 7, 7)]
        dias_de_reuniones_especiales_fin_de_semana = []

        dias_especiales_formato_estandar_entre_semana = Seccion_fechas.convertir_fechas_entre_semana_especiales_a_formato_estandar(dias_de_reuniones_especiales_entre_semana)
        dias_especiales_formato_estandar_fin_de_semana = Seccion_fechas.convertir_fechas_fin_de_semana_especiales_a_formato_estandar(dias_de_reuniones_especiales_fin_de_semana)

        self.dias_de_reuniones_especiales_entre_semana = dias_especiales_formato_estandar_entre_semana
        self.dias_de_reuniones_especiales_fin_de_semana = dias_especiales_formato_estandar_fin_de_semana

        #Logro que en cualquier dia actual se coloque como lunes
        funcion_lunes = Seccion_fechas.buscar_lunes(fecha)

        #El retorno = [0]. semanas totales, [1]. Contiene miércoles, [2]. Contiene domingo, [3]. lista_lunes, [4]. numero_semanas, [5]. Distancia final
        #[6]. Lista Martes, [7]. lIsta Sábado
        tipos_de_fechas = Seccion_fechas.renovar_semanas(funcion_lunes)
        
        self.lista_semanas_totales = tipos_de_fechas[0]
        self.lista_miercoles = tipos_de_fechas[1]
        self.lista_domingo = tipos_de_fechas[2]
        lista_lunes = tipos_de_fechas[3]
        numero_total_de_semanas = tipos_de_fechas[4]
        distancia_final = tipos_de_fechas[5]
        self.lista_martes = tipos_de_fechas[6]
        self.lista_sabado = tipos_de_fechas[7] 

        #Buscar dias de reuniones especiales (dias distintos)

        #ENTRESEMANA
        self.semanas_de_reuniones_especiales_entre_semana = Seccion_fechas.buscar_dias_de_reuniones_especiales(lista_lunes, self.lista_semanas_totales, self.dias_de_reuniones_especiales_entre_semana)

        #FIN DE SEMANA
        self.semanas_de_reuniones_especiales_fin_de_semana = Seccion_fechas.buscar_dias_de_reuniones_especiales(lista_lunes, self.lista_semanas_totales, self.dias_de_reuniones_especiales_fin_de_semana)

        #Encontrar semanas especiales
        semanas_especiales = Seccion_fechas.encontrar_semanas_especiales(lista_lunes, self.fechas_especiales_de_asamblea, self.lista_semanas_totales)
        self.semanas_especiales = semanas_especiales[0]
        self.dias_totales_de_semanas = semanas_especiales[1]
        funcion_distacia_entre_fechas_especiales = Seccion_fechas.calcular_distancia_fechas_especiales(self.dias_totales_de_semanas, self.fechas_especiales_de_asamblea, nombre_de_eventos)

        self.distancia_de_semanas_especiales = funcion_distacia_entre_fechas_especiales[0]
        self.nombre_eventos_actualizados = funcion_distacia_entre_fechas_especiales[1]

        #Multiplico el ciclo de grupos recorrido (De esa manera, por cada semana está el ciclo adecuado de grupos)
        #Debe ser Domingo para que no haya cambios durante la semana
        fecha_final_grupos = datetime.date(2033, 1, 30)
        diferencia_grupos = fecha_final_grupos - fecha
        dias_a_semanas_grupos = diferencia_grupos.days // 7
        grupos_ordenados_por_semanas = dias_a_semanas_grupos
        
        self.sucesion_grupos = []
        self.sucesion_grupos = lista_de_numero_de_los_grupos_de_limpieza[:] * numero_total_de_semanas
        
        for numero_semanas in range(grupos_ordenados_por_semanas) : 

            self.sucesion_grupos = self.sucesion_grupos [1:] + self.sucesion_grupos [:1]

        return self.lista_semanas_totales


    def lista_acomodadores_fechas (self) : 

        indice = 0
        for fechas in self.lista_semanas_totales : 
            self.listbox_de_fechas.insert(indice, fechas)
            indice = indice  + 1
        self.titulo_fecha.grid(column = 2, row = 0)
        self.listbox_de_fechas.grid(column = 2, row = 1)


    def botones_semanas (self) : 
        
        mostrar = tk.Button(self.pagina_1, text = "Mostrar", relief = "groove", background = "#1976D2", foreground = "white", command = self.mostrar_semanas_en_caja)
        mostrar.grid(column = 2, row = 2)

        self.boton_remover_pantalla = tk.Button(self.pagina_1, text = "Remover", relief = "groove", background = "#1976D2", foreground = "white", command = self.remover)
        self.boton_remover_pantalla.grid(column = 3, row = 2)

        boton_base_datos = tk.Button(self.pagina_1, text = "Guardar datos", relief = "groove", background = "#1976D2", foreground = "white", command = self.transportar_datos_a_base)
        boton_base_datos.grid(column = 3, row = 3)

            
    def texto_limpieza (self) : 

        self.pantalla_semanas = Text(self.pagina_1); self.pantalla_semanas.grid(column = 3, row = 1, pady = 15)
        self.pantalla_semanas.config(state = "disabled", width = 38, height = 11, foreground = "#E0E0E0", background = "#424242")
        self.titulo_limpieza.grid(column = 3, row = 0)

    #============================FUNCIONALIDAD==============================================

    #BOTONES GENERALES

    def fondo_defecto (self) : 

        Fondos.oscuro(self.root, self.pagina_1, self.pagina_2, self.titulo_acomodadores, self.titulo_vigilancia, self.titulo_fecha, 
        self.titulo_limpieza, self.listbox_acomodadores, self.listbox_vigilancia, self.listbox_de_fechas, self.pantalla_semanas)
        
    def fondo_claro (self) : 

        Fondos.claro(self.root, self.pagina_1, self.pagina_2, self.titulo_acomodadores, self.titulo_vigilancia, self.titulo_fecha, 
        self.titulo_limpieza, self.listbox_acomodadores, self.listbox_vigilancia, self.listbox_de_fechas, self.pantalla_semanas)

    def salir (self) : 

        self.root.quit()

    #=============================================================================================

    #BOTONES ACOMODADORES

    def remover_acomodadores (self): 

        seleccion = self.listbox_acomodadores.curselection()
        indice = 0
        if seleccion : 
            self.listbox_acomodadores.delete(seleccion[indice])
            del self.lista_acomodadores [seleccion[indice]]


    def aleatorio_acomodadores (self) : 

        try : 
            self.seleccion_acomodadores = random.sample(self.lista_acomodadores, 5)
            messagebox.showinfo("Seleccionado", f"""Acomodadores 1° hora: {self.seleccion_acomodadores[0]} / {self.seleccion_acomodadores [1]}\n\nAcomodadores 2° hora: {self.seleccion_acomodadores[2]} / {self.seleccion_acomodadores[3]}\n\nAcomodador después de la reunión: {self.seleccion_acomodadores[4]}""")

        except Exception as e : 
            messagebox.showerror("Error",f"Debe haber un mínimo de 5 opciones\nCausa: {e}")


    def reiniciar_acomodadores (self) : 

        self.listbox_acomodadores.delete(0, END)
        self.widgets_acomodadores()
    
    #=============================================================================================

    #BOTONES VIGILANCIA

    def remover_vigilancia (self): 

        seleccion = self.listbox_vigilancia.curselection()
        indice = 0
        if seleccion : 
            self.listbox_vigilancia.delete(seleccion[indice])
            del self.lista_vigilancia [seleccion[indice]]
            

    def aleatorio_vigilancia (self) : 

        try : 
            self.seleccion_vigilancia = random.sample(self.lista_vigilancia, 3)
            messagebox.showinfo("Seleccionado", f"""Vigilancia 1° hora: {self.seleccion_vigilancia[0]}\n\nVigilancia 2° hora: {self.seleccion_vigilancia[1]}\n\nVigilancia después de la reunión: {self.seleccion_vigilancia[2]}""")
        
        except Exception as e : 
            messagebox.showerror("Error",f"Debe haber un mínimo de 3 opciones\nCausa: {e}")


    def reiniciar_vigilancia (self) : 

        self.listbox_vigilancia.delete(0, END)
        self.widgets_vigilancia()


    #=============================================================================================
    #BOTONES FECHAS

    def mostrar_semanas_en_caja (self) : 

        try:

            botones_acomodadores = self.botones_acomodadores()
            botones_vigilancia = self.botones_vigilancia()
            self.boton_entresemana.config(state = "normal")
            self.boton_fin_de_semana.config(state = "normal")

            seleccion_de_la_semana = self.listbox_de_fechas.curselection()
            self.indice = 0

            for self.indice in seleccion_de_la_semana : 

                if seleccion_de_la_semana : 
                    
                    grupos = self.sucesion_grupos[self.indice]

                    funcion_buscar_grupos_por_semana = Seccion_fechas.buscar_grupos_por_semana(grupos, self.sucesion_grupos, self.indice)
                    messagebox.showinfo("Seleccionado", f"Semana seleccionada: {self.lista_semanas_totales[self.indice]}") 
                    self.pantalla_semanas.config(state = "normal")
                    self.pantalla_semanas.delete("1.0", END)
                    self.pantalla_semanas.insert("1.0", f"{self.lista_semanas_totales[self.indice]}\n")
                    self.reiniciar_acomodadores(); self.reiniciar_vigilancia(); self.boton_remover_pantalla.configure(state = "normal")

                    self.funcion_fechas_en_pantalla = None
                    funcion_reubicar_grupos = None

                    for semana_especial in range (len(self.semanas_especiales)) : 

                        if not self.lista_semanas_totales[self.indice] == self.semanas_especiales[semana_especial]: 

                            funcion_reubicar_grupos = Seccion_fechas.reubicar_grupos_desde_semanas_especiales(self.distancia_de_semanas_especiales, 
                                                    self.semanas_especiales, self.lista_semanas_totales, self.indice, funcion_buscar_grupos_por_semana)

                            if not funcion_reubicar_grupos == None: 

                                self.funcion_fechas_en_pantalla = Seccion_fechas.mostrar_grupos_en_pantalla(funcion_reubicar_grupos, self.pantalla_semanas, 
                                                                    self.grupo_1, self.grupo_2, self.grupo_3, self.grupo_4, self.grupo_5, self.grupo_6)
                                
                            else: 

                                self.funcion_fechas_en_pantalla = Seccion_fechas.mostrar_grupos_en_pantalla(funcion_buscar_grupos_por_semana, self.pantalla_semanas, 
                                                                    self.grupo_1, self.grupo_2, self.grupo_3, self.grupo_4, self.grupo_5, self.grupo_6)

                        else:

                            funcion_fecha_especial = Seccion_fechas.fechas_especiales_en_caja(self.nombre_eventos_actualizados, self.semanas_especiales, self.lista_semanas_totales, 
                            self.indice, self.pantalla_semanas, self.boton_remover_pantalla, self.listbox_acomodadores, self.listbox_vigilancia, 
                            botones_acomodadores, botones_vigilancia, self.boton_entresemana, self.boton_fin_de_semana)
                            
        except Exception as e : 
            messagebox.showerror("Error", f"Debe de haber por lo menos una semana seleccioanda para poder mostrarla.\n\nCausa: {e}")
        

    def remover (self) : 

        try : 
            numero_grupo = Seccion_fechas.mostrar_grupos_en_pantalla(self.funcion_fechas_en_pantalla, self.pantalla_semanas, self.grupo_1, self.grupo_2, self.grupo_3, self.grupo_4, self.grupo_5, self.grupo_6) 
            funcion_remover_desde_grupos = Seccion_fechas.remover_desde_grupos(numero_grupo, self.lista_vigilancia, self.listbox_vigilancia,self.grupo_1, self.grupo_2, self.grupo_3, self.grupo_4, self.grupo_5, self.grupo_6)

        except Exception as e : 
            messagebox.showerror("Error", f"Debe de haber por lo menos una semana seleccioanda para poder mostrarla y luego removerla.\n\nCausa: {e}")


    def transportar_datos_a_base (self) : 

        try : 

            valores = []
            for item in self.treeview.get_children():
                valores.append(self.treeview.item(item, "values"))

            guardar_valores_base_datos = Seccion_base_datos.creacion_base_datos()
            insertar_valores_base_datos = Seccion_base_datos.insertar_valores(guardar_valores_base_datos, valores, self.funcion_fechas_en_pantalla)

            messagebox.showinfo("Información", "Los datos han sido guardados exitosamente")
        
        except Exception as error: 

            messagebox.showerror("Error", f"No ha sido pisble guardar en la base de de datos.\nPor favor, intente nuevamente\n\nError = {error}")
        

    #=============================================================================================
    #BOTÓN DE TREEVIEW DE LA PRIMERA PÁGINA
    
    def treeview_entre_semana (self) :  

        try : 

            valores_treeview_entresemana = self.treeview.insert("", "end", text=f"{self.lista_semanas_totales[self.indice]}", values = (f"{self.lista_semanas_totales[self.indice]}" ,f"{self.seleccion_acomodadores[0]} / {self.seleccion_acomodadores[1]}", 
                                    f"{self.seleccion_acomodadores[2]} / {self.seleccion_acomodadores[3]}", f"{self.seleccion_acomodadores[4]}" , f"{self.seleccion_vigilancia[0]}", f"{self.seleccion_vigilancia[1]}", f"{self.seleccion_vigilancia[2]}",f"Miércoles {self.lista_miercoles[self.indice]}"))

            for reunion_especial in range (len(self.semanas_de_reuniones_especiales_entre_semana)) :            

                if self.semanas_de_reuniones_especiales_entre_semana[reunion_especial] == self.lista_semanas_totales[self.indice] :
                    
                
                    item_id = valores_treeview_entresemana
                    valores_actuales = self.treeview.item(item_id, "values")
                    valores_lista = list(valores_actuales)
                    valores_lista[7] = f"Martes {self.lista_martes[self.indice]}"
                    self.treeview.item(item_id, values = tuple(valores_lista))

            return valores_treeview_entresemana

        except Exception as e:
            messagebox.showerror("Error", f"Por favor, seleccione a los Acomodadores/Vigilancia o Semanas y vuelve a intentarlo.\n\nError: {e}")


    def treeview_fin_semana (self) : 

        try : 
            
            valores_treeview_fin_de_semana = self.treeview.insert("", "end", text=f"{self.lista_semanas_totales[self.indice]}", values =(f"{self.lista_semanas_totales[self.indice]}", f"{self.seleccion_acomodadores[0]} / {self.seleccion_acomodadores[1]}", 
                    f"{self.seleccion_acomodadores[2]} / {self.seleccion_acomodadores[3]}", f"{self.seleccion_acomodadores[4]}" ,f"{self.seleccion_vigilancia[0]}", f"{self.seleccion_vigilancia[1]}", f"{self.seleccion_vigilancia[2]}",f"Domingo {self.lista_domingo[self.indice]}"))
            
            for reunion_especial in range (len(self.semanas_de_reuniones_especiales_fin_de_semana)) :
                
                if self.semanas_de_reuniones_especiales_fin_de_semana[reunion_especial] == self.lista_semanas_totales[self.indice] :

                    item_id = valores_treeview_fin_de_semana
                    valores_actuales = self.treeview.item(item_id, "values")

                    valores_lista = list(valores_actuales)
                    valores_lista[7] = f"Sabado {self.lista_sabado[self.indice]}" 

                    self.treeview.item(item_id, values = tuple(valores_lista))

            return valores_treeview_fin_de_semana
        
        except Exception as e:

            messagebox.showerror("Error", f"Por favor, seleccione a los Acomodadores/Vigilancia o Semanas y vuelve a intentarlo.\n\nError: {e}")
    

    #=============================================================================================
    #WIDGETS DE SEGUNDA PESTAÑA

    def crear_widgets_segunda_pestaña (self) : 

        self.tiutlo_de_las_listas = tk.Label(self.pagina_2, text = "LISTA GENERAL" , fg = "#333333", relief = "solid", font = self.diseño_titulo, foreground = "#E0E0E0", background = "#333333")

        self.entrada_de_seleccion_de_lista = ttk.Combobox(self.pagina_2, values=["Lista General", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                                                                                "Noviembre", "Diciembre"], state="readonly")
        
        valor_del_item = tk.IntVar()
        checkbox = tk.Checkbutton(self.pagina_2, text = "Convertir", font = self.diseño_de_listbox, variable = valor_del_item, command = self.convertir_a_documentos_por_meses)

        self.tiutlo_de_las_listas.grid(column = 2, row = 0)
        self.entrada_de_seleccion_de_lista.grid(column = 2, row = 3, pady = 20)
        checkbox.grid(row = 4, column = 2)
        
        self.entrada_de_seleccion_de_lista.current(0) 
        self.entrada_de_seleccion_de_lista.bind("<<ComboboxSelected>>", self.cambiar_pestana_segun_tipo_de_lista)

    #=============================================================================================
    #BOTONES DE SEGUNDA PESTAÑA (CONVERTIR A WORD, PDF, EXCEL, TRANSPORTAR DATOS A APP MÓVIL)

    def crear_botones_de_interaccion (self) : 

        boton_word = tk.Button(self.pagina_2, text = "Convertir a Word General", command = self.convertir_word)
        boton_excel = tk.Button(self.pagina_2, text = "Convertir a Excel General", command = self.convertir_excel)
        boton_mostrar_lista = tk.Button(self.pagina_2, text = "Mostrar Asignados Totales", command = self.mostrar_asignados)
        boton_pdf = tk.Button(self.pagina_2, text = "Convertir a PDF General", command = self.convertir_pdf)
        boton_movil = tk.Button(self.pagina_2, text = "Convertir Datos a Aplicación Móvil", command = self.transportar_datos_a_aplicacion_movil)

        botones = [boton_word, boton_excel, boton_mostrar_lista , boton_pdf, boton_movil]
        
        for boton in range (len(botones)) : 

            botones[boton].grid (column = boton, row = 2); botones[boton].config(background = "#1976D2", foreground = "white", relief = "groove",activebackground="gray95",activeforeground = "#333333")

    #=============================================================================================
    #FUNCIONALIDAD DE LOS BOTONES (SEGUNDA PESTAÑA)

    def convertir_word (self) : 

        funcion_word = Seccion_base_datos.pasar_datos_word()
        messagebox.showinfo("Información", "Los datos han sido convertidos a Word exitosamente")
        

    def convertir_excel (self) : 

        try : 

            funcion_excel = Seccion_base_datos.pasar_datos_excel()
            messagebox.showinfo("Información", "Los datos han sido convertidos a Excel exitosamente")
        
        except: 

            messagebox.showerror("Error", "Se produjo un incoveniente al intentar convertir los datos a Excel.\n\nPor favor, guarde los datos e intente de nuevo.")
    

    def mostrar_asignados (self) : 

        try : 
            
            datos_almacenados = Seccion_base_datos.recopilar_datos_almacenados()
            muestra_de_datos = Seccion_base_datos.mostrar_datos_en_treeview(self.treeview_de_segunda_pestaña, datos_almacenados)

        except Exception as error: 

            messagebox.showerror("Error", f"No ha sido posible mostrar las asignaciones.\n\nPor favor, guarde los datos e intente de nuevo.\n{error}")


    def convertir_pdf (self) :

        try: 
        
            funcion_pdf = Seccion_base_datos.pasar_datos_pdf()
            messagebox.showinfo("Información", "Los datos han sido convertidos a PDF exitosamente.")

        except : 

            messagebox.showerror("Error", "Se produjo un incoveniente al intentar convertir los datos a PDF.\n\nPor favor, guarde los datos e intente de nuevo.")


    def convertir_a_documentos_por_meses (self) :

        ventana_emergente = tk.Toplevel(self.pagina_2)
        ventana_emergente.title("Selecciona el tipo de convertor")
        ventana_emergente.geometry("330x250")
        ventana_emergente.resizable(False, False) 
        ventana_emergente.wm_maxsize(400, 300) 
        ventana_emergente.wm_attributes("-topmost", True)

        nombre_del_mes_seleccioando = self.entrada_de_seleccion_de_lista.get()
        numero_del_mes_seleccionado = self.entrada_de_seleccion_de_lista.current()

        etiqueta_consulta = tk.Label(ventana_emergente, text = f"¿A que formato desea convertir\nlas asignaciones del mes de\n{nombre_del_mes_seleccioando}?\n\nWord (.docx) - PDF (.pdf) - Excel (.xlsx)", font=("Helvetica", 12, "bold"))
        etiqueta_consulta.pack(pady = 5)


        def convertir_datos_del_mes_por_word () :

            funcion_word_mes_especifico = Seccion_base_datos.convertir_datos_del_mes_por_word(numero_del_mes_seleccionado, nombre_del_mes_seleccioando)
            messagebox.showinfo("Información", "Los datos han sido convertidos a Word exitosamente")
            ventana_emergente.destroy()

        def convertir_datos_del_mes_por_pdf () :

            funcion_pdf_mes_especifico = Seccion_base_datos.convertir_datos_del_mes_por_pdf(nombre_del_mes_seleccioando)
            messagebox.showinfo("Información", "Los datos han sido convertidos a PDF exitosamente")
            ventana_emergente.destroy()

        def convertir_datos_del_mes_por_excel () : 

            funcion_excel_mes_especifico = Seccion_base_datos.convertir_datos_del_mes_por_excel(numero_del_mes_seleccionado, nombre_del_mes_seleccioando)
            messagebox.showinfo("Información", "Los datos han sido convertidos a Excel exitosamente")
            ventana_emergente.destroy()


        boton_word = tk.Button(ventana_emergente, text = "Word", background = "#1976D2", foreground = "white" , relief = "groove" , activebackground = "gray95" , activeforeground = "#333333" , border = 10, width = 10, command = convertir_datos_del_mes_por_word)
        boton_pdf = tk.Button(ventana_emergente, text = "PDF", background = "#1976D2", foreground = "white" , relief = "groove" , activebackground = "gray95" , activeforeground = "#333333" , border = 10, width = 10, command = convertir_datos_del_mes_por_pdf)
        boton_excel = tk.Button(ventana_emergente, text = "Excel", background = "#1976D2", foreground = "white" , relief = "groove" , activebackground = "gray95" , activeforeground = "#333333" , border = 10, width = 10, command = convertir_datos_del_mes_por_excel)

        boton_word.pack(side = LEFT, padx = 4)
        boton_pdf.pack(side = LEFT, padx = 4)
        boton_excel.pack(side = LEFT, padx = 4)


    def transportar_datos_a_aplicacion_movil (self) : 

        messagebox.showinfo("Información", "Estamos trabajando en la aplicación móvil para su respectiva\nutilización.\n\nPor favor, mantenga la aplicación actualizada para recibir\nnotificaciones de la misma.")


    #=============================================================================================
    #CREACIÓN DEL TREEVIEW CONTENEDOR DE LAS SEMANAS TOTALES (SEGUNDA PESTAÑA)

    def crear_lista_con_semanas_totales (self) : 

        self.treeview_de_segunda_pestaña = ttk.Treeview(self.pagina_2, columns=("Semanas", "Acomodadores 1° hora", "Acomodadores 2° hora", "Acomodador final" ,"Vigilancia 1° hora", "Vigilancia 2° hora","Vigilancia final", "Dias de reunión"), show='headings')
        Seccion_treeview.creacion_tabla(self.treeview_de_segunda_pestaña)
        self.treeview_de_segunda_pestaña.grid(column = 0, columnspan = 5 , row = 1)
        self.treeview_de_segunda_pestaña.configure(height = 25)


    def mostrar_lista_con_semanas_totales_por_meses (self) :

        indice_seleccionado = self.entrada_de_seleccion_de_lista.current() 

        Seccion_base_datos.mostrar_asignaciones_por_mes_seleccionado(self.treeview_de_segunda_pestaña, indice_seleccionado)

    #=============================================================================================
    #TIPOS DE LISTAS (APARTE DE LA GENERAL, OTRA CON LOS MESES)

    def cambiar_pestana_segun_tipo_de_lista (self, event) : 

        indice_seleccionado = self.entrada_de_seleccion_de_lista.current()
        self.treeview_de_segunda_pestaña.delete(*self.treeview_de_segunda_pestaña.get_children())
        meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        
        if indice_seleccionado == 0 : 
            
            self.tiutlo_de_las_listas.destroy()
            self.tiutlo_de_las_listas = tk.Label(self.pagina_2, text = "LISTA GENERAL" , foreground = "#E0E0E0", background = "#333333", relief = "solid", font = self.diseño_titulo)
            self.tiutlo_de_las_listas.grid(column = 2, row = 0)
            self.treeview_de_segunda_pestaña.config(height = 25)
            self.mostrar_asignados()
        
        for numero, mes in enumerate (meses) : 

            if indice_seleccionado == mes :

                self.tiutlo_de_las_listas.destroy()
                self.tiutlo_de_las_listas = tk.Label(self.pagina_2, text = "LISTA POR MESES" , foreground = "#E0E0E0", background = "#333333", relief = "solid", font = self.diseño_titulo)
                self.tiutlo_de_las_listas.grid(column = 2, row = 0)
                self.treeview_de_segunda_pestaña.config(height = 17)
                funcion_mostrar_por_meses = self.mostrar_lista_con_semanas_totales_por_meses()
                return funcion_mostrar_por_meses

    
    #=============================================================================================
    #PARTE FINAL

    def final (self) : 

        self.actualizar_reloj()
        self.texto_limpieza()
        self.botones_ventana()
        self.widgets_acomodadores()
        self.botones_acomodadores()
        self.widgets_vigilancia()
        self.botones_vigilancia()
        self.recorrer_semanas()
        self.lista_acomodadores_fechas()
        self.botones_semanas()
        self.creacion_treeview()
        self.crear_widgets_segunda_pestaña()
        self.crear_lista_con_semanas_totales()
        self.crear_botones_de_interaccion()

if __name__ == '__main__' :

    objeto = Aplicacion ()
    objeto.iniciar_programa()
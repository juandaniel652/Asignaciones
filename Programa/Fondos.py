import tkinter as tk

def oscuro (root, pagina_1, pagina_2, titulo_acomodadores, titulo_vigilancia,
             titulo_fecha, titulo_limpieza, listbox_acomodadores, 
             listbox_vigilancia, caja, pantalla) : 

        root.config(background = "#1E1E1E")
        pagina_1.config(bg = "#1E1E1E", highlightbackground = "#1E1E1E", relief = "ridge")
        pagina_2.config(bg = "#1E1E1E", highlightbackground = "#1E1E1E", relief = "ridge")

        titulo_acomodadores.config(fg = "#E0E0E0", bg = "#333333")
        titulo_vigilancia.config(fg = "#E0E0E0", bg = "#333333")
        titulo_fecha.config(fg = "#E0E0E0", bg = "#333333")
        titulo_limpieza.config(fg = "#E0E0E0", bg = "#333333")

        listbox_acomodadores.config(fg = "#E0E0E0", bg = "#424242")
        listbox_vigilancia.config(fg = "#E0E0E0", bg = "#424242")
        caja.config(fg = "#E0E0E0", bg = "#424242")
        pantalla.config(fg = "#E0E0E0", bg = "#424242")
        

def claro (root,tab1, tab2, titulo_acomodadores, titulo_vigilancia, 
           titulo_fecha, titulo_limpieza, listbox_acomodadores, 
           listbox_vigilancia, caja, pantalla) : 

        root.configure(background = "#F5F5F5")
        tab1.config(bg = "#F5F5F5")
        tab2.config(bg = "#F5F5F5")

        titulo_acomodadores.config (fg = "#333333", bg = "white")
        titulo_vigilancia.config (fg = "#333333", bg = "white")
        titulo_fecha.config (fg = "#333333", bg = "white")
        titulo_limpieza.config (fg = "#333333", bg = "white")

        listbox_acomodadores.config(fg = "#333333", bg = "#D9E3F0")
        listbox_vigilancia.config(fg = "#333333", bg = "#D9E3F0")
        caja.config(fg = "#333333", bg = "#D9E3F0")
        pantalla.config(fg = "#333333", bg = "#D9E3F0")

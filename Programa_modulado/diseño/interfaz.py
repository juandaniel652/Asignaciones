import tkinter as tk
from diseño.icono.icono_aplicacion import IconoAplicacion
from diseño.fuentes.fuente import Fuentes
from diseño.pestanas import Pestanas
from diseño.titulos.titulo import Titulos
from diseño.listboxes.listbox import Listboxes
from diseño.reloj.reloj import Reloj
from diseño.boton_asignacion.boton_acomodador import BotonAcomodador
from diseño.boton_asignacion.boton_vigilancia import BotonVigilancia
from diseño.botones_generales.botones_generales import BotonesGenerales
from diseño.botones_semana.botones_semana import BotonesSemana
from diseño.treeview.treeview_personalizado import TreeviewPersonalizado
from diseño.tema.modo_tema import ModoTema
from diseño.caja_fecha.caja_fecha import CajaFecha


class Interfaz :

    def __init__ (self) :

        self.ventana = tk.Tk()
        self.ventana.title("Asignaciones")
        self.ventana.geometry("800x650")
        self.ventana.resizable(True, True)
        self.ventana.config(background="#1E1E1E")

        # Establecer el icono de la aplicación
        self.icono_aplicacion = IconoAplicacion(self.ventana, "Programa_modulado/imagenes/cuaderno.ico")

        # Crear fuentes
        self.fuentes = Fuentes()

        # Crear pestañas
        self.pestanas = Pestanas(self.ventana)
        self.pagina_1 = self.pestanas.pagina_1
        self.pagina_2 = self.pestanas.pagina_2

        # Crear títulos
        self.titulos = Titulos(self.pagina_1, self.fuentes.fuente_titulo)
        self._ubicar_titulos()

        # Crear listboxes
        self.listboxes = Listboxes(self.pagina_1, self.fuentes.fuente_listbox)
        self._ubicar_listboxes()
        self._ubicar_caja_fecha()

        # Configurar grid
        self._configurar_grid()

        # Crear reloj
        self.reloj = Reloj(self.pagina_1, self.fuentes.fuente_titulo)

        # Crear botones de asignación usando polimorfismo
        self.boton_acomodador = BotonAcomodador(self.pagina_1, self)
        self.boton_vigilancia = BotonVigilancia(self.pagina_1, self)

        # Crear botones de semana
        self.botones_semana = BotonesSemana(self.pagina_1, self)

        # Crear treeview
        self.treeview = TreeviewPersonalizado(self.pagina_1)

        # Crear botones generales
        self.botones_generales = BotonesGenerales(self.pagina_1, self)

        # Añadir clase de cambio de temas
        self.modo_tema = ModoTema(self)

    def _ubicar_titulos(self):
        titulos_grid = [
            (self.titulos.titulo_acomodadores, 0),
            (self.titulos.titulo_vigilancia, 1),
            (self.titulos.titulo_fecha, 2),
            (self.titulos.titulo_limpieza, 3),
        ]
        for widget, columnas in titulos_grid:
            widget.grid(row=0, column=columnas, padx=10, pady=10, sticky="ew")

    def _ubicar_listboxes(self):
        listboxes_grid = [
            (self.listboxes.listbox_acomodadores, 0),
            (self.listboxes.listbox_vigilancia, 1),
            (self.listboxes.listbox_de_fechas, 2),
        ]
        for widget, columnas in listboxes_grid:
            widget.grid(row=1, column=columnas, padx=10, pady=5, sticky="nsew")

    def _ubicar_caja_fecha(self):
        # Ubica el Text de la clase CajaFecha en la columna 3, fila 1
        self.caja_fecha = CajaFecha(self.pagina_1, self.fuentes.fuente_titulo)

    def _configurar_grid(self):
        for i in range(4):
            self.pagina_1.columnconfigure(i, weight=1)
        self.pagina_1.rowconfigure(0, weight=0)
        self.pagina_1.rowconfigure(1, weight=1)
        self.pagina_1.rowconfigure(2, weight=0)
        self.pagina_1.rowconfigure(3, weight=0)
        self.pagina_1.rowconfigure(4, weight=1)

    def iniciar_programa(self):
        self.ventana.mainloop()

        
if __name__ == "__main__":
    app = Interfaz()
    app.iniciar_programa()
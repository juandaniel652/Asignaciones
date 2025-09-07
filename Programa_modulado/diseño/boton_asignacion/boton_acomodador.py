from diseño.boton_asignacion.boton_asignacion import BotonAsignacion

class BotonAcomodador(BotonAsignacion):
    def __init__(self, parent, app):
        super().__init__(parent, app, columna=0, tipo="acomodadores")
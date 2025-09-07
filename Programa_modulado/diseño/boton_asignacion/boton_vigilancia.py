from diseño.boton_asignacion.boton_asignacion import BotonAsignacion

class BotonVigilancia(BotonAsignacion):
    def __init__(self, parent, app):
        super().__init__(parent, app, columna=1, tipo="vigilancia")
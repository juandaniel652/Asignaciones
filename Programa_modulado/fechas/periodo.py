import datetime
from fechas.semana import Semana

class Periodo :

    def __init__ (self, fecha_inicio: datetime.date) :

        self.fecha_inicio = fecha_inicio
        self.numero_grupo = 1  # Inicialmente 1


    def actualizar_numero_grupo (self, fecha_actual: datetime.date) :

        semana = Semana(fecha_actual)
        semanas_pasadas = semana.semanas_transcurridas(self.fecha_inicio)
        self.numero_grupo = (semanas_pasadas % 6) + 1  # Ciclo 1-6   

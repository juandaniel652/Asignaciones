import datetime
from typing import List, Optional

class SemanaEspecial :

    def __init__ (self, dia: datetime.date, semanas: List[datetime.date]) : 

        self.dia = dia
        self.semanas = semanas


    def verificar (self) -> bool :

        for semana in self.semanas :

            if (
                self.dia.isocalendar()[1] == semana.isocalendar()[1]
                and self.dia.year == semana.year
            ) :
                
                return True
            
        return False


    def obtener_semana_especial (self) -> Optional[str] :
    
        for semana in self.semanas :

            if (
            self.dia.isocalendar()[1] == semana.isocalendar()[1]
            and self.dia.year == semana.year
            ) :
                inicio = semana
                fin = inicio + datetime.timedelta(days = 6)

                if inicio.month != fin.month :

                    texto = (
                    f"Del {inicio.day} de {inicio.strftime('%B')} "
                    f"al {fin.day} de {fin.strftime('%B')} {fin.year}"
                    )

                else :

                    texto = (
                    f"Del {inicio.day} al {fin.day} de {fin.strftime('%B')} {fin.year}"
                    )
                
                return texto
            
        return None

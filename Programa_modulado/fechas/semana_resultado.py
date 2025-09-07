from dataclasses import dataclass
from typing import List, Optional
import datetime


@dataclass
class SemanaResultado :

    lista_semanas: List[str]
    lista_miercoles: List[str]
    lista_domingo: List[str]
    lista_lunes: List[datetime.date]
    total_semanas: int
    distancia_final: Optional[datetime.date]
    lista_martes: List[str]
    lista_sabado: List[str]
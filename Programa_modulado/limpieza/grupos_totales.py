from dataclasses import dataclass, field
from typing import List

@dataclass
class GruposTotales :

    grupo_1: List[str] = field(default_factory = list)
    grupo_2: List[str] = field(default_factory = list)
    grupo_3: List[str] = field(default_factory = list)
    grupo_4: List[str] = field(default_factory = list)
    grupo_5: List[str] = field(default_factory = list)
    grupo_6: List[str] = field(default_factory = list)


    def mostrar(self) :

        for indice, grupo in enumerate([
            self.grupo_1,
            self.grupo_2,
            self.grupo_3,
            self.grupo_4,
            self.grupo_5,
            self.grupo_6
        ], 1):
            
            pass
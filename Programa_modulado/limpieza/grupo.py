from limpieza.grupos_totales import GruposTotales
from fechas.periodo import Periodo
from typing import List

class Grupo:

    def __init__ (self, listado_total: List[str], periodo: Periodo) :

        self.listado_total = listado_total
        self.grupos = GruposTotales()
        self.periodo = periodo


    def validar_nombres (grupos_func) :

        def wrapper (self, *args, **kwargs) :

            grupos_asignados = grupos_func(self, *args, **kwargs)
            nombres_validos = set(self.listado_total)

            for grupo in grupos_asignados :

                for nombre in grupo :

                    if nombre not in nombres_validos :

                        raise ValueError(f"Nombre no válido en grupo: {nombre}")
                    
            return grupos_asignados
        
        return wrapper


    @validar_nombres
    def obtener_grupos_asignados (self) :

        return [
            ["Ferreira Rocio", "Gomez Yanina", "Israelson Analia", "Valiente Silvia"],
            ["Coronel Vanesa", "Dominguez Alejandra", "Quiroz Rosario"],
            ["Altamirano Maia", "Altamirano Pamela", "Cardozo Karolaine", "Gonzalez Iris"],
            ["Carena Graciela", "Deiana Ruth", "Valiente Fátima"],
            ["Dominguez Miriam", "Encina Mónica", "Viera Valeria"],
            ["Arguello Monica", "Benitez Gabriela", "Ledesma Susana", "Sotelo Rosa"]
        ]


    def asignar_manualmente (self) :

        grupos_asignados = self.obtener_grupos_asignados()

        for indice, grupo in enumerate(grupos_asignados, 1) :

            setattr(self.grupos, f'grupo_{indice}', grupo)


    def mostrar_grupos(self) :

        resultado = []
        
        for indice, grupo in enumerate([
            self.grupos.grupo_1,
            self.grupos.grupo_2,
            self.grupos.grupo_3,
            self.grupos.grupo_4,
            self.grupos.grupo_5,
            self.grupos.grupo_6
        ], 1) :
            
            resultado.append(f"Grupo {indice}: {', '.join(grupo)}")

        return "\n".join(resultado)

    
    def mostrar_limpieza_semanal (self) : 

        return f"\nLimpieza corresponde al grupo: {self.periodo.numero_grupo}"

    
    def obtener_integrantes_grupo_actual(self) -> str:

        grupo = getattr(self.grupos, f'grupo_{self.periodo.numero_grupo}', [])
        return f"Integrantes del grupo {self.periodo.numero_grupo}: {', '.join(grupo)}" if grupo else "Grupo no encontrado."
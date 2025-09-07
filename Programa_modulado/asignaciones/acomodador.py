from asignacion import Asignacion

class Acomodador (Asignacion) :

    def __init__(self, datos) :

        super().__init__(datos)
        self.datos = datos


    def mostrar (self) :

        total_datos = len(self.datos)
        horas = 2
        acomodadores_por_hora = 2  
        resultado = []

        for hora in range (horas) :

            inicio = hora * acomodadores_por_hora
            fin = inicio + acomodadores_por_hora
            asignados = " / ".join(self.datos[inicio:fin])
            resultado.append(f"Acomodadores {hora + 1}° Hora: {asignados}")

        if total_datos > horas * acomodadores_por_hora :

            acomodador_final = self.datos[horas * acomodadores_por_hora]
            resultado.append(f"Acomodador Final: {acomodador_final}")

        return "\n".join(resultado)


if __name__ == "__main__" :

    lista_acomodadores = ['Altamirano Elias', 'Altamirano Martin' ,'Altamirano Horacio', 'Dominguez Joel', 
                           'Encina Gerardo', 'Ferreira David', 'Gracia Enrique', 
                           'Israelson Fernando', 'Ontiveros Juan', 'Ortiz Aureliano', 
                           'Valiente Walter', 'Vallejos Horacio', 'Viera Cristian']
    
    acomodador = Acomodador(lista_acomodadores)
    acomodador.ordenar_aleatoriamente()
    print(acomodador.mostrar())
from asignacion import Asignacion

class Vigilancia (Asignacion) :

    def __init__(self, datos) :

        super().__init__(datos)
        self.datos = datos


    def mostrar (self) :
        
        horas = 2
        resultado = []

        for hora in range (horas) :

            try :

                asignado = self.datos[hora]
            
            except IndexError :

                asignado = "Sin asignar"

            resultado.append(f"Vigilancia {hora + 1}° Hora: {asignado}")

        return "\n".join(resultado)


if __name__ == "__main__" :

    lista_vigilancia =  ['Altamirano Maia', 'Altamirano Pamela', 'Arguello Monica', 
                        'Benitez Gabriela', 'Cardozo Karolaine', 'Carena Graciela', 
                        'Coronel Vanesa', 'Deiana Ruth', 'Dominguez Alejandra', 
                        'Dominguez Miriam', 'Encina Mónica', 'Ferreira Rocio', 
                        'Gomez Yanina', 'Gonzalez Iris', 'Israelson Analia', 
                        'Ledesma Susana', 'Quiroz Rosario', 'Sotelo Rosa', 
                        'Valiente Fátima', 'Valiente Silvia', 'Viera Valeria']
    
    vigilancia = Vigilancia(lista_vigilancia)
    vigilancia.ordenar_aleatoriamente()
    print(vigilancia.mostrar())
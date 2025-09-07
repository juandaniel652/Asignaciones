import random

class Asignacion :

    def __init__ (self, lista_asignados = None) :

        self.__lista_asignados = lista_asignados if lista_asignados else []

    def ordenar_alfabeticamente (self) :
        
        self.__lista_asignados.sort()
        return self.__lista_asignados

    def ordenar_aleatoriamente (self) :

        try :

            random.shuffle(self.__lista_asignados)
            return self.__lista_asignados
        
        except Exception as error :

            return f"Error: Debe haber un mínimo de 5 opciones\nCausa: {error}"


    def remover (self, indice) :

        try :

            del self.__lista_asignados[indice]
            return self.__lista_asignados
        
        except IndexError :
            
            return "Error: índice fuera de rango"

    
    def obtener_lista(self):
        return self.__lista_asignados


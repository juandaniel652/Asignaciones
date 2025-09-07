#Seleccion al azar

import random

lista = ["Aureliano Ortiz", "Martín Altamirano", "Fernando Israelson", "Juan Ontiveros", "Horacio Altamirano", 
         "Walter Valiente", "Gerardo Encina", "Enrique Gracia", "Joel Dominguez", "Armando Ligeron", "Elias Altamirano",
         "Horacio Vallejos"]



lista_random = random.sample(lista, 4)
print(lista_random)
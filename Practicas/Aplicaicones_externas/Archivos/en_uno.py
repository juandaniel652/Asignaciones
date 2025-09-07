import random
import pywhatkit as kit
import datetime

lista = ["Ortiz Aureliano", "Altamirano Martín", "Israelson Fernando", "Ontiveros Juan", "Altamirano Horacio", 
         "Valiente Walter", "Encina Gerardo", "Gracia Enrique", "Dominguez Joel", "Ligeron Armando", "Altamirano Elias",
         "Vallejos Horacio"]

lista_aleatoria = random.sample(lista, 4)

lista_vigilancia = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Mónica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gómez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Domínguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela"]

lista_vigilancia_aleatoria = random.sample(lista_vigilancia, 3)

print("\n")

h = f"""Buenos dias a todos queirdos hermanos!!! A continuación compartimos a los acomodadores y la vigilancia del dia 
miércoles.\n
_______________________________________\n
'''ACOMODADORES'''\n____________________\n
*Acomodadores 1° hora: {lista_aleatoria[0]} / {lista_aleatoria[1]}*\n
*Acomodadores 2° hora: {lista_aleatoria[2]} / {lista_aleatoria[3]}*\n
_______________________________________\n
'''VIGILANCIA'''\n____________________\n
*Vigilancia 1° hora: {lista_vigilancia_aleatoria[0]}*\n
*Vigilancia 2° hora: {lista_vigilancia_aleatoria[1]}*\n
*Vigilancia después de la reunión: {lista_vigilancia_aleatoria[2]}*\n
_______________________________________\n
Por favor, avisarme en caso de no poder asistir.\n
Muchas bendiciones!!!
"""

with open ('Archivo.txt', 'w') as archivo : 
    archivo.write(h)
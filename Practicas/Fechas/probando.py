import random
from datetime import datetime, time


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

h = f"""a todos queridos hermanos!!! A continuación compartimos a los acomodadores y la vigilancia del dia miércoles.\n
_______________________________________\n
```ACOMODADORES```\n________________________\n
*Acomodadores 1° hora: {lista_aleatoria[0]} / {lista_aleatoria[1]}*\n
*Acomodadores 2° hora: {lista_aleatoria[2]} / {lista_aleatoria[3]}*\n
_______________________________________\n
```VIGILANCIA```\n________________________\n
*Vigilancia 1° hora: {lista_vigilancia_aleatoria[0]}*\n
*Vigilancia 2° hora: {lista_vigilancia_aleatoria[1]}*\n
*Vigilancia después de la reunión: {lista_vigilancia_aleatoria[2]}*\n
_______________________________________\n
Por favor, avisarme en caso de no poder asistir.\n
Muchas bendiciones!!!
"""

# Obtener la hora actual
hora_actual = datetime.now().time()
hora = hora_actual.hour
minuto = hora_actual.minute

# Crear objetos time para las horas con las que quieres comparar
hora1 = time(6, 0)  # 14:30 (6:00 PM)
hora2 = time(13, 0)  # 13:00 (1:00 PM)
hora3 = time(20, 0) #20:00 (8: 00 PM)


hora_editable = hora_actual.strftime("%H:%m")

if hora_actual >= hora1 and hora_actual < hora2: 
    print("Buenos dias",h)

elif hora_actual >= hora2 and hora_actual < hora3 : 
    print("Buenas tardes",h)

elif hora_actual >= hora3 and hora_actual < hora1 : 
    print("Buenas noches",h)

else: 
    print("Salida")

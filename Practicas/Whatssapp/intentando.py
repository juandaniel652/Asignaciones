import pywhatkit as kit
import random
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

hora_actual = datetime.datetime.now()
minuto = hora_actual + datetime.timedelta(minutes = 1)

lista_dias = [1, 2, 3, 4, 5, 6]
fecha_actual = datetime.datetime.now().date()
dia_semana = fecha_actual.weekday()

for w in range (6) : 

        #Cuando la fecha actual no cae lunes

            if dia_semana == lista_dias[w] : 
            
                dia_calendario = datetime.timedelta(days = lista_dias[w])
                lunes = fecha_actual - dia_calendario
                break;
        
        #Cuando cae lunes

            elif dia_semana == 0 : 

                lunes = fecha_actual
                break;

        #Excepcion de error
        
            else: 

                pass;

martes = lunes + datetime.timedelta(days = 1)
miercoles = lunes + datetime.timedelta(days = 2)
jueves = lunes + datetime.timedelta(days = 3)
viernes = lunes + datetime.timedelta(days = 4)
sabado = lunes + datetime.timedelta(days = 5)
domingo = lunes + datetime.timedelta(days = 6)

if fecha_actual == domingo or fecha_actual == lunes or fecha_actual == martes or fecha_actual == miercoles: 
    txt = "del dia miércoles."


elif fecha_actual == jueves or fecha_actual == viernes or fecha_actual == sabado : 

    txt= "del dia sábado."


if hora_actual.hour > 6 and hora_actual.hour < 13 : 
    horario = f"Buenos dias todos queridos hermanos!!! A continuación compartimos a los acomodadores y la vigilancia {txt}"
    
elif hora_actual.hour >= 13 and hora_actual.hour < 20: 
    horario = f"Buenas tardes a todos queridos hermanos!!! A continuación compartimos a los acomodadores y la vigilancia {txt}"

elif hora_actual.hour >= 20 and hora_actual.hour < 2: 
    horario = f"Buenas noches a todos queridos hermanos!!! A continuación compartimos a los acomodadores y la vigilancia {txt}"

else: 

    print("Para tan tarde/temprano lo vas a hacer... Anda a dormir loco")
    



h = f"""{horario}

_______________________________

```ACOMODADORES```
_________________________

*Acomodadores 1° hora: {lista_aleatoria[0]} / {lista_aleatoria[1]}*

*Acomodadores 2° hora: {lista_aleatoria[2]} / {lista_aleatoria[3]}*

_______________________________

```VIGILANCIA```
_________________________

*Vigilancia 1° hora: {lista_vigilancia_aleatoria[0]}*

*Vigilancia 2° hora: {lista_vigilancia_aleatoria[1]}*

*Vigilancia después de la reunión: {lista_vigilancia_aleatoria[2]}*

_______________________________

Por favor, avisarme en caso de no poder asistir.

Muchas bendiciones!!!"""

# Número de teléfono con el prefijo del país, y el mensaje
phone_number = '+541141602708'


# Enviar mensaje a través de WhatsApp Web
# Nota: La hora y minutos deben ser mayores al tiempo actual
kit.sendwhatmsg(phone_number, h, hora_actual.hour, minuto.minute)
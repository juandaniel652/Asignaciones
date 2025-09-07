import pywhatkit as kit

# Mensaje que queremos imprimir y enviar por WhatsApp
mensaje = "Hola, este es un mensaje de prueba desde Python"

# Imprimimos el mensaje (simulando el uso de print)
print(mensaje)

# Configuración de los parámetros para enviar el mensaje
numero_telefono = "+541141602708"  # Reemplaza con el número de teléfono al que deseas enviar el mensaje
hora_envio = 18  # Hora de envío en formato 24 horas (por ejemplo, 15 para las 3 PM)
minuto_envio = 46  # Minuto de envío (por ejemplo, 30)

# Enviamos el mensaje por WhatsApp
kit.sendwhatmsg(numero_telefono, mensaje, hora_envio, minuto_envio)
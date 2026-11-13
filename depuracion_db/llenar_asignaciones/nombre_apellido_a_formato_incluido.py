def obtener_nombre (lista, indice):
    tuplas = lista[indice]
    nombre = tuplas["nombre"]
    return nombre

def obtener_apellido (lista, indice):
    tuplas = lista[indice]
    apellido = tuplas["apellido"]
    return apellido

def modificar_tipo_query (nombre, apellido, indice, lista):

    tuplas = lista[indice]
    mensaje = tuplas["tipo_mensaje"]
    mensaje_editado = f"{mensaje} '{apellido} {nombre} /%'" 
    return mensaje_editado


lista_diccionario_acomodador = [
  {"id": 14, 
  "nombre": "Elias", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 15, 
  "nombre": "Martin", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 16, 
  "nombre": "Horacio", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 17, 
  "nombre": "Joel", 
  "apellido": "Dominguez", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 18, 
  "nombre": "Gerardo", 
  "apellido": "Encina", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 19, 
  "nombre": "David", 
  "apellido": "Ferreira", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 20, 
  "nombre": "Enrique", 
  "apellido": "Gracia", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 21, 
  "nombre": "Fernando", 
  "apellido": "Israelson", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 22, 
  "nombre": "Juan", 
  "apellido": "Ontiveros", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 23, 
  "nombre": "Aureliano", 
  "apellido": "Ortiz", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 24, 
  "nombre": "Walter", 
  "apellido": "Valiente", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 25, 
  "nombre": "Cristian", 
  "apellido": "Viera", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 26, 
  "nombre": "Juan", 
  "apellido": "Herrera", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 27, 
  "nombre": "Francisco", 
  "apellido": "Cristaldo", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 28, 
  "nombre": "Luis", 
  "apellido": "Benitez", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 29, 
  "nombre": "Esteban", 
  "apellido": "Salas", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 30, 
  "nombre": "Horacio", 
  "apellido": "Vallejos", 
  "estado": False, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
  {"id": 31, 
  "nombre": "Maximiliano", 
  "apellido": "Gomez", 
  "estado": True, 
  "tipo_labor": "acomodador",
  "tipo_mensaje": f"Acomodadores_2_HS° like"},
  
]

for x in range (len(lista_diccionario_acomodador)):
    diccionario = lista_diccionario_acomodador[x]
    nombre = obtener_nombre(lista_diccionario_acomodador, x)
    apellido = obtener_apellido(lista_diccionario_acomodador, x)
    mensaje = modificar_tipo_query(nombre, apellido, x, lista_diccionario_acomodador)
    nueva_lista= lista_diccionario_acomodador[x]["tipo_mensaje"] = mensaje
    
print(lista_diccionario_acomodador)

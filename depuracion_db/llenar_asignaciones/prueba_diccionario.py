dict_prueba = None

dict_prueba = {"id": 31, 
  "nombre": "Elias", 
  "apellido": "Altamirano", 
  "estado": True, 
  "tipo_labor": "acomodador",
}
lista = [f"Acomodadores_1_HS° like '{dict_prueba['apellido']} {dict_prueba['nombre']} /%'", 
f"Acomodadores_2_HS° like '{dict_prueba['apellido']} {dict_prueba['nombre']} /%'",
f"Acomodadores_1_HS° like '%/ {dict_prueba['apellido']} {dict_prueba['nombre']}'",
f"Acomodadores_2_HS° like '%/ {dict_prueba['apellido']} {dict_prueba['nombre']}'"]

lista_unica = [f"Acomodador_final = '{dict_prueba['apellido']} {dict_prueba['nombre']}'",
            f"Vigilancia_1°_HS = '{dict_prueba['apellido']} {dict_prueba['nombre']}'",
            f"Vigilancia_2°_HS = '{dict_prueba['apellido']} {dict_prueba['nombre']}'",
            f"Vigilancia_final = '{dict_prueba['apellido']} {dict_prueba['nombre']}'"]



print(lista)
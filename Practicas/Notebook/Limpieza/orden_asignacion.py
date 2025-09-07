#Recordemos que es para limpieza, por ende solo contaremos por el momento a las hermanas asignadas para vigilancia,
#Tiene un parecido con limpieza final en la carpeta 'Vigilancia', pero la idea es que este sea mas óptimo y ya sea 
#Aplicable al programa final

lista_vigilancia = ["Deiana Ruth", "Benitez Gabriela", "Gonchay Brenda", "Altamirano Araceli", "Altamirano Maia", 
                    "Valiente Fátima", "Dominguez Alejandra", "Israelson Analia", "Encina Mónica", "Arguello Monica", 
                    "Valiente Silvia", "Quiroz Rosario", "Ferreira Rocio", "Cardozo Karolaine", "Gomez Yanina", 
                    "Viera Valeria", "Coronel Vanesa", "Dominguez Miriam", "Ledesma Susana", "Sotelo Rosa",
                    "Altamirano Pamela"]

lista_vigilancia.sort()


grupo_1 = ["Ferreira Rocio", "Gomez Yanina", "Israelson Analia", "Valiente Silvia"]
grupo_2 = ["Benitez Gabriela", "Dominguez Alejandra", "Quiroz Rosario"]
grupo_3 = ["Altamirano Araceli", "Altamirano Maia", "Altamirano Pamela", "Cardozo Karolaine", "Sotelo Rosa", "Viera Valeria"]
grupo_4 = ["Deiana Ruth", "Ledesma Susana", "Valiente Fátima"]
grupo_5 = ["Arguello Monica", "Coronel Vanesa", "Dominguez Miriam", "Encina Mónica", "Gonchay Brenda"]




indice_lista_gral = 0

for z in lista_vigilancia : 
    indice_lista_gral = indice_lista_gral + 1


indice_1 = 0 

for i in grupo_1 : 

    indice_1 = indice_1 + 1


for j in range (indice_1) : 
    for x in range (indice_lista_gral) : 
        if grupo_1[j] == lista_vigilancia[x] : 
            print(f"Iguales en lista vigilancia: {lista_vigilancia[x]}")
            del lista_vigilancia[x]
            break;

print(f"Lista viiglancia despues del DEL: {lista_vigilancia}")

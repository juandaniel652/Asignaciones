#Llevandolo a vigilancia 

#Total de hermanas que trabajan de vigilancia.
#indice = 0
#
#for i in lista_vigilancia : 
#    indice = indice + 1
#
#print(indice) #22


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


seleccion = int(input("Ingrese el numero del grupo al cual le corresponde la limpieza del salón en esa semana [1 - 5]: "))

if seleccion > 0 and seleccion <= 5 : 

    if seleccion == 1: 
        limpieza_1 = list(set(grupo_1) & set(lista_vigilancia))
        print(f"Tienen Limpieza: {limpieza_1}\n\n")
        eliminar_1 = list(set(lista_vigilancia) - (set(grupo_1)))
        print(eliminar_1)

    elif seleccion == 2 : 
        limpieza_2 = list(set(grupo_2) & set(lista_vigilancia))
        print(f"Tienen Limpieza: {limpieza_2}\n\n")
        eliminar_2 = list(set(lista_vigilancia) - (set(grupo_2)))
        print(f"Eliminacion de una lista pasada a conjubto: {eliminar_2}")
    
          

    elif seleccion == 3 : 
        limpieza_3 = list(set(grupo_3) & set(lista_vigilancia))
        print(f"Tienen Limpieza: {limpieza_3}\n\n")
        eliminar_3 = list(set(lista_vigilancia) - (set(grupo_3)))
        print(eliminar_3)

    elif seleccion == 4 : 
        limpieza_4 = list(set(grupo_4) & set(lista_vigilancia))
        print(f"Tienen Limpieza: {limpieza_4}\n\n")
        eliminar_4 = list(set(lista_vigilancia) - (set(grupo_4)))
        print(eliminar_4)

    elif seleccion == 5 : 
        limpieza_5 = list(set(grupo_5) & set(lista_vigilancia))
        print(f"Tienen Limpieza: {limpieza_5}\n\n")
        eliminar_5 = list(set(lista_vigilancia) - (set(grupo_5)))
        print(eliminar_5)


    else: 
        print("Error. Intente de nuevo.")
    

else: 
    print("Error. Ingrese el numero de grupo dentro de lo establecido.")
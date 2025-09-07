#import random

#Creación lista
lista =  ["Aureliano Ortiz", "Martín Altamirano", "Fernando Israelson", "Juan Ontiveros", "Horacio Altamirano", 
         "Walter Valiente", "Gerardo Encina", "Enrique Gracia", "Joel Dominguez", "Armando Ligeron", "Elias Altamirano",
         "Horacio Vallejos"]

lista_g = []

#Inicicializar indice y opcion cantidad
indice = 0 
cantidad = int(input("Ingrese la cantidad de índices a remover: "))

print("\n================== \nLista actual:\n")

#Muestreo de lista a ser editada


#Configuración y muestreo de resultado de lista
for i in range (cantidad): 
    for x in lista: 
        indice = indice + 1
        print(f"{indice}. {x}")
    print("\n================================")
    seleccion = int(input("Seleccione el indice a ser removido: "))
    if seleccion > 0 : 
        indice = seleccion - 1
        lista_g.append(lista[indice])
        print(f"\nSelecciondo = {indice + 1}. {lista[indice]}\n")

        if indice :
            del lista[indice]
        elif indice == 1 : 
            del lista[1]
    
        
    else: 
        print("\nEl indice seleccionado debe ser mayor a 0.\n")


print(f"\nSi pueden: {lista}")
print(f"\nNo pueden: {lista_g}")


#Random
#for i in range (4) : 
#    lista_random = random.choice(lista)
#    print(f"{lista_random}")
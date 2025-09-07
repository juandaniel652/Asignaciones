#Este es bueno, pero al recorrer y confimar devuelve si o si falsos (no quiere que devuelva)

lista = ["Manzana", "Banana", "Limón"]

#if lista[0] == "Manzana" : 
#    lista[0] = lista[1]
#    lista.pop(0)
#    #print(lista)

#########

#for frutas in range(len(lista)) : 
#    if lista[frutas] == "Limón" : 
#        print("correcto")
#
#    else : 
#        print("Incorrecto")

#########

for r in range(len(lista)) : 

    if "Manzana" in lista :
        print(r)

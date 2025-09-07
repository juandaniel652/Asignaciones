lista_1 = ['Pera', 'Manzana', 'Banana', 'Ananá']
lista_2 = ['Manzana', 'Ananá']

for indice  in range(len(lista_1)) : 

    if indice < len(lista_2) : 
        
        if lista_2[indice] in lista_1 : 

            print(lista_2[indice])
#SIN ZIP: Error ya que tuple no toma dos argumentos, se puede, pero con el zip es mas eficiente.
#lista = ['p', 'y', 'l']
#list_2 = ['r', 'q', '2']
#lista_tupla = []
#lista_tupla_2 = []
#for i in lista :
#    for x in list_2 : 
#        lista_tupla.append(i)
#        lista_tupla_2.append(x)
#print(tuple(lista_tupla, lista_tupla_2))

#CON ZIP
#En este ejemplo, al haber añadido un elemnto más a la lista, ¿Que hace zip? termina la iteración de cada elemento 
#cuando se llega al último elemento de la LISTA MAS CORTA. Por ende en este caso, el resultado es el mismo.
#Si usara 'lista3' ahi si al ser la misma cantidad de elementos, cada uno se asocia a otro y se 'completa' por asi decirlo.

lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c']
lista3 = ['a', 'b', 'c', 'd']

combinado = zip(lista1, lista2)
print(list(combinado))  # [(1, 'a'), (2, 'b'), (3, 'c')]


#lista = ['a', 'b', 'c','d']
#lista_comparada = ['t', 'y', 'o', 'b']
#
##SET: Pasa la lista a tipo de dato conjunto
##print(lista)
##print(set(lista))
#
#print(zip(lista))


lista1 = [1, 2, 3]
lista2 = [1, 2, 4]

for a, b in zip(lista1, lista2):
    if a != b:
        print(f"{a} y {b} son diferentes")


#Con diccionario.
keys = ['nombre', 'edad', 'pais']
values = ['Ana', 25, 'España']

diccionario = dict(zip(keys, values))
print(diccionario)  # {'nombre': 'Ana', 'edad': 25, 'pais': 'España'}

#lista = ["Aureliano Ortiz", "Martín Altamirano", "Fernando Israelson", "Juan Ontiveros", "Horacio Altamirano", 
#         "Walter Valiente", "Gerardo Encina", "Enrique Gracia", "Joel Dominguez", "Armando Ligeron", "Elias Altamirano",
#         "Horacio Vallejos"]
#
#
#cantidad = int(input("Ingrese la cantidad de índices a remover: "))
#for i in range (cantidad): 
#    indice = int(input("Elija el indice a remover: "))
#    print(f"{indice}. {lista[indice]}")
#    del lista[indice]
#    print(f"{lista}")


#lista = ["Aureliano Ortiz", "Martín Altamirano", "Fernando Israelson", "Juan Ontiveros", "Horacio Altamirano", 
#         "Walter Valiente", "Gerardo Encina", "Enrique Gracia", "Joel Dominguez", "Armando Ligeron", "Elias Altamirano",
#         "Horacio Vallejos"]
#
#
#print(lista[1])
#del lista[1]
#print(lista[1])

#Remove: Elimina por elemento y se reemplaza indice

#lista = ["Manzana", "Naranaja", "Limon", "Banana", "Pomelo"]
#
#print(lista[0])
#lista.remove("Manzana")
#print(lista[0])

#Pop: Se reemplaza alborrar pero muestra cual fue el elemento borrado
#lista = ["Manzana", "Naranaja", "Limon", "Banana", "Pomelo"]
#lista.pop(1)
#print(lista[1])

#Del: Selecciona por indice
#lista = ["Manzana", "Naranaja", "Limon", "Banana", "Pomelo"]
#del lista [1]
#print(lista[1])


#lista = ["Manzana", "Naranaja", "Limon", "Banana", "Pomelo"]
#lista_g = []
#
#cantidad = int(input("Ingrese la cantidad de índices a remover: "))
#
#for i in range (cantidad): 
#    indice = int(input("Seleccione el indice a eliminar: "))
#    lista_g.append(lista[indice])
#    del lista[indice]
#    
#print(lista_g)
#print(lista)

lista = ["Manzana", "Naranaja", "Limon", "Banana", "Pomelo"]
lista_g = []
indice = 0



for x in lista: 
    indice = indice + 1
    print(f"{indice}. {x}")
    
print("\n================================")

cantidad = int(input("Ingrese la cantidad de índices a remover: "))

for i in range (cantidad):
    seleccion = int(input("Seleccione el indice a ser removido: "))
    indice = seleccion - 1
    lista_g.append(lista[indice])
    print(f"Seleccionado: {lista[indice]}")

print(lista_g)
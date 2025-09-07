#n1 = 56
#n2 = 78
#suma = n1 + n2 
#
## Abre (o crea si no existe) un archivo llamado 'archivo.txt' en modo de escritura
#with open('archivo.txt', 'w') as archivo:
#    # Escribe una línea en el archivo
#    archivo.write('Hola, este es un archivo de texto creado en Python.\n')
#    archivo.write('Esta es otra línea de texto e imprime la suma por código.\n')
#    archivo.write(f'{suma}')
#
#print('Archivo creado y texto escrito.')
#
## Abre el archivo en modo de lectura
#with open('archivo.txt', 'r') as archivo:
#    # Lee todo el contenido del archivo
#    contenido = archivo.read()
#
#print('Contenido del archivo:')
#print(contenido)

## Paso 1: Crear y escribir en el archivo
#with open('archivo_lectura.txt', 'w') as archivo:
#    archivo.write('Este archivo ha sido creado para ser leído.\n')
#    archivo.write('Esta es otra línea de texto.')
#
#try:
#    with open('archivo_lectura.txt', 'r') as archivo:
#        contenido = archivo.read()
#        contenido
#    print('Contenido del archivo:')
#    print(contenido)
#except FileNotFoundError:
#    print('El archivo no existe.')

import os

# Crear y escribir en el archivo
with open('archivo_solo_lectura.txt', 'w') as archivo:
    archivo.write('Este es un archivo que será configurado como solo lectura.\n')
    archivo.write('Contiene dos líneas de texto.')

# Cambiar los permisos del archivo a solo lectura
os.chmod('archivo_solo_lectura.txt', 0o444)

print('El archivo ahora es solo lectura.')




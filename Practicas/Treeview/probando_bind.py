#import tkinter as tk
#
#def mostrar_mensaje(event):
#    print("¡Clic detectado!")
#
#root = tk.Tk()
#
## Crear un botón
#boton = tk.Button(root, text="Haz clic aquí")
#boton.pack()
#
## Asignar el evento al botón
#boton.bind("<", mostrar_mensaje)  # "<Button-1>" se refiere a un clic del botón izquierdo del ratón
#
#root.mainloop()

#==================================================================

#import tkinter as tk
#
#def mostrar_info(event):
#    print(f"Posición del clic: ({event.x}, {event.y})")
#
#root = tk.Tk()
#
## Crear una etiqueta para hacer clic
#etiqueta = tk.Label(root, text="Haz clic en mí")
#etiqueta.pack()
#
## Asociar el clic del ratón a la etiqueta
#etiqueta.bind("<Button-1>", mostrar_info)
#
#root.mainloop()

#==================================================================

import tkinter as tk

def click_izquierdo(event):
    print(f"Clic izquierdo en: ({event.x}, {event.y})")

def click_derecho(event):
    print(f"Clic derecho en: ({event.x}, {event.y})")

def tecla_presionada(event):
    print(f"Tecla presionada: {event.char}")

def enter (event) : 
    print("tecla selccionada: Enter")

root = tk.Tk()

# Crear un widget que capture los eventos
frame = tk.Frame(root, width=300, height=200, bg="lightblue")
frame.pack()

# Asociar eventos al frame
frame.bind("<Button-1>", click_izquierdo)   # Clic izquierdo
frame.bind("<Button-3>", click_derecho)     # Clic derecho
frame.bind("<KeyPress>", tecla_presionada)  # Cualquier tecla
frame.bind("<Return>", enter) 

# El frame necesita tener el foco para detectar teclas
frame.focus_set()

root.mainloop()


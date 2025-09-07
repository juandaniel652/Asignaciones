from PIL import Image, ImageTk

class IconoAplicacion :

    """
    Clase para establecer el icono de la ventana principal de la aplicación.
    No muestra la imagen en la interfaz, solo la usa como icono de la app.
    """

    def __init__ (self, ventana, ruta_icono) :

        try :

            ventana.iconbitmap(ruta_icono)

        except Exception :

            pass  # Si falla (por ejemplo, en Linux), ignora el error

        # Usar wm_iconphoto para mostrar el logo en la barra de tareas (más universal)
        try :

            # Cargar imagen compatible (PNG recomendado para wm_iconphoto)
            imagen = Image.open(ruta_icono)
            # Convertir a formato compatible con Tkinter
            icono = ImageTk.PhotoImage(imagen)
            ventana.wm_iconphoto(True, icono)
            # Guardar referencia para evitar que el recolector de basura la elimine
            self._icono = icono

        except Exception :
            
            pass
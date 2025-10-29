import requests
import os

VERSION_LOCAL = "1.6"
URL_VERSION = "version.txt"
URL_DESCARGA = "https://github.com/tuusuario/miapp/releases/latest/download/main"

def verificar_actualizacion () :
    
    try :
        
        request = requests.get(URL_VERSION, timeout=5)
        
        if request.status_code == 200 :
            
            version_online = request.text.strip()
            
            if version_online != VERSION_LOCAL :
                
                return True, version_online
            
        return False, None
    
    except Exception as error :
        
        print("Error al verificar actualización:", error)
        return False, None


def descargar_actualizacion():
    
    try:

        with requests.get(URL_DESCARGA, stream=True) as r :
            
            with open("main_nuevo", "wb") as f:
                
                for chunk in r.iter_content(chunk_size=8192):
                    
                    f.write(chunk)
                    
        print("Actualización descargada correctamente.")
        # Podrías luego cerrar el programa y reemplazar el archivo actual
    except Exception as e:
        print("Error al descargar:", e)

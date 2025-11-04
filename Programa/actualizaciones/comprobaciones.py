import requests
import os


VERSION_LOCAL = "1.6"
URL_VERSION = "https://pastebin.com/raw/vAYDdXDh"
URL_DESCARGA = "https://github.com/juandaniel652/Asignaciones/commits/v1.6"

def verificar_actualizacion():
    try:
        headers = {"User-Agent": "MiApp/1.6"}
        r = requests.get(URL_VERSION, headers=headers, timeout=5)
        if r.status_code == 200:
            version_online = r.text.strip()
            print(f"Versión local: {VERSION_LOCAL}")
            print(f"Versión online: {version_online}")

            if version_online != VERSION_LOCAL:
                print("✅ Nueva versión disponible.")
            else:
                print("🟢 Ya tienes la última versión.")
        else:
            print("Error al obtener la versión:", r.status_code)

        
    except Exception as e:
        print("Error al verificar actualización:", e)


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



a = verificar_actualizacion()
print(a)
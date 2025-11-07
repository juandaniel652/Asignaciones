import requests, os, zipfile, shutil

VERSION_LOCAL = "1.6.1"
URL_VERSION = "https://raw.githubusercontent.com/juandaniel652/Asignaciones/main/Programa/actualizaciones/version.txt"
URL_DESCARGA = "https://github.com/juandaniel652/Asignaciones/releases/download/v1.6.1/Acomodadores.zip"

APP_DIR = os.path.dirname(os.path.abspath(__file__))  # Carpeta del programa
ZIP_FILE = os.path.join(APP_DIR, "update.zip")

def verificar_actualizacion():
    try:
        r = requests.get(URL_VERSION, timeout=5)
        if r.status_code == 200:
            version_online = r.text.strip()

            if version_online != VERSION_LOCAL:
                print(f"✅ Nueva versión disponible: {version_online}")
                descargar_actualizacion()
            else:
                print("🟢 Ya tienes la última versión.")
        else:
            print("Error al obtener versión:", r.status_code)
    except Exception as e:
        print("Error al verificar actualización:", e)


def descargar_actualizacion():
    try:
        print("⬇️ Descargando actualización...")
        with requests.get(URL_DESCARGA, stream=True) as r:
            with open(ZIP_FILE, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print("✅ Actualización descargada. Instalando...")

        instalar_actualizacion()

    except Exception as e:
        print("Error al descargar:", e)


def instalar_actualizacion():
    
    r = requests.get(URL_VERSION, timeout=5)
    version_online = r.text.strip()
    
    try:
        temp_dir = os.path.join(APP_DIR, "update_temp")
        os.makedirs(temp_dir, exist_ok=True)

        with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        # Copiar archivos al programa
        for item in os.listdir(temp_dir):
            src = os.path.join(temp_dir, item)
            dst = os.path.join(APP_DIR, item)

            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)

        os.remove(ZIP_FILE)
        shutil.rmtree(temp_dir)

        # Actualizar version local ✅
        with open(os.path.join(APP_DIR, "version.txt"), "w") as f:
            f.write(version_online)

        print("✅ Actualización completada.")
        print("🔁 Reinicia la aplicación para aplicar cambios.")

    except Exception as e:
        print("Error aplicando actualización:", e)


verificar_actualizacion()

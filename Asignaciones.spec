# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files

datas = [
    ('Programa/img/*', 'Programa/img'),
    # Agregamos la base de datos que está fuera de la carpeta Programa
    ('asignaciones_de_congregacion.db', '.'),
]

# Incluye recursos de PIL (por seguridad)
datas += collect_data_files('PIL', include_py_files=True)

a = Analysis(
    ['Programa/Asignaciones.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Asignaciones',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    icon='Programa/img/cuaderno.png'
)

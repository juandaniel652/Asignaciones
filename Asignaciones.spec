# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files

# Incluimos las carpetas reales necesarias
datas = [
    ('Programa/img/*', 'Programa/img'),   # imágenes y recursos gráficos
]

# Si luego agregás iconos o base de datos, podés descomentar:
# ('Programa/iconos/*', 'Programa/iconos'),
# ('Programa/db/*', 'Programa/db'),

# Recursos extra para PIL (Pillow)
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
    icon='Programa/img/cuaderno.ico'
)

import sqlite3
import tkinter as tk
from tkinter import ttk

# 📌 Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("mi_base.db")
cursor = conn.cursor()

# 📌 Crear una tabla (si no existe)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
""")
conn.commit()

# 📌 Insertar datos de ejemplo (solo si la tabla está vacía)
cursor.execute("SELECT COUNT(*) FROM usuarios")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", [
        ("Alice", 25),
        ("Bob", 30),
        ("Charlie", 22),
    ])
    conn.commit()

# 📌 Función para cargar los datos en el Treeview
def cargar_datos():
    # Limpiar datos anteriores
    for row in tree.get_children():
        tree.delete(row)

    # Obtener datos de la base
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)  # Insertar en el Treeview

# 📌 Interfaz con Tkinter
root = tk.Tk()
root.title("Usuarios - SQLite")

# Crear Treeview
columns = ("ID", "Nombre", "Edad")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)  # Encabezado
    tree.column(col, width=100)  # Ajustar ancho

tree.pack(expand=True, fill="both")

# Botón para recargar datos
btn_cargar = tk.Button(root, text="Cargar Datos", command=cargar_datos)
btn_cargar.pack()

# Cargar datos al iniciar
cargar_datos()

# Ejecutar ventana
root.mainloop()

# Cerrar la conexión (opcional)
conn.close()

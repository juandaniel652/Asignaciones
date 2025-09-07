import tkinter as tk
from tkinter import messagebox
from docx import Document

# Función para guardar el contenido en un archivo Word
def guardar_en_word():
    # Obtener el texto del widget de entrada
    texto = entrada_texto.get("1.0", tk.END)
    
    # Crear un nuevo documento de Word
    doc = Document()
    
    # Añadir el texto al documento
    doc.add_paragraph(texto)
    
    # Guardar el archivo Word
    try:
        doc.save("salida.docx")
        messagebox.showinfo("Éxito", "El archivo Word se ha guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al guardar el archivo: {e}")

# Crear la ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Guardar en Word")

# Crear un widget de entrada de texto
entrada_texto = tk.Text(ventana, height=10, width=40)
entrada_texto.pack(pady=10)

# Crear un botón para guardar el archivo Word
boton_guardar = tk.Button(ventana, text="Guardar en Word", command=guardar_en_word)
boton_guardar.pack(pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()

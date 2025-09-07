from docx import Document

def extraer_texto_word(ruta_docx):
    """Lee un archivo .docx y devuelve su texto como una cadena."""
    try:
        doc = Document(ruta_docx)
        texto = "\n".join([p.text for p in doc.paragraphs])
        return texto.strip()
    except Exception as e:
        return f"Error al leer el archivo Word: {e}"

# Uso del programa
ruta_docx = "Word/Discursos_publicos/VyMC mar y abr 2025 (1).docx"  # Reemplázalo con la ruta de tu archivo
texto_extraido = extraer_texto_word(ruta_docx)

# Muestra el texto extraído
print(texto_extraido)

# Copiar al portapapeles (opcional)
try:
    import pyperclip
    pyperclip.copy(texto_extraido)
    print("\nTexto copiado al portapapeles.")
except ImportError:
    print("\nInstala 'pyperclip' con 'pip install pyperclip' para copiar al portapapeles.")

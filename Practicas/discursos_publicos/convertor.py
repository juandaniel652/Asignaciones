import fitz  # PyMuPDF

def extraer_texto_pdf(ruta_pdf):
    """Lee un PDF y devuelve su texto como una cadena."""
    try:
        doc = fitz.open(ruta_pdf)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text("text") + "\n"
        return texto.strip()
    except Exception as e:
        return f"Error al leer el PDF: {e}"

# Uso del programa
ruta_pdf = "Asignaciones_de_Febrero_2025.pdf"  # Reemplázalo con la ruta de tu PDF
texto_extraido = extraer_texto_pdf(ruta_pdf)

# Muestra el texto extraído y lo copia al portapapeles si quieres
print(texto_extraido)

# Copiar al portapapeles (opcional, requiere pyperclip)
try:
    import pyperclip
    pyperclip.copy(texto_extraido)
    print("\nTexto copiado al portapapeles.")
except ImportError:
    print("\nInstala 'pyperclip' con 'pip install pyperclip' para copiar al portapapeles.")

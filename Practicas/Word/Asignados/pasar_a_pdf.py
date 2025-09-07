import os
import comtypes.client

def convertir_docx_a_pdf(input_path, output_path=None):
    word = comtypes.client.CreateObject("Word.Application")
    doc = word.Documents.Open(os.path.abspath(input_path))

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    doc.SaveAs(os.path.abspath(output_path), FileFormat=17)  # 17 es el formato PDF
    doc.Close()
    word.Quit()

    print(f"PDF guardado en: {output_path}")

# Uso:
convertir_docx_a_pdf("Asignaciones.docx")

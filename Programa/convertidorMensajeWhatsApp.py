from docx import Document

def generar_documento_whatsapp(titulos_de_acomodadores_y_vigilancia, lista_de_los_parrafos, semanas_totales, cantidad_de_datos):
    """
    Genera un documento Word simulando el formato de mensajes de WhatsApp
    para las listas de Acomodadores y Vigilancia.
    """
    documento = Document()

    for cantidad in range(cantidad_de_datos):
        # Título de la semana
        documento.add_paragraph(f"{semanas_totales[cantidad]}\n")

        # Iterar subtítulos: ACOMODADORES y VIGILANCIA
        for i, subtitulo in enumerate(titulos_de_acomodadores_y_vigilancia[cantidad]):
            # Separador superior
            documento.add_paragraph("_________________________")

            # Bloque con ```TITULO```
            documento.add_paragraph(f"```{subtitulo.strip()}```")

            # Separador inferior
            documento.add_paragraph("_______________________\n")

            # Agregar cada línea del grupo correspondiente
            for texto in lista_de_los_parrafos[cantidad][i]:
                documento.add_paragraph(f"*{texto}*")

            # Separador entre secciones
            documento.add_paragraph("_________________________\n")

        # Espacio entre semanas
        documento.add_paragraph("\n")

    # Retornar documento listo
    return documento

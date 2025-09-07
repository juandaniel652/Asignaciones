from asignaciones.acomodador import Acomodador

def test_mostrar_acomodadores():
    
    lista_acomodadores = ["Altamirano Horacio", "Gracia Enrique", "Valiente Walter", "Altamirano Elias",
                        "Ferreira David"]

    afirmacion = Acomodador(lista_acomodadores)
    resultado = afirmacion.mostrar()
    assert resultado == ['Acomodadores 1° Hora: Altamirano Horacio / Gracia Enrique', 'Acomodadores 2° Hora: Valiente Walter / Altamirano Elias', 'Acomodador Final: Ferreira David'] 
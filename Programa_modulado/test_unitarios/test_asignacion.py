from asignaciones_generales.asignacion import Asignacion

def test_ordenar_alfabeticamente () :

    afirmacion = Asignacion(["Carlos", "Ana", "Beto"])
    resultado = afirmacion.ordenar_alfabeticamente()
    assert resultado == ["Ana", "Beto", "Carlos"]

def test_ordenar_aleatoriamente () :

    lista = ["Carlos", "Ana", "Beto", "David", "Eva"]
    afirmacion = Asignacion(lista.copy())
    resultado = afirmacion.ordenar_aleatoriamente()
    assert sorted(resultado) == sorted(lista)  # Comprobamos que tenga los mismos elementos

def test_remover_valido () :

    afirmacion = Asignacion(["Carlos", "Ana", "Beto"])
    resultado = afirmacion.remover(1)
    assert resultado == ["Carlos", "Beto"]

def test_remover_fuera_de_rango () :

    afirmacion = Asignacion(["Carlos", "Ana", "Beto"])
    resultado = afirmacion.remover(5)
    assert resultado == "Error: índice fuera de rango"
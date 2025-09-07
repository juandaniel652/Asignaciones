import datetime
from fechas.semana_resultado import SemanaResultado

class Semana :

    def __init__ (self, fecha_actual: datetime.date) :

        self.fecha_actual = fecha_actual


    def obtener_lunes_actual (self) -> datetime.date :

        dias_hasta_lunes = self.fecha_actual.weekday()
        lunes = self.fecha_actual - datetime.timedelta(days=dias_hasta_lunes)
        return lunes


    def renovar_semana (self, lunes: datetime.date) -> SemanaResultado :
        
        hoy = self.fecha_actual
        inicio_semana = lunes
        fin_semana = lunes + datetime.timedelta(days = 6)

        if not (inicio_semana <= hoy <= fin_semana) :

            return SemanaResultado([], [], [], [], 0, None, [], [])

        distancia_inicial = datetime.date(2024, 8, 19)
        distancia_final = datetime.date(2025, 4, 19)
        diferencia_dias = distancia_final - distancia_inicial
        diferencia_semanas = diferencia_dias.days // 7
        total_semanas = diferencia_semanas

        return self.generar_listas_semanas(lunes, total_semanas, distancia_final)


    def generar_listas_semanas(
        self,
        lunes: datetime.date,
        total_semanas: int,
        distancia_final: datetime.date
    ) -> SemanaResultado:

        lista_semanas = []
        lista_martes = []
        lista_miercoles = []
        lista_sabado = []
        lista_domingo = []
        lista_lunes = []

        for semana in range(total_semanas) :

            inicio = lunes + datetime.timedelta(weeks=semana)
            fin = inicio + datetime.timedelta(days=6)
            dias = [inicio + datetime.timedelta(days=dia) for dia in range(7)]

            if inicio.month != fin.month:
                texto = (
                    f"Del {inicio.strftime('%d')} de {inicio.strftime('%B')} "
                    f"al {fin.strftime('%d')} de {fin.strftime('%B')} {fin.strftime('%Y')}\n"
                )
            else:
                texto = (
                    f"Del {inicio.strftime('%d')} al {fin.strftime('%d')} de {fin.strftime('%B')} {fin.strftime('%Y')}\n"
                )

            lista_semanas.append(texto)

            lista_lunes.append(inicio)
            lista_martes.append(dias[1].strftime("%d - %m - %Y"))
            lista_miercoles.append(dias[2].strftime("%d - %m - %Y"))
            lista_sabado.append(dias[5].strftime("%d - %m - %Y"))
            lista_domingo.append(dias[6].strftime("%d - %m - %Y"))

            print(distancia_final)

        return SemanaResultado(
            lista_semanas,
            lista_miercoles,
            lista_domingo,
            lista_lunes,
            total_semanas,
            distancia_final,
            lista_martes,
            lista_sabado
        )


    def semanas_transcurridas (self, desde: datetime.date) -> int :

        lunes_actual = self.obtener_lunes_actual()
        diferencia = lunes_actual - desde
        return diferencia.days // 7



def meses_espanol_decorator(func):
    """
    Decorador para traducir los nombres de los meses al español
    en los textos generados por la función generar_listas_semanas.
    """
    meses = {
        "January": "Enero",
        "February": "Febrero",
        "March": "Marzo",
        "April": "Abril",
        "May": "Mayo",
        "June": "Junio",
        "July": "Julio",
        "August": "Agosto",
        "September": "Septiembre",
        "October": "Octubre",
        "November": "Noviembre",
        "December": "Diciembre"
    }

    def traducir_mes(texto):
        for en, es in meses.items():
            texto = texto.replace(en, es)
        return texto

    def wrapper(self, *args, **kwargs):
        resultado = func(self, *args, **kwargs)
        # Traducir los textos de lista_semanas
        if hasattr(resultado, "lista_semanas"):
            resultado.lista_semanas = [traducir_mes(txt) for txt in resultado.lista_semanas]
        return resultado
    return wrapper
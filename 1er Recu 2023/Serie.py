from Contenido import Contenido

class Serie(Contenido):
    def __init__(self, nombre, año, calificacion):
        super().__init__(nombre, año, calificacion)
        self.__capitulos = []
from Contenido import Contenido

class Pelicula(Contenido):
    def __init__(self, nombre, año, calificacion):
        super().__init__(nombre, año, calificacion)
        self.__vista = False
from Pokemon import Pokemon

class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo = 'Fuego'
        self._debilidad = 'Agua'
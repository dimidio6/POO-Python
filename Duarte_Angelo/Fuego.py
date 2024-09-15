from Pokemon import Pokemon

class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo = 'Fuego'
        self._debilidad = 'Agua'
    
    def imprimir(self):
        return super().imprimir()
    
    def ataque(self, pokemon):
        return super().ataque(pokemon)
    
    def defensa(self, ataque):
        return super().defensa(ataque)
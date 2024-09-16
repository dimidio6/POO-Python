from Pokemon import Pokemon

class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo = 'Fuego'
        self._debilidad = 'Agua'
    
    def getSalvajismo(self):
        return super().getSalvajismo()
    
    def setSalvajismo(self, valor):
        return super().setSalvajismo(valor)
    
    def getVida(self):
        return super().getVida()
    
    def setVida(self, valor):
        return super().setVida(valor)
    
    def getNombre(self):
        return super().getNombre()
    
    def imprimir(self):
        return super().imprimir()
    
    def ataque(self, pokemon):
        return super().ataque(pokemon)
    
    def defensa(self, ataque):
        return super().defensa(ataque)
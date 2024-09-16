from Pokemon import Pokemon
from random import *

class Agua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo = 'Agua'
        self._debilidad = 'Hierba'
    
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
        if self._tipo == pokemon._debilidad:
            return self._ataque+self._ataque*0.7 #incrementa el ataque en %70
        else:
            return self._ataque
    
    def defensa(self, ataque):
        probabilidad = randint(1,10)
        if probabilidad < 4: #probabilidad del %30
            super().defensa(ataque*0.5) #reduce el daño %50
        else:
            super().defensa(ataque)
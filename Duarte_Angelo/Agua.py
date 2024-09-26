from Pokemon import Pokemon
from random import *

class Agua(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre,'Agua','Hierba')
    
    def ataque(self, pokemon):
        if self._tipo == pokemon.getDebilidad():
            return self._ataque+self._ataque*0.7 #incrementa el ataque en %70
        else:
            return self._ataque
    
    def defensa(self, ataque):
        probabilidad = randint(1,10)
        if probabilidad < 4: #probabilidad del %30
            super().defensa(ataque*0.5) #reduce el daño %50
        else:
            super().defensa(ataque)
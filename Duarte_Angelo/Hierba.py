from Pokemon import Pokemon
from random import *

class Hierba(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._tipo = 'Hierba'
        self._debilidad = 'Fuego'
    
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
    
    def defensa(self,ataque):
        probabilidad = randint(1,2) #probabilidad del %50
        if not(self._velocidad > 50 and probabilidad == 1): #uso un not para pensarlo de forma inversa
            super().defensa(ataque)
        #si no entra en la condición significa que esquivó el ataque
from abc import ABC, abstractmethod
from random import *

class Pokemon(ABC):
    def __init__(self,nombre,tipo,debilidad):
        self._nombre = nombre
        self._tipo = tipo
        self._vida = 100
        self._ataque = randint(0,100)
        self._defensa = randint(0,100)
        self._velocidad = randint(0,100)
        self._debilidad = debilidad
        self._salvajismo = randint(0,100)
    
    def getNombre(self):
        return self._nombre
    
    def getVida(self):
        return self._vida
    
    def setVida(self,valor):
        self._vida = valor
    
    def getSalvajismo(self):
        return self._salvajismo
    
    def getDebilidad(self):
        return self._debilidad
    
    def setSalvajismo(self,valor):
        self._salvajismo = valor
    
    def imprimir(self):
        print('Nombre:',self._nombre)
        print('Ataque:',self._ataque)
        print('Defensa:',self._defensa)
        print('Velocidad:',self._velocidad)
        print('Salvajismo:',self._salvajismo)
        print()
    
    def ataque(self,pokemon):
        probabilidad = randint(1,10)
        if self._tipo == pokemon.getDebilidad() and probabilidad < 8: #probabilidad del %70
            return self._ataque+self._ataque*0.5 #incrementa el ataque en %50
        else:
            return self._ataque
    
    def defensa(self,ataque):
        if ataque > self._defensa:
            self._vida -= ataque - self._defensa
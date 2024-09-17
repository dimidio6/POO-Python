from abc import ABC, abstractmethod
from random import *

class Pokemon(ABC):
    def __init__(self,nombre):
        self.__nombre = nombre
        self._tipo = None
        self.__vida = 100
        self._ataque = self.generar_atributos()
        self.__defensa = self.generar_atributos()
        self._velocidad = self.generar_atributos()
        self._debilidad = None
        self.__salvajismo = self.generar_atributos()

    def getSalvajismo(self):
        return self.__salvajismo
    
    def setSalvajismo(self,valor):
        self.__salvajismo = valor

    def getVida(self):
        return self.__vida

    def setVida(self,valor):
        self.__vida = valor
    
    def getNombre(self):
        return self.__nombre
    
    def generar_atributos(self):
        return randint(0,100)
    
    @abstractmethod
    def imprimir(self):
        print('Nombre:',self.__nombre)
        print('Ataque:',self._ataque)
        print('Defensa:',self.__defensa)
        print('Velocidad:',self._velocidad)
        print('Salvajismo:',self.__salvajismo)
        print()
    
    @abstractmethod
    def ataque(self,pokemon):
        probabilidad = randint(1,10)
        if self._tipo == pokemon._debilidad and probabilidad < 8: #probabilidad del %70
            return self._ataque+self._ataque*0.5 #incrementa el ataque en %50
        else:
            return self._ataque
    
    @abstractmethod
    def defensa(self,ataque):
        if ataque > self.__defensa:
            self.__vida -= ataque - self.__defensa
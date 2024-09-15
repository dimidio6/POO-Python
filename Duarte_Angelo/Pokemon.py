from abc import ABC, abstractmethod
from random import *

class Pokemon(ABC):
    def __init__(self,nombre):
        self.__nombre = nombre
        self._tipo = None
        self.__vida = 100
        self.__ataque = self.generar_atributos()
        self.__defensa = self.generar_atributos()
        self.__velocidad = self.generar_atributos()
        self._debilidad = None
        self.__salvajismo = self.generar_atributos()
    
    # @property
    # def getDebilidad(self):
    #     return self.__debilidad
    
    # @getDebilidad.setter
    # def setDebilidad(self,debilidad):
    #     self.__debilidad = debilidad
    
    @property
    def getSalvajismo(self):
        return self.__salvajismo
    
    @getSalvajismo.setter
    def setSalvajismo(self,valor):
        self.__salvajismo = valor
    
    @property
    def getVida(self):
        return self.__vida
    
    def generar_atributos(self):
        return randint(0,100)
    
    @abstractmethod
    def imprimir(self):
        print('Nombre:',self.__nombre)
        print('Defensa:',self.__ataque)
        print('Ataque:',self.__defensa)
        print('Ataque:',self.__velocidad)
        print('Ataque:',self.__salvajismo)
    
    @abstractmethod
    def ataque(self,pokemon):
        probabilidad = randint(1,10)
        if self._tipo == pokemon._debilidad and probabilidad < 8: #probabilidad del %70
            return self.__ataque+self.__ataque*0.5 #incrementa el ataque en %50
        else:
            return self.__ataque
    
    @abstractmethod
    def defensa(self,ataque):
        if ataque > self.__defensa:
            self.__vida -= ataque - self.__defensa
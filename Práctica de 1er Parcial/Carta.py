from abc import ABC,abstractmethod
from random import *

class Carta(ABC):
    def __init__(self,nombre,apellido,equipo,pais):
        self.__nombre = nombre + " " + apellido
        self.__equipo = equipo
        self.__pais = pais
        self._velocidad = self.asignar_atributo()
        self._tiro = self.asignar_atributo()
        self._regate = self.asignar_atributo()
        self._defensa = self.asignar_atributo()
        self._pase = self.asignar_atributo()
        self._fisico = self.asignar_atributo()
    
    @abstractmethod
    def imprimir(self):
        print('Nombre:',self.__nombre)
        print('Equipo:',self.__equipo)
        print('País:',self.__pais)
        print('-----------')
        print('Velocidad:',self._velocidad,' Defensa:',self._defensa)
        print('     Tiro:',self._tiro,'    Pase:',self._pase)
        print('   Regate:',self._defensa,'  Físico:',self._fisico)
    
    @abstractmethod
    def asignar_atributo(self):
        pass
    
    @abstractmethod
    def calcular_quimica(self,equipoFav,paisFav):
        if equipoFav == self.__equipo and paisFav == self.__pais:
            return 100
        elif equipoFav == self.__equipo or paisFav == self.__pais:
            return 80
        else:
            return 0
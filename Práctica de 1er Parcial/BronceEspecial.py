from Carta import Carta
from random import *

class BronceEspecial(Carta):
    def __init__(self, nombre, apellido, equipo, pais, habilidad):
        super().__init__(nombre, apellido, equipo, pais)
        self.__habilidad = habilidad
    
    def imprimir(self):
        super().imprimir()
        print('Habilidad:',self.__habilidad)
        print('==========================')
    
    def asignar_atributo(self):
        aleatorio = randint(49,65)
        return aleatorio+2 #suma del 2
    
    def calcular_quimica(self, equipoFav, paisFav):
        return super().calcular_quimica(equipoFav, paisFav)
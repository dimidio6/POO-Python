from Carta import Carta
from random import *

class Oro(Carta):
    def __init__(self, nombre, apellido, equipo, pais):
        super().__init__(nombre, apellido, equipo, pais)
    
    def imprimir(self):
        super().imprimir()
        print('==========================')
    
    def asignar_atributo(self):
        aleatorio = randint(74,90)
        return int(aleatorio*0.05+aleatorio) #suma del 5% base
    
    def calcular_quimica(self, equipoFav, paisFav):
        return super().calcular_quimica(equipoFav, paisFav)
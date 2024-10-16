from Docente import Docente
from NoDocente import NoDocente
from random import *

class Reloj:
    def __init__(self,lista):
        self.__lista = lista # lista de Personal
        
    def informe_horasMes(self):
        for personal in self.__lista:
            probabilidad = randint(1,100)
            if personal.sector == 'Docente':
                
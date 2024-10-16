from Controlar import Controlar
from abc import ABC, abstractmethod

class Contenido(Controlar,ABC):
    def __init__(self,nombre,año,calificacion):
        self.__nombre = nombre
        self.__año = año
        self.__calificacion = calificacion
    
    def reproducir(self):
        pass
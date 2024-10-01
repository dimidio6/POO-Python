from abc import ABC, abstractmethod

class Personal(ABC):
    def __init__(self,nombreCompleto,antiguedad,sector):
        self.__nombreCompleto: nombreCompleto
        self.__antiguedad: antiguedad
        self.__sector: sector
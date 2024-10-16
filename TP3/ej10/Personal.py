from abc import ABC, abstractmethod

class Personal(ABC):
    def __init__(self,nombreCompleto,antiguedad,sector):
        self._nombreCompleto: nombreCompleto
        self._antiguedad: antiguedad
        self._sector: sector
        self._horasTrabajadas = None
    
    def horasSemanales(self):
        pass
    
    def imprimir(self):
        print('Nombre:',self.__nombreCompleto)
        print('Antiguedad:',self.__antiguedad)
        print('Sector:',self.__sector)
    
    @property
    def sector(self):
        return self.__sector
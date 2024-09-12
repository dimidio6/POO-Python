from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self,vida,lvl_ataque,lvl_defensa):
        self._vida = vida
        self._lvl_ataque = lvl_ataque
        self._lvl_defensa = lvl_defensa
    
    @abstractmethod
    def atacar(self):
        return self._lvl_ataque
    
    @abstractmethod
    def defender(self,ataque):
        pass
    
    @abstractmethod
    def imprimir(self,nombre):
        print(nombre)
        print('Vida:',self._vida)
        print('Ataque:',self._lvl_ataque)
        print('Defensa:',self._lvl_defensa)
        print()
from abc import ABC,abstractmethod

class Cuenta(ABC):
    def __init__(self,saldo,dueño,nroCuenta):
        self._saldo = saldo
        self.__dueño = dueño
        self.__nroCuenta = nroCuenta
    
    @abstractmethod
    def debito(self,gasto):
        pass
    
    @abstractmethod
    def credito(self,gasto,cuotas,interes):
        match cuotas:
            case (1,2,3): self._saldo -= gasto/cuotas
            case (6,9,12):
                gastoCuota = (gasto/cuotas)
                self._saldo -= (gastoCuota+gastoCuota*interes) # se le agrega un interés
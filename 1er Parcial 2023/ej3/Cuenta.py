from abc import ABC,abstractmethod

class Cuenta(ABC):
    def __init__(self,saldo,dueño,nroCuenta):
        self._saldo = saldo
        self._dueño = dueño
        self._nroCuenta = nroCuenta
    
    def __verificarSaldo(self,gasto):
        if self._saldo - gasto < 0:
            print('Saldo insuficiente.')
        else:
            self._saldo -= gasto
            print('Pago realizado con éxito.')
    
    def debito(self,gasto):
        self.__verificarSaldo(gasto)
    
    @abstractmethod
    def credito(self,gasto,cuotas):
        self.__verificarSaldo(gasto)
    
    def getSaldo(self):
        return self._saldo
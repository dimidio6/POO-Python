from abc import ABC,abstractmethod

class Cuenta(ABC):
    def __init__(self,saldo,dueño,nroCuenta):
        self._saldo = saldo
        self._dueño = dueño
        self._nroCuenta = nroCuenta
    
    def __verificarSaldo(self,gasto):
        if self._saldo - gasto < 0:
            print('Pago = - $',gasto)
            print('Saldo insuficiente = $',self._saldo)
            print('Pago NO realizado.')
            print('------------------')
        else:
            print('Pago = - $',gasto)
            print('Saldo = $',self._saldo)
            self._saldo -= gasto
            print('Saldo actualizado = $',self._saldo)
            print('Pago realizado con éxito.')
            print('-------------------------')
    
    def debito(self,gasto):
        self.__verificarSaldo(gasto)
    
    @abstractmethod
    def credito(self,gasto,cuotas):
        self.__verificarSaldo(gasto)
    
    def getSaldo(self):
        return self._saldo
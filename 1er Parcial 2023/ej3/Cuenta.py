from abc import ABC
from Pagar import Pagar

class Cuenta(Pagar,ABC):
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
            print('Saldo = $',int(self._saldo))
            self._saldo -= gasto
            print('Saldo actualizado = $',int(self._saldo))
            print('Pago realizado con éxito.')
            print('-------------------------')
    
    def debito(self,gasto):
        self.__verificarSaldo(gasto)
    
    def credito(self,gasto):
        self.__verificarSaldo(gasto)
    
    def imprimirDatos(self):
        print('=================')
        print('Dueño:',self._dueño)
        print('Saldo = $',int(self._saldo))
        print('N° Cuenta:',self._nroCuenta)
        print('=================')
    
    def getSaldo(self):
        return self._saldo
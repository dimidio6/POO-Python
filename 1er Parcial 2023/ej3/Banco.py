from Cuenta import Cuenta

class Banco(Cuenta):
    def __init__(self, saldo, dueño, nroCuenta):
        super().__init__(saldo, dueño, nroCuenta)
        self.__cbu = None
    
    def debito(self, gasto):
        self._saldo -= gasto*0.1 # reintegro del %10
    
    def credito(self, gasto, cuotas, interes):
        return super().credito(gasto, cuotas, 0.02) # interés del %2
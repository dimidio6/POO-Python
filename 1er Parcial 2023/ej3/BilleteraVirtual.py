from Cuenta import Cuenta

class BilleteraVirtual(Cuenta):
    def __init__(self, saldo, dueño, nroCuenta):
        super().__init__(saldo, dueño, nroCuenta)
        self.__cvu = None
    
    def debito(self, gasto):
        self._saldo -= gasto
    
    def credito(self, gasto, cuotas, interes):
        return super().credito(gasto, cuotas, 0.08) # interés del %8
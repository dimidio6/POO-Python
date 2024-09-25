from Cuenta import Cuenta

class BilleteraVirtual(Cuenta):
    def __init__(self, saldo, dueño, nroCuenta):
        super().__init__(saldo, dueño, nroCuenta)
        self.__cvu = None
    
    def credito(self,gasto,cuotas):
        gastoCuota = gasto/cuotas
        super().credito(gastoCuota+gastoCuota*0.08,cuotas) # interés del 8%
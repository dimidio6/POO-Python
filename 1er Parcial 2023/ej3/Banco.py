from Cuenta import Cuenta

class Banco(Cuenta):
    def __init__(self, saldo, dueño, nroCuenta):
        super().__init__(saldo, dueño, nroCuenta)
        self.__cbu = None
    
    def debito(self,gasto):
        super().debito(gasto*0.9) # reintegro del %10
    
    def credito(self,gasto,cuotas):
        gastoCuota = gasto/cuotas
        match cuotas:
            case 1|2|3: super().credito(gastoCuota)
            case 6|9|12: super().credito(gastoCuota*1.02) # interés del 2%
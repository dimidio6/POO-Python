class Impuesto:
    def __init__(self,nombre,monto,periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado = 'Pendiente'
        self.__numComprobante = None
    
    def validarPago(self,monto,periodo,num_comprobante):
        if monto == self.__monto and periodo == self.__periodo:
            self.__estado = 'Cobrado'
            self.__numComprobante = num_comprobante
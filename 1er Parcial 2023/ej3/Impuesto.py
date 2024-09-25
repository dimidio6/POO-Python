class Impuesto:
    def __init__(self,nombre,monto,periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado = 'Pendiente'
        self.__numComprobante = None
    
    def validarPago(self,monto,mes,num_comprobante):
        if monto == self.__monto and mes == self.__periodo:
            self.__estado = 'Cobrado'
            self.__numComprobante = num_comprobante
    
    def getMonto (self):
        return self.__monto
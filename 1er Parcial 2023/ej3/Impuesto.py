class Impuesto:
    def __init__(self,nombre,monto,periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado = False # pendiente
        self.__numComprobante = None
    
    def validarPago(self,monto,mes,num_comprobante):
        if (monto == self.__monto) and (mes == self.__periodo):
            self.__estado = True # cobrado
            self.__numComprobante = num_comprobante
        print('Monto = $',monto)
        print('Mes:',mes)
        print('ESTADO:',self.__estado)
        print('Comprobante N°',self.__numComprobante)
        print('=================')
    
    def imprimir(self):
        print('Impuesto:',self.__nombre)
        print('=================')
        print('Monto = $',self.__monto)
        print('Mes:',self.__periodo)
        print('ESTADO:',self.__estado)
        print('Comprobante N°',self.__numComprobante)
        print('=---------------=')
    
    def getMonto (self):
        return self.__monto
    
    def getEstado(self):
        return self.__estado
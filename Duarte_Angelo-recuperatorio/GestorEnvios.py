from Cartero import Cartero
from Furgoneta import Furgoneta
from Paquete import Paquete

class GestorEnvios:
    def __init__(self):
        self.__transportes = []
    
    def gestionarEnvio(self,transportes,paquete,distancia):
        if paquete.mayorPeso() > Cartero.getPesoLimite():
            print('Gestionando el envío del paquete pesado:')
            print()
        else:
            print('Gestionando el envío del paquete liviano:')
            print()
        menorIndicador = 9999999
        for transporte in transportes:
            indicadorCosto = transporte.transportarPaquete(distancia,paquete.mayorPeso())
            if indicadorCosto < menorIndicador and indicadorCosto > 0:
                menorIndicador = indicadorCosto
        print('El mejor indicador de costo es',menorIndicador)
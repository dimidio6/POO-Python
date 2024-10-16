from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,tipo,pesoLimite,velocidad,valorKM):
        self._tipo = tipo
        self._pesoLimite = pesoLimite # kg
        self._velocidadPromedio = velocidad # km/h
        self._valorKM = valorKM # $
    
    def transportarPaquete(self,distancia,pesoPaquete,cantidadTiempo,cantidadCosto): # devuelve el costo de transporte
        if pesoPaquete > self._pesoLimite:
            return -1
        else:
            tiempo = self._velocidadPromedio * distancia
            costo = self._valorKM * distancia
            return cantidadTiempo * tiempo + cantidadCosto * costo # sus clases hijas utilizan la misma fórmula con distintos valores
    
    def getTipo(self):
        return self._tipo
    
    def getPesoLimite(self):
        return self._pesoLimite
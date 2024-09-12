from abc import ABC, abstractmethod

class TarifaProveedor(ABC):
    def __init__(self,totalSMS,totalMinutos,totalGigas):
        self._totalSMS = totalSMS
        self._totalMinutos = totalMinutos
        self._totalGigas = totalGigas
    
    @abstractmethod
    def getNombre(self):
        pass
    
    
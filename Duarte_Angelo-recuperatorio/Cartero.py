from Transporte import Transporte

class Cartero(Transporte):
    def __init__(self):
        super().__init__('Cartero',5,5,270)
    
    def transportarPaquete(self, distancia, pesoPaquete):
        return super().transportarPaquete(distancia,pesoPaquete,0.2,0.8)
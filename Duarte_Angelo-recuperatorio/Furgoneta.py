from Transporte import Transporte

class Furgoneta(Transporte):
    def __init__(self):
        super().__init__('Furgoneta',100,60,1000)
    
    def transportarPaquete(self, distancia, pesoPaquete):
        return super().transportarPaquete(distancia, pesoPaquete,0.7,0.3)
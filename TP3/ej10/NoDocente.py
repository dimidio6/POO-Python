from Personal import Personal
import random

jornada = ['Completa','Reducida']

class NoDocente(Personal):
    def __init__(self, nombreCompleto, antiguedad):
        super().__init__(nombreCompleto, antiguedad, 'No docente')
        self.__jornada = random.choice(jornada)
    
    def horasSemanales(self):
        match self.__jornada:
            case 'Completa': return 30
            case 'Reducida': return 20
    
    def imprimir(self):
        super().imprimir()
        print('Jornada:',self.__jornada)
        print('-----------------------')
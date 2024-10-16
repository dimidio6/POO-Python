from Personal import Personal
import random

categoria = ['Simple','Semiexclusiva','Exclusiva']

class Docente(Personal):
    def __init__(self, nombreCompleto, antiguedad):
        super().__init__(nombreCompleto, antiguedad, 'Docente')
        self.__categoria = random.choice(categoria)
    
    def horasSemanales(self):
        match self.__categoria:
            case 'Simple': return 10
            case 'Semiexclusiva': return 20
            case 'Exclusiva': return 40
    
    def imprimir(self):
        super().imprimir()
        print('Categoría:',self.__categoria)
        print('-----------------------')
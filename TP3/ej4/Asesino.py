from Personaje import Personaje

class Asesino(Personaje):
    def __init__(self,lvl_ataque,lvl_defensa):
        super().__init__(100,lvl_ataque,lvl_defensa)
    
    def atacar(self):
        return self._lvl_ataque + 20
    
    def defender(self, ataque):
        if ataque > self._lvl_defensa:
            self._vida = self._vida - (ataque - self._lvl_defensa)
            print('------------------------------')
            print('DAÑO ENTRANTE: -',ataque)
            print('DAÑO BLOQUEADO: ',self._lvl_defensa)
            print('------------------------------')
    
    def imprimir(self, nombre):
        return super().imprimir(nombre)
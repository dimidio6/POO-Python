from Personaje import Personaje

class Caballero(Personaje):
    def __init__(self,lvl_ataque,lvl_defensa):
        super().__init__(200,lvl_ataque,lvl_defensa)
    
    def atacar(self):
        return super().atacar()
    
    def defender(self, ataque):
        defensa_especial = 10
        if ataque > (self._lvl_defensa*2): # si el ataque es > al doble de la defensa, reduce el daño recibido en 10
            self._vida = self._vida - (ataque - (self._lvl_defensa + defensa_especial))
            print('------------------------------')
            print('DAÑO CRÍTICO = -',ataque)
            print(f'DEFENSA ESPECIAL = ',{self._lvl_defensa+defensa_especial})
            print('------------------------------')
        elif ataque > self._lvl_defensa: # si el ataque es > al lvl_defensa baja la cantidad de vida
            self._vida = self._vida - (ataque - self._lvl_defensa)
            print('------------------------------')
            print('DAÑO ENTRANTE = -',ataque)
            print('DAÑO BLOQUEADO = ',self._lvl_defensa)
            print('------------------------------')
            
    def imprimir(self, nombre):
        return super().imprimir(nombre)
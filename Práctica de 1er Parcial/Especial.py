from Carta import Carta
import random

class Especial(Carta):
    def __init__(self, nombre, apellido, equipo, pais, lista_hab):
        super().__init__(nombre, apellido, equipo, pais)
        self.__habilidades = self.setear_habilidades(lista_hab)
    
    def setear_habilidades(self,lista):
        lista_nueva = []
        for i in range(1,random.randint(2,len(lista))): #cantidad aleatoria de habilidades (entre 1 y máx) q voy a agregar de la lista original
            habilidad_elegida = random.choice(lista) #elijo una habilidad aleatoria
            if not habilidad_elegida in lista_nueva: #la agrego solo si ya no fue agregada, para evitar repeticiones
                lista_nueva.append(habilidad_elegida)
        return lista_nueva
    
    def imprimir(self):
        super().imprimir()
        print('Habilidades:',", ".join(self.__habilidades))
        print('==========================')
    
    def asignar_atributo(self):
        aleatorio = random.randint(89,99)
        if aleatorio > 97:
            return 99
        else:
            return int(aleatorio*0.02+aleatorio) #suma del 2% base
    
    def calcular_quimica(self, equipoFav, paisFav): #no utilizo los parámetros pero igual los incluyo para tener Polimorfismo DINÁMICO
        return 100
from Carta import Carta

class Plantilla:
    def __init__(self,usuario,paisFav,equipoFav):
        self.__usuario = usuario
        self.__paisFav = paisFav
        self.__equipoFav = equipoFav
        self.__plantel = []
    
    def imprimir(self):
        print(self.__usuario)
        print('País:',self.__paisFav)
        print('Equipo:',self.__equipoFav)
        print('Química =',self.quimica_total())
        print('==========================')
        print()
        for carta in self.__plantel:
            carta.imprimir()
    
    def agregar_carta(self,carta):
        if len(self.__plantel) < 11: # len devuelve la cantidad de elementos
            self.__plantel.append(carta)
    
    def quimica_total(self):
        quimica = 0
        for jugador in self.__plantel:
            quimica += jugador.calcular_quimica(self.__equipoFav,self.__paisFav)
        return int(quimica/len(self.__plantel))
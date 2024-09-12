from Caballero import Caballero
from Asesino import Asesino

logan = Caballero(30,50)
randal = Asesino(60,30)
logan.imprimir("Logan")
randal.imprimir("Randal")
logan.defender(randal.atacar())
logan.imprimir("Logan")
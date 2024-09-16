from Hierba import Hierba
from Fuego import Fuego
from Agua import Agua
from Entrenador import Entrenador
import random

nombres = ['pokemon1','pokemon2','pokemon3','pokemon4','pokemon5','pokemon6','pokemon7','pokemon8','pokemon9','pokemon10','pokemon11','pokemon12']
pokemones = [] #lista de TODOS los pokemones

for i in range(1,10):
    tipo_pokemon = random.randint(1,3)
    match tipo_pokemon:
        case 1: nuevoPokemon = Hierba(random.choice(nombres))
        case 2: nuevoPokemon = Fuego(random.choice(nombres))
        case 3: nuevoPokemon = Agua(random.choice(nombres))
    pokemones.append(nuevoPokemon) #lleno la lista con 10 pokemones

entrenador1 = Entrenador('Ash',random.choice(pokemones)) #el pokemón principal del entrenador se asigna aleatoriamente

for combate in range(0,3): # *
    entrenador1.atraparPokemon(random.choice(pokemones)) # **
print('=======================')
entrenador1.imprimir()

# COSAS A AGREGAR
#   - *: debería hacer un for de 10 para intentar atrapar los de 10 pokemones creados. Tengo q cambiar la asignación de nombres
#   - **: podría modificarse para que el random no haga atrapar a un pokemón que ya tengo en mi pokedex
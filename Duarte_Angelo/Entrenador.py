from random import *
from Hierba import Hierba
from Fuego import Fuego
from Agua import Agua

class Entrenador:
    def __init__(self,nombre,pokemonMain):
        self.__nombre = nombre
        self.__nivel = randint(1,100)
        self.__pokemonMain = pokemonMain
        self.__pokedex = []
    
    def atraparPokemon(self,pokemonDisputado):
        print('----- INICIO DE COMBATE -----')
        print()
        print('/// POKEMÓN A CAPTURAR ///')
        pokemonDisputado.imprimir()
        print('/// POKEMÓN UTILIZADO ///')
        self.__pokemonMain.imprimir()
        salvajismoActual = pokemonDisputado.getSalvajismo()
        capturado = False #variable para evitar capturarlo + de una vez en el for
        if self.__nivel > salvajismoActual:
            self.__pokedex.append(pokemonDisputado) #si tiene el nivel requerido lo captura directamente
            capturado = True
            print("Pokemón atrapado con éxito!")
        else:
            for turno in range(1,3): #el Pokemón del Entrenador realiza ataques y el contrario defiende durante 3 turnos
                pokemonDisputado.defensa(self.__pokemonMain.ataque(pokemonDisputado))
                salvajismoActual -= salvajismoActual*0.1 #en cada ataque disminuyo el Salvajismo en %10
                pokemonDisputado.setSalvajismo(salvajismoActual) #actualizo el valor en el Pokemón
                if pokemonDisputado.getVida() > 0 and self.__nivel > salvajismoActual and not capturado: #mientras esté vivo, si el salvajismo disminuye lo suficiente lo captura
                    self.__pokedex.append(pokemonDisputado)
                    capturado = True
                    print("Pokemón atrapado con éxito!")
        if not capturado:
            print("Falló la captura :(")
        print()
    
    def imprimir(self):
        print('Entrenador:',self.__nombre)
        print('     Nivel:',self.__nivel)
        print('POKEDEX:')
        print(self.__pokemonMain.getNombre())
        for pokemon in self.__pokedex:
            print(pokemon.getNombre())
        print('--------------')
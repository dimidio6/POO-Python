from BronceEspecial import BronceEspecial
from Oro import Oro
from Especial import Especial
from Plantilla import Plantilla
import random

usuarios = ['pepe','_SamuelValenciano_','patrick','entrenador1']
nombres = ['Luis','Juan','Germán','Lucas','Alfredo','Franco','Herb','Julián']
apellidos = ['Pérez','Benitez','Martínez','Carrasco','Figueroa','Rodríguez','Fernández','Alvarez']
habilidades = ['Ataque','Pase','Defensa']
clubes = ['Arsenal','Montevideo City Torque','Inter Miami','Manchester City']
paises = ['Argentina','Inglaterra','Holanda','Japón']

plantilla1 = Plantilla(random.choice(usuarios),random.choice(paises),random.choice(clubes))
plantilla2 = Plantilla(random.choice(usuarios),random.choice(paises),random.choice(clubes))
cartas = []

for jugador in range(0,22):
    tipo_Carta = random.randint(1,3)
    match tipo_Carta:
        case 1:
            carta = BronceEspecial(random.choice(nombres),random.choice(apellidos),random.choice(clubes),random.choice(paises),random.choice(habilidades))
        case 2:
            carta = Oro(random.choice(nombres),random.choice(apellidos),random.choice(clubes),random.choice(paises))
        case 3:
            carta = Especial(random.choice(nombres),random.choice(apellidos),random.choice(clubes),random.choice(paises),habilidades)
    cartas.append(carta)

random.shuffle(cartas)

for jugador in cartas[0:11]:        
    plantilla1.agregar_carta(jugador)
for jugador in cartas[11:22]:
    plantilla2.agregar_carta(jugador)
    
print('-------------------------------PLANTILLA 1-------------------------------')
plantilla1.imprimir()
print()
print('-------------------------------PLANTILLA 2-------------------------------')
plantilla2.imprimir()
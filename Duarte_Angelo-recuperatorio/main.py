from Paquete import Paquete
from Cartero import Cartero
from Furgoneta import Furgoneta
from GestorEnvios import GestorEnvios

paqueteLivano = Paquete(3,10,20,10)
paquetePesado = Paquete(25,30,10,50)

cartero1 = Cartero()
furgoneta1 = Furgoneta()
lista = [cartero1,furgoneta1]

GestorEnvios.gestionarEnvio()



# Para la abstracción de Transporte utilicé una clase abstracta ya que observe que tanto Cartero cómo Furgoneta compartian atributos,
# que luego solo ingrese cómo parámetros en el super.

# La otra forma en la que podría hacerse sería con una interfaz Transportar en la que se defina el método transportarPaquete y se
# implemente en las clases Cartero y Furgoneta, ya que ambas sabrian hacer esto.
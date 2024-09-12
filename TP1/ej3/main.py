from Serie import Serie #Importa al main la clase Serie del archivo Serie
from Cartelera import Cartelera #importa la Clase Cartelera

serie1 = Serie("Avatar","link","Estreno todos los martes") #instancio un objeto serie1 de la clase Serie
serie2 = Serie("Billy y Mandy", "link2", "Estreno todos los miércoles")
serie3 = Serie("Los simpsons", "link3", "Estreno todos los jueves")
cartelera = Cartelera("Estreno semanal") #instancio un objeto cartelera de la clase Cartelera
cartelera.agregar_serie(serie1) #utilizo el método agregar_serie de la clase Cartelera
cartelera.agregar_serie(serie2)
cartelera.agregar_serie(serie3)
cartelera.imprimir()
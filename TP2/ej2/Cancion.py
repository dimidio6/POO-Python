class Cancion:
    def __init__(self): #El constructor que faltaba
        #todos los atributos privados
        self.__nombre = ''
        self.__autor = ''
        self.__duracion = 0.0
    
    #los getters y setters que faltan para realizar las asignaciones e impresiones de atributos privados
    
    #nombre
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self.__nombre = nombre
        
    #autor
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor (self, autor):
        self.__autor = autor
        
    #duracion
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion (self, duracion):
        self.__duracion = duracion
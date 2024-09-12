class Persona:
    def __init__(self,nombre,apellido,nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nacimiento = nacimiento
    
    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self,nombre):
        self.__nombre = nombre
    
    @property
    def apellido (self):
        return self.__apellido
    
    @apellido.setter
    def apellido (self,apellido):
        self.__apellido = apellido
    
    @property
    def nacimiento (self):
        return self.__nacimiento
    
    @nacimiento.setter
    def nacimiento (self,nacimiento):
        self.__nacimiento = nacimiento
    
    def toString (self):
        return (self.__nombre+" "+self.__apellido+" - "+self.__nacimiento)
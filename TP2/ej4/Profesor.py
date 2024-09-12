class Profesor:
    
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    
    def iniciar(self): #borré la inicialización de nombre y apellido
        self.__materia = []
        return self
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    def get_apellido(self):
        return self.__apellido
    
    def set_materia(self,materia):
        self.__materia = materia
    
    def get_materia(self):
        return self.__materia
    
    def add_materia(self,materia):
        self.__materia.append(materia)
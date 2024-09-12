class Persona:
    
    def __init__(self,nombre,apellido,edad,sexo,estudia,trabaja):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sexo = sexo
        self.__estudia = estudia
        self.__trabaja = trabaja
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    def get_sexo(self):
        return self.__sexo
    
    def get_trabaja(self):
        return self.__trabaja
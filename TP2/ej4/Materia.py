class Materia:
    
    def __init__(self,nombre,codigo):
        self.__nombre = nombre
        self.__codigo = codigo
    
    def getnombre (self):
        return self.__nombre #retorna el nombre
    
    def set_nombre (self, nombre):
        self.__nombre = nombre
    
    def set_codigo (self, codigo):
        self.__codigo = codigo
        
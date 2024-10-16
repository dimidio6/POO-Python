class Usuario:
    def __init__(self,nombre,apellido,mail,password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__password = password
        self.__perfiles = []
        
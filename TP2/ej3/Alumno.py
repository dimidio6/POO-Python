class Alumno:
    def __init__(self): #Constructor que crea un objeto sin nada
        pass
    
    #inicializador
    def iniciar(self):
        self.__nombre = ''
        self.__apellido = ''
        self.__dni = 0
        return self
    
    #Otra forma de hacer un Constructor
    @classmethod
    def iniciar_con_nom_ape(cls, nombre, apellido):
        alumno = cls.__new__(cls)
        alumno.__nombre = nombre
        alumno.__apellido = apellido
        return alumno
    
    def setNombre (self, nombre):
        self.__nombre = nombre
    
    def setApellido (self, apellido):
        self.__apellido = apellido
    
    def setDni (self, dni):
        self.__dni = dni
    
    def getNombreYapellido (self):
        return (self.__nombre + " " + self.__apellido)
    
    def getDni (self):
        return self.__dni
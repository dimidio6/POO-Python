class Curso:
    def __init__(self, titulo, capacitador, valoracion, precio):
        self.__titulo = titulo
        self.__capacitador = capacitador
        self.__valoracion = valoracion
        self.__precio = precio
        self.__categoria = None
    
    @property #Getter del atributo privado categoria
    def categoria(self):
        return self.__categoria
    
    @categoria.setter #Setter de categoria
    def categoria(self, nombre):
        self.__categoria = nombre
    
    def imprimir (self):
        print("Título:",self.__titulo)
        print("Capacitador:",self.__capacitador)
        print("Valoración:",self.__valoracion)
        print("Precio:",self.__precio)
        if not self.__categoria == None:
            print(self.__categoria)
        print("")
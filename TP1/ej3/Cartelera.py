class Cartelera:
    def __init__(self, categoria):
        self.__categoria = categoria
        self.__lista_series = [] #inicializa una Lista vacía
    
    def agregar_serie (self, serie):
        self.__lista_series.append(serie) #agrega el parámetro serie que entró, a la Lista lista_series
        
    def imprimir(self):
        print(self.__categoria) #imprime el nombre de la categoría
        for i in self.__lista_series: #imprime los elementos de la lista
            i.imprimir() #utiliza el imprimir de la Class Serie
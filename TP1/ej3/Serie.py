class Serie: #la 1er letra de la CLASE con Mayúscula para diferenciarla
    def __init__(self, nombre, urlimg, estreno): #Constructor, Self siempre es el 1er parámetro
        self.__nombre = nombre #privado
        self.__urlimg = urlimg #privado
        self.__estreno = estreno #privado
    
    def imprimir(self):
        print("{}     {}     {}".format(self.__nombre, self.__urlimg, self.__estreno)) # {} me permite agregar espacios entre cada parámetro
        
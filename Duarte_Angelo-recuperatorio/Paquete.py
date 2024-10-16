class Paquete:
    def __init__(self,peso,alto,ancho,longitud):
        self.__peso = peso
        self.__dimensiones = alto*ancho*longitud
        self.__pesoVolumetrico = (alto*ancho*longitud)/5000 # cm
    
    def __str__(self):
        print('Peso =',self.__peso)
        print('Dimensiones =',self.__dimensiones)
        print('Peso volumétrico =',self.__pesoVolumetrico)
    
    def mayorPeso(self): # retorna el mayor peso del paquete
        if self.__peso > self.__pesoVolumetrico:
            return self.__peso
        else:
            return self.__pesoVolumetrico
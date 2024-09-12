class Comuna:
    
    def __init__(self):
        self.__familias = []
    
    def agregar(self,familia):
        self.__familias.append(familia)
    
    def cantidad_familia(self):
        contador = 0
        for familia in self.__familias:
            contador = contador + 1
        return contador
    
    def cantidad_trabaja_com(self):
        contador = 0
        for familia in self.__familias:
            contador = contador + familia.cantidad_trabaja_fam()
        return contador
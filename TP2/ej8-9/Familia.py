class Familia:
    
    def __init__(self):
        self.__integrantes = []
    
    def agregar(self,persona):
        self.__integrantes.append(persona)
    
    def eliminar(self,persona):
        self.__integrantes.remove(persona)
    
    def get_integrantes(self):
        return self.__integrantes
    
    def cantidad(self):
        contador = 0
        for persona in self.__integrantes:
            contador = contador + 1
        return contador
    
    def sumatoria_edad(self):
        sumatoria = 0
        for persona in self.__integrantes:
            sumatoria = sumatoria + persona.get_edad()
        return sumatoria
    
    def cantidad_trabaja_fam(self):
        contador = 0
        for persona in self.__integrantes:
            if persona.get_trabaja():
                contador = contador + 1
        return contador
    
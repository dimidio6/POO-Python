from Profesor import Profesor

class Titular(Profesor):
    def __init__(self, nombre, apellido, edad, horasTrabajadas,antiguedad):
        super().__init__(nombre, apellido, edad, horasTrabajadas)
        self._valorHora = 300.00 #accedo al atributo valorHora que está en la clase abstracta y lo seteo para la class Titular
        self.__valorAntiguedad = 1000.00 #propio de la class Titular
        self.__antiguedad = antiguedad #propio de la class Titular
    
    def get_remuneracion_antiguedad(self):
        return self.__valorAntiguedad * self.__antiguedad
    
    def get_nombre(self):
        return super().get_nombre()
    
    def get_apellido(self):
        return super().get_apellido()
    
    def get_horas_trabajadas(self):
        return super().get_horas_trabajadas()
    
    def get_remuneracion_mensual(self):
        return (self._valorHora * self.get_horas_trabajadas()) + self.get_remuneracion_antiguedad()
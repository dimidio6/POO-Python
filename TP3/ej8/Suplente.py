from Profesor import Profesor

class Suplente(Profesor):
    def __init__(self, nombre, apellido, edad, horasTrabajadas):
        super().__init__(nombre, apellido, edad, horasTrabajadas)
        self._valorHora = 200.00
    
    def get_nombre(self):
        return super().get_nombre()
    
    def get_apellido(self):
        return super().get_apellido()
    
    def get_horas_trabajadas(self):
        return super().get_horas_trabajadas()
    
    def get_remuneracion_mensual(self):
        return self._valorHora * self.get_horas_trabajadas()
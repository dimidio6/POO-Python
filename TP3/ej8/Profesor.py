from abc import ABC, abstractmethod

class Profesor(ABC):
    def __init__(self,nombre,apellido,edad,horasTrabajadas):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.__horasTrabajadas = horasTrabajadas
        self._valorHora = None
    
    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    def get_horas_trabajadas(self):
        return self.__horasTrabajadas
    
    def get_remuneracion_mensual(self):
        pass
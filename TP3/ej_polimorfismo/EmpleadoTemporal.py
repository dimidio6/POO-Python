from Empleado import Empleado

class EmpleadoTemporal(Empleado):
    
    def __init__(self,nombre,sueldo_por_hora,horas_trabajadas):
        self.__nombre = nombre
        self.__sueldo_por_hora = sueldo_por_hora
        self.__horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        salario = self.__sueldo_por_hora*self.__horas_trabajadas
        return salario
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.__nombre}')
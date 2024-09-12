from Empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    
    def __init__(self,nombre,sueldo_anual):
        self.__nombre = nombre
        self.__sueldo_anual = sueldo_anual
    
    def calcular_salario(self):
        salario = self.__sueldo_anual/12
        return salario
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.__nombre}')
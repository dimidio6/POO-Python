class Empresa:
    
    def __init__(self,nombre,direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleados = []
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,direccion):
        self.__direccion = direccion
    
    def agregar_empleado(self,empleado):
        self.__empleados.append(empleado)
    
    def total_empleados(self):
        total = 0
        for empleado in self.__empleados:
            total += 1 # lo mismo que: total = total + 1
        return total
    
    def imprimir_datos(self):
        print("Lista de empleados")
        for empleado in self.__empleados:
            print(" ")
            print(empleado.get_nombre(),empleado.get_apellido())
            print("Edad: ",empleado.get_edad())
            print("Sexo: ",empleado.get_sexo())
            
from Empresa import Empresa
from Persona import Persona

empresa = Empresa("Empresa genérica","Los perales 544")
empleado1 = Persona("Juan","Fernández",39,"H",False,True)
empleado2 = Persona("Camila","Pérez",40,"M",False,True)
empleado3 = Persona("Laura","Sanchez",30,"M",True,True)
empleado4 = Persona("Carlos","Rodriguez",27,"H",True,True)
empleado5 = Persona("Paticia","Cardenas",32,"M",False,True)
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)
empresa.agregar_empleado(empleado3)
empresa.agregar_empleado(empleado4)
empresa.agregar_empleado(empleado5)
print(f'{"Total de empleados: "}{empresa.total_empleados()}')
print(" ")
empresa.imprimir_datos()
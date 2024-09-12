from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto
from EmpleadoTemporal import EmpleadoTemporal

empleados = [EmpleadoTiempoCompleto("Fernando",3840000),EmpleadoTemporal("Juan",1500,190),EmpleadoTemporal("Franco",1800,195)]

for empleado in empleados:
    empleado.mostrar_informacion()
    print(f'Salario: {empleado.calcular_salario()}')
    print()
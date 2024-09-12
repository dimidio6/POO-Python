from Titular import Titular
from Suplente import Suplente

titulares = []
titulares.append(Titular("Aldana","Gutierrez",40,40,15))
titulares.append(Titular("Pedro","Perez",30,30,4))
titulares.append(Titular("Maria","Gomez",29,40,1))

suplentes = []
suplentes.append(Suplente("Tomás","Sosa",28,40))
suplentes.append(Suplente("Luciana","Torres",35,10))

for titular in titulares:
    print("Nombre y Apellido {} {}".format(titular.get_nombre(),titular.get_apellido()))
    print("Es titular? Si")
    print("Remuneración: {}".format(titular.get_remuneracion_mensual()))

print ("--------------------------------")

for suplente in suplentes:
    print("Nombre y Apellido {} {}".format(suplente.get_nombre(),suplente.get_apellido()))
    print("Es titular? No")
    print("Remuneración: {}".format(suplente.get_remuneracion_mensual()))

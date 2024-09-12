from Materia import Materia
from Profesor import Profesor

poo = Materia("POO","IF153")
algebra = Materia("Algebra","183")
introduccion = Materia("Introducción a la Computación","IF300")
algoritmica = Materia("Algorítmica","500")

profesores = []

profesor1 = Profesor("Pedro","Hernández")
profesor1.iniciar() #faltaba iniciar para agregar materias
profesor1.add_materia(poo)
profesor1.add_materia(algebra)
profesores.append(profesor1) #append
profesor2 = Profesor("Romina","Alvarez")
profesor2.iniciar() #faltaba iniciar
profesor2.add_materia(introduccion)
profesor2.add_materia(algoritmica)
profesores.append(profesor2)
profesor3 = Profesor("Laura","Pérez")
profesor3.iniciar()
profesores.append(profesor3)

for pro in profesores:
    print (f'{"Profesor: "}{pro.get_apellido()}{" "}{pro.get_nombre()}')
    print ("Materias:")
    for mat in pro.get_materia():
        print(f'{mat.getnombre()}')
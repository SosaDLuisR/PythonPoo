from cosas import *

def main():
    per1 = Persona("José", 19)
    print(per1)
    print(Persona.descripcion)

    print("------ herencia alumno --------")
    al1 = Alumno("José", 19, "564464646849", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("------------- herencia profesor -------------")
    profe1 = Profesor("Jesus", 30+16, "151616156", "Ing de Softwware")
    print(profe1)
    profe1.dormir()

    print("-------------- herencia ayudante profe ----------------")
    ayudante = AyudanteProfesor("Adrián", 28, "54645646", "ICO", 156465465, "Ing. de Software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")

main()
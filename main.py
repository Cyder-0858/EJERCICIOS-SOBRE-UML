from Ejercicio_1 import Circulo, Rectangulo, Cuadrado, Elipse
from Ejercicio_2.Persona import Persona


if __name__ == "__main__":
    #EJERCICIO 1
    print("EJERCICIO 1")
    c1 = Circulo(1, 5, "rojo")
    r1 = Rectangulo(1, 4, 6, "azul")
    q1 = Cuadrado(1, 4, "verde")
    e1 = Elipse(1, 5, 3, "amarillo")
    c2= Circulo(2, 10, "celeste")

    print(c1)
    print(r1)
    print(q1)
    print(e1)
    print(c2)

    #EJERCICIO 2
    print("\nEJERCICIO 2")
    p1 = Persona("Kate","Windsor", "Middleton", "Mujer")
    p2 = Persona("Guillermo","Windsor", "Gales", "Hombre")
    p3 = Persona("Diana","Windsor", "Spencer", "Mujer")
    p4 = Persona("Carlos","Windsor", "Gales", "Hombre")

    print(p2)
    print(p2.casado_con(p1))
    print(p2.es_hijo_de(p4,p3))


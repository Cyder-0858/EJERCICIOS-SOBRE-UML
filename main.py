from Ejercicio_1.Figuras import Circulo, Rectangulo, Cuadrado, Elipse
from Ejercicio_2.Persona import Persona
from Ejercicio_3.Cuadro import Cuadro
from Ejercicio_4.Edificio import Edificio
from Ejercicio_5.Figurass import Circuloo, Rectanguloo, Cuadradoo, Elipsee
from Ejercicio_6.Personaa import Personaa   


if __name__ == "__main__":
    #EJERCICIO 1
    print("\nEJERCICIO 1")
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
 
    #EJERCICIO 3
    print("\nEJERCICIO 3")
    cuadro1 = Cuadro("La Gioconda", "1503-1516", "Oleo", "Sfumato", "Madera de álamo", "leonardo da Vinci", "Regular")
    cuadro2 = Cuadro("Gioconda de El Prado", "1519-1516", "Oleo", "Pincelada Simple", "Madera de nogal", "Leonardo da Vinci", "Buena")

    print(cuadro1)
    print(cuadro1.localizado_en("Museo del Louvre"))

    print(cuadro2)
    print(cuadro2.replica_de("La Gioconda"))
    print(cuadro2.localizado_en("Museo del Prado"))

    #EJERCICIO 4
    print("\nEJERCICIO 4")

    Edificio1 = Edificio("Catedral de Santiago de Compostela", "Católico", "Santiago de Compostela", "1075", "1128", "1128", "1211", "Granito", "Románico")
    
    print(Edificio1)
    
    #EJERCICIO 5
    print("\nEJERCICIO 5")

    c1 = Circuloo(1, 5, "rojo")
    r1 = Rectanguloo(1, 4, 6, "azul")
    q1 = Cuadradoo(1, 4, "verde")
    e1 = Elipsee(1, 5, 3, "amarillo")
                 
    print(c1)
    print(r1)
    print(q1)
    print(e1)

    #EJERCICIO 6
    print("\nEJERCICIO 6")

    persona1 = Personaa("Juan", "Pérez", 30, "Masculino", "12345678A")

    print(persona1)

    #EJERCICIO 7
    print("\nEJERCICIO 7")

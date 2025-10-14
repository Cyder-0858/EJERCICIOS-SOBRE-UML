from Ejercicio_1.Figuras import Circulo, Rectangulo, Cuadrado, Elipse
from Ejercicio_2.Persona import Persona
from Ejercicio_3.Cuadro import Cuadro
from Ejercicio_4.Edificio import Edificio
from Ejercicio_5.Figurass import Circuloo, Rectanguloo, Cuadradoo, Elipsee
from Ejercicio_6.Personaa import Personaa   
from Ejercicio_7.ejercicio7 import Proyecto, miembro_del_equipo, lugar_de_Actuacion
from Ejercicio_8.Arqueologia import actuacion_arqueologica
from Ejercicio_9.Pintura import TipoTecnica, TipoSub_tecnica, TipoMaterial, TipoEstado_Conservacion, Pintura
from Ejercicio_10.Asociaciones_7 import Personaaaa, Proyectoooo, Lugar
from Ejercicio_11.CuadrosACR import cuadro11, museo11
from Ejercicio_12.estructura_arqueologica import EstructuraArqueologica
from Ejercicio_13.Poli import Punto, Poligono
from Ejercicio_14.bellingham import punto_I, Triangulo






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

    proyecto1 = Proyecto(1, "Desarrollo de Software", "2023-01-01", "2023-12-31")
    miembro1 = miembro_del_equipo(1, "Ana", "García", "Desarrolladora")
    lugar1 = lugar_de_Actuacion(1, "Oficina Central", "Madrid")
    miembro10 = miembro_del_equipo(1," Antonio","Lopez","Operario")
    miembro2 = miembro_del_equipo(2, "Luis", "Martínez", "Gestor de Proyecto")
    proyecto2 = Proyecto(2, "Investigación Médica", "2022-03-15", "2023-08-20")
    miembro3 = miembro_del_equipo(3, "María", "López", "Investigadora")
    lugar2 = lugar_de_Actuacion(2, "Laboratorio Norte", "Barcelona")
    miembro4 = miembro_del_equipo(4, "Pedro", "Sánchez", "Coordinador")
    proyecto3 = Proyecto(3, "Construcción de Puente", "2021-06-01", "2024-01-31")
    miembro5 = miembro_del_equipo(5, "Lucía", "Fernández", "Ingeniera Civil")
    lugar3 = lugar_de_Actuacion(3, "Zona Río", "Sevilla")
    miembro6 = miembro_del_equipo(6, "Javier", "Ruiz", "Supervisor")
    proyecto4 = Proyecto(4, "Campaña Publicitaria", "2023-02-10", "2023-11-30")
    miembro7 = miembro_del_equipo(7, "Sofía", "Torres", "Creativa")
    lugar4 = lugar_de_Actuacion(4, "Agencia Creativa", "Valencia")
    miembro8 = miembro_del_equipo(8, "Miguel", "Gómez", "Director de Arte")

        #AGRUPACION POR id --- NO SE PIDE EN EL ENUNCIADO, ME ABURRIA --------------------
    todos = [obj for obj in globals().values() 
            if isinstance(obj, (Proyecto, miembro_del_equipo, lugar_de_Actuacion))]
        
    ids = {}
    for obj in todos:
        ids.setdefault(obj.id, []).append(obj)

    for grupo in ids.values():
        if len(grupo) >= 3:  # al menos un proyecto, un miembro y un lugar
            for o in grupo:
                print(o)
            print("---")
        #----------------------------------------------------------------------------------

    #EJERCICIO 8
    print("\nEJERCICIO 8")

    actuacion1 = actuacion_arqueologica("2023-01-01", "2023-06-30", "6 meses", "excavación")
    actuacion2 = actuacion_arqueologica("2023-07-01", "2023-12-31", "6 meses", "sondeo")
    actuacion3 = actuacion_arqueologica("2024-01-01", "2024-06-30", "6 meses", "seguimiento")
    actuacion4 = actuacion_arqueologica("2024-07-01", "2024-12-31", "6 meses", "restauración")  # Tipo inválido    

    print(actuacion1)
    print(actuacion2)
    print(actuacion3)
    print(actuacion4)  # Tipo inválido

    #EJERCICIO 9
    print("\nEJERCICIO 9")

    pintura1 = Pintura("La Gioconda", "Retrato de Lisa Gherardini", "Leonardo da Vinci", "Museo del Louvre", "Si" ,TipoTecnica.OLEO, TipoSub_tecnica.SFUMATO, TipoMaterial.MADERA_DE_ALAMO, TipoEstado_Conservacion.REGULAR)
    print(pintura1)

    #EJERCICIO 10
    print("\nEJERCICIO 10")

    proyectoA = Proyectoooo("Proyecto Beta", "2024-01-01", "2024-12-31")
    print(proyectoA)
    personaA = Personaaaa(proyectoA, "Juan", "Pérez", "Analista")
    print(personaA)
    lugarA = Lugar(personaA, "Oficina Sur", "Sevilla")
    print(lugarA)


    #EJERCICIO 11
    print("\nEJERCICIO 11")

    museo1 = museo11("Museo del Prado", "Madrid")
    museo2 = museo11("Museo del Louvre", "París")
    cuadro1 = cuadro11("La Gioconda", "Óleo", "Da Vinci", museo2)
    cuadro2 = cuadro11("Las Meninas", "Óleo", "Velazquez", museo1)

    print(museo1)
    print(museo2)
    
    #agregar cuadros a los museos
    museo1.agregar_cuadro(cuadro2)
    print(museo1)
    museo2.agregar_cuadro(cuadro1)
    print(museo2)

    print(cuadro1)
    print(cuadro2)

    #EJERCICIO 12
    print("\nEJERCICIO 12")

    # Crear estructuras simples
    estructura1 = EstructuraArqueologica("E001", "Siglo I", ["piedra", "madera"])
    estructura2 = EstructuraArqueologica("E002", "Siglo II", ["ladrillo"])
    estructura3 = EstructuraArqueologica("E003", "Siglo III", ["adobe", "piedra"])

    # Componer estructuras
    estructura1.agregar_estructura(estructura2)
    estructura1.agregar_estructura(estructura3)

    # Mostrar resultados
    print(estructura1)
    print(estructura2)
    print(estructura3)

    #EJERCICIO 13
    print("\nEJERCICIO 13") #ESTA MAL PUESTO, ES AL REVES (ESTO SON ASOCIACIONES)
    
    p1 = Punto(0, 0)
    p2 = Punto(1, 0)
    p3 = Punto(1, 1)
    p4 = Punto(0, 1)

    poligono1 = Poligono(1)

    p1.asignar_a_poligono(poligono1)
    p2.asignar_a_poligono(poligono1)
    p3.asignar_a_poligono(poligono1)
    p4.asignar_a_poligono(poligono1)

    print(poligono1)

    for punto in poligono1.puntos:
        print(punto)

    #EJERCICIO 14
    print("\nEJERCICIO 14")

    p_1 = punto_I(0, 0)
    p_2 = punto_I(1, 0)
    p_3 = punto_I(0, 1)
    p_4 = punto_I(1, 1)  # Este punto no debería poder agregarse
    p_5 = punto_I(2, 2)
    p_6 = punto_I(3, 3)
    p_7 = punto_I(4, 5)

    Triangulo1 = Triangulo(1)
    Triangulo2 = Triangulo(2)

    Triangulo1.agregar_punto(p_1)
    Triangulo1.agregar_punto(p_2)
    Triangulo1.agregar_punto(p_3)
    Triangulo1.agregar_punto(p_4)  # Este debe mostrar un mensaje de error

    Triangulo2.agregar_punto(p_5)
    Triangulo2.agregar_punto(p_6)
    Triangulo2.agregar_punto(p_7)

    print(Triangulo1)
    print(Triangulo2)

    #EJECICIO 15
    print("\nEJERCICIO 15")
    print("Ya está aplicado")   

    #EJERCICIO 16
    print("\nEJERCICIO 16")

    


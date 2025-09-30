#EJERCICIO 1
from Ejercicio_1 import Circulo, Rectangulo, Cuadrado, Elipse

c1 = Circulo("c1", 5, "rojo")
r1 = Rectangulo("r1", 4, 6, "azul")
q1 = Cuadrado("q1", 4, "verde")
e1 = Elipse("e1", 5, 3, "amarillo")
c2= Circulo("c2", 10, "celeste")

print(f"El circulo {c1.id} de color {c1.color} tiene un radio de {c1.radio}")
print(f"El circulo {c2.id} de color {c2.color} tiene un radio de {c2.radio}")
print(f"El rectangulo {r1.id} de color {r1.color} tiene una base de {r1.base} y una altura de {r1.altura}")
print(f"El cuadrado {q1.id} de color {q1.color} tiene un lado de {q1.lado}")
print(f"La elipse {e1.id} de color {e1.color} tiene un eje mayor de {e1.eje_mayor} y un eje menor de {e1.eje_menor}")


#EJERCICIO 2
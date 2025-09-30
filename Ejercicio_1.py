class Circulo:
    def __init__(self,id, radio, color):
        self.id = id
        self.radio = radio
        self.color = color
        
        
class Rectangulo:
    def __init__(self,id, base, altura,color):
        self.id = id
        self.base = base
        self.altura = altura
        self.color = color
        

class Cuadrado:
    def __init__(self,id, lado, color):
        self.id = id
        self.lado = lado
        self.color = color
        
class Elipse:
    def __init__(self,id, eje_mayor, eje_menor, color):
        self.id = id
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color
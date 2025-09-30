class Circuloo:
    def __init__(self,id, radio, color):
        self.id = id
        self.radio = radio
        self.color = color

    def __str__(self):
        return f"Circulo(nº={self.id}, radio={self.radio}, color={self.color})"
    
class Rectanguloo:
    def __init__(self,id, base, altura,color):
        self.id = id
        self.base = base
        self.altura = altura
        self.color = color

    def __str__(self):
        return f"Rectangulo(nº={self.id}, base={self.base}, altura={self.altura}, color={self.color})"
        
class Cuadradoo:
    def __init__(self,id, lado, color):
        self.id = id
        self.lado = lado
        self.color = color
    def __str__(self):
        return f"Cuadrado(nº={self.id}, lado={self.lado}, color={self.color})"
        
class Elipsee:
    def __init__(self,id, eje_mayor, eje_menor, color):
        self.id = id
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color

    def __str__(self):
        return f"Elipse(nº={self.id}, eje_mayor={self.eje_mayor},eje_menor={self.eje_menor} color={self.color})"
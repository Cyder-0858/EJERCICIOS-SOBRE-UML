class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poligonos = []

    def asignar_poligono(self, poligono):
        self.poligonos.append(poligono)
        poligono.punto = self

    def __str__(self):
        return f'Punto({self.x}, {self.y})'
    
class Poligono:
    def __init__(self, id):
        self.id = id
        self.punto = None

    def posee_punto(self, punto: punto):
        self.punto = punto
        punto.asignar_poligono(self)

    def __str__(self):
        return f'Poligono(ID: {self.id}, Punto: ({self.punto.x}, {self.punto.y})' if self.punto else f'Poligono(ID: {self.id}, Punto: None)'

class Triangulo:
    def __init__(self, id):
        self.id = id
        self.puntos = []

    def agregar_punto(self, punto):
        if punto not in self.puntos and len(self.puntos) < 3:
            self.puntos.append(punto)
        else:
            print(f"No se puede agregar el punto ({punto.x}, {punto.y}) al triángulo {self.id}. Ya tiene 3 puntos o el punto ya existe.")
    def __str__(self):
        return f"Triangulo(self.id={self.id}, puntos={[str(puntos) for puntos in self.puntos]})"

class punto_I:
    def __init__(self, x, y):
        self.x = x
        self.y = y  
        self.triangulo = None
    
    def __str__(self):
        return f"Puntos({self.x},{self.y})"




        

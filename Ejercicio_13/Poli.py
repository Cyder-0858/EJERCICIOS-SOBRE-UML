class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poligono = None  # Cada punto solo puede pertenecer a un polígono

    def asignar_a_poligono(self, poligono):
        if self.poligono is None:
            self.poligono = poligono
            poligono.agregar_punto(self)
        else:
            print(f"El punto ({self.x}, {self.y}) ya pertenece al polígono {self.poligono.id}")

    def __str__(self):
        return f"Punto({self.x}, {self.y})"


class Poligono:
    def __init__(self, id):
        self.id = id
        self.puntos = []

    def agregar_punto(self, punto):
        if punto not in self.puntos:
            self.puntos.append(punto)

    def __str__(self):
        return f"Poligono(id={self.id}, puntos={[str(p) for p in self.puntos]})"
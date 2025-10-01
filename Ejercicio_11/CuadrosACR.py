class museo11:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.cuadros = []
    def agregar_cuadro(self, cuadro):
        self.cuadros.append(cuadro)
        cuadro.museo = self

    def __str__(self):
        return f'Museo: {self.nombre}, Ciudad: {self.ciudad}, Cuadros: {[cuadro.titulo for cuadro in self.cuadros]}'

class cuadro11:
    def __init__(self, titulo, tecnica, autor, museo: museo11):
        self.titulo = titulo
        self.tecnica = tecnica
        self.autor = autor
        self.museo = museo #roll

    def __str__(self):
        return f'Cuadro: {self.titulo}, Técnica: {self.tecnica}, Autor: {self.autor}, Museo: {self.museo.nombre if self.museo else "Ninguno"}'


class Cuadro:
    def __init__(self, Titulo, AC, Tecnica, Sub_tecnica, Soporte, Autor, Estado_Conservacion):
        self.Titulo = Titulo
        self.AC = AC
        self.Tecnica = Tecnica
        self.Sub_tecnica = Sub_tecnica
        self.Soporte = Soporte
        self.Autor = Autor
        self.Estado_Conservacion = Estado_Conservacion

    def replica_de(self, replica_de):
        self.replica_de = replica_de
        return f"El cuadro {self.Titulo} es una replica de {self.replica_de}"
    
    def localizado_en(self, ubicacion):
        self.ubicacion = ubicacion
        return f"El cuadro {self.Titulo} se encuentra en {self.ubicacion}"
    
    def __str__(self):
        return f"Cuadro(Titulo={self.Titulo}, AC={self.AC}, Tecnica={self.Tecnica}, Sub_tecnica={self.Sub_tecnica}, Soporte={self.Soporte}, Autor={self.Autor}, Estado_Conservacion={self.Estado_Conservacion})"
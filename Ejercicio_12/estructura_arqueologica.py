#REVISAR
class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales if materiales else []
        self.estructuras_compuestas = []

    def agregar_estructura(self, estructura):
        if isinstance(estructura, EstructuraArqueologica):
            estructura.marco = self
            self.estructuras_compuestas.append(estructura)

    def __str__(self):
        return f"EstructuraArqueologica(codigo={self.codigo}, datacion={self.datacion}, materiales={self.materiales}, estructuras_compuestas={[e.codigo for e in self.estructuras_compuestas]})"
    
#fuck off como dice bellingham

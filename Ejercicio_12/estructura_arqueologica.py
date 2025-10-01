#REVISAR
class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales=None):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales if materiales else []
        self.estructuras_compuestas = []

    def agregar_estructura(self, estructura):
        if isinstance(estructura, EstructuraArqueologica):
            self.estructuras_compuestas.append(estructura)

    def __str__(self):
        compuestas = [e.codigo for e in self.estructuras_compuestas]
        return (f"Estructura {self.codigo} | Datación: {self.datacion} | "
                f"Materiales: {self.materiales} | Compuestas por: {compuestas}")
    
#fuck off como dice bellingham

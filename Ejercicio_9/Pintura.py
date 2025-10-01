from enum import Enum

class TipoTecnica(Enum):
    ACRILICO = "Acrílico"
    OLEO = "Óleo"
    ACUARELA = "Acuarela"
    TEMPERA = "Témpera"
    FRESCO = "Fresco"
    PASTEL = "Pastel"
    TINTA = "Tinta"

class TipoSub_tecnica(Enum):
    SFUMATO = "Sfumato"
    PINCELADA_SIMPLE = "Pincelada Simple"
    COLLAGE = "Collage"
    VELATURA = "Velatura"

class TipoMaterial(Enum):
    MADERA_DE_ALAMO = "Madera de álamo"
    MADERA_DE_NOGAL = "Madera de nogal"
    LIENZO = "Lienzo"

class TipoEstado_Conservacion(Enum):
    EXCELENTE = "Excelente"
    BUENA = "Buena"
    REGULAR = "Regular"
    MALA = "Mala"

class Pintura:
    def __init__(self, Titulo, Quien_es, Pintor, Ubicacion, Existen_copias, Tecnica: TipoTecnica, Sub_tecnica: TipoSub_tecnica, Material: TipoMaterial, Estado_Conservacion: TipoEstado_Conservacion):
        self.Titulo = Titulo
        self.Quien_es = Quien_es
        self.Pintor = Pintor
        self.Ubicacion = Ubicacion
        self.Existen_copias = Existen_copias
        self.Tecnica = Tecnica
        self.Sub_tecnica = Sub_tecnica
        self.Material = Material
        self.Estado_Conservacion = Estado_Conservacion

    def __str__(self):
        return f"Pintura(Titulo={self.Titulo}, Quien_es={self.Quien_es}, Pintor={self.Pintor}, Ubicacion={self.Ubicacion}, Existen_copias={self.Existen_copias}, Tecnica={self.Tecnica.value}, Sub_tecnica={self.Sub_tecnica.value}, Material={self.Material.value}, Estado_Conservacion={self.Estado_Conservacion.value})"
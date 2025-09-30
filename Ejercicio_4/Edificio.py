class Edificio:
    def __init__(self,nombre, culto, lugar, Fecha_inicio_construccion, Fecha_fin_construccion, fecha_segunda_construccion, fecha_declaracio_BIC, Material, Estilo):
        self.__nombre = nombre
        self.__culto = culto
        self.__lugar = lugar
        self.__Fecha_inicio_construccion = Fecha_inicio_construccion
        self.__Fecha_fin_construccion = Fecha_fin_construccion
        self.__fecha_segunda_construccion = fecha_segunda_construccion
        self.__fecha_declaracio_BIC = fecha_declaracio_BIC
        self.__Material = Material
        self.__Estilo = Estilo

    def __str__(self):
        return f"Edificio(nombre={self.__nombre}, culto={self.__culto}, lugar={self.__lugar}, Fecha_inicio_construccion={self.__Fecha_inicio_construccion}, Fecha_fin_construccion={self.__Fecha_fin_construccion}, fecha_segunda_construccion={self.__fecha_segunda_construccion}, fecha_declaracio_BIC={self.__fecha_declaracio_BIC}, Material={self.__Material}, Estilo={self.__Estilo})"
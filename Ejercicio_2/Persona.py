class Persona:
    def __init__(self, nombre,apellido,lugar_nacimiento,sexo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__lugar_nacimiento = lugar_nacimiento
        self.__sexo = sexo

    #Relaciones Familiares
    def casado_con(self, pareja):
        self.__pareja = pareja
        return f"{self.__nombre} está casado/a con {self.__pareja.__nombre}"
    
    def es_hijo_de(self, padre, madre):
        self.__padre = padre
        self.__madre = madre
        return f"{self.__nombre} es hijo/a de {self.__padre.__nombre} y de {self.__madre.__nombre}"


    def __str__(self):
        return f"Persona(nombre={self.__nombre}, apellido={self.__apellido}, lugar_nacimiento={self.__lugar_nacimiento}, sexo={self.__sexo})"
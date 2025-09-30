class Proyecto:
    def __init__(self, id, nombre, FechaInicio, FechaFin,):
        self.id = id
        self.nombre = nombre
        self.FechaInicio = FechaInicio
        self.FechaFin = FechaFin

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Inicio: {self.FechaInicio}, Fecha de Fin: {self.FechaFin}"
    

class miembro_del_equipo:
    def __init__(self, id, nombre, apellidos, rol):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.rol = rol
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Rol: {self.rol}"
    
class lugar_de_Actuacion:
    def __init__(self, id, nombre, lugar):
        self.id = id
        self.nombre = nombre
        self.lugar = lugar
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Lugar: {self.lugar}"
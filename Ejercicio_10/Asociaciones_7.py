class Proyectoooo:
    def __init__(self, nombre, Fecha_ini, Fecha_fin):
        self.nombre = nombre
        self.Fecha_ini = Fecha_ini
        self.Fecha_fin = Fecha_fin

    def __str__(self):
        return f"Proyecto(nombre={self.nombre}, Fecha_ini={self.Fecha_ini}, Fecha_fin={self.Fecha_fin})"

class Personaaaa:
    def __init__(self, proyectoooo: Proyectoooo, nombre, apellidos, rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.rol = rol
        self.proyectoooo = proyectoooo
    
    def __str__(self):
        return f"Persona(nombre={self.nombre}, apellidos={self.apellidos}, rol={self.rol}, proyecto={self.proyectoooo})"

class Lugar:
    def __init__(self, personaaaa: Personaaaa, nombre, ubicacion):
        self.personaaaa = personaaaa
        self.nombre = nombre
        self.ubicacion = ubicacion
        
    def __str__(self):
        return f"Lugar(nombre={self.nombre}, ubicacion={self.ubicacion}, persona={self.personaaaa})"
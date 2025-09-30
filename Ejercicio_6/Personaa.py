class Personaa:
    def __init__(self, nombre, apellidos, edad, sexo, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.dni = dni
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Edad: {self.edad}, Sexo: {self.sexo}, DNI: {self.dni}"
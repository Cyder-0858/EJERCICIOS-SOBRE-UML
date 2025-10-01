class actuacion_arqueologica:
    def __init__(self,fecha_inicio, fecha_fin,tiempo_duracion, tipo_de_actuacion):
        tipos_validos = ["sondeo", "excavación", "seguimiento"]
        if tipo_de_actuacion not in tipos_validos:
            print(f"Error: tipo_de_actuacion == {tipo_de_actuacion} no es valido, debe ser uno de {tipos_validos}")
            tipo_de_actuacion = "desconocido"
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tiempo_duracion = tiempo_duracion
        self.tipo_de_actuacion = tipo_de_actuacion

   # IDEA DESCARTADA
   # def tipo_de_actuacion(self, tipo_de_actuacion):
   #     self.tipo_de_actuacion = tipo_de_actuacion
   #     return f"El tipo de actuacion es {self.tipo_de_actuacion}"

    def __str__(self):
        return f"Actuacion arqueologica(fecha_inicio={self.fecha_inicio}, fecha_fin={self.fecha_fin}, tiempo_duracion={self.tiempo_duracion}, tipo_de_actuacion={self.tipo_de_actuacion})"
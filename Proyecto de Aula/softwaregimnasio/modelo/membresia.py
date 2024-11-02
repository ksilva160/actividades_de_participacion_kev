class Membresia:
    def __init__(self, membresia, fecha_inicio, fecha_final):
        self.membresia = membresia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.estado = "Activo"

    def congelar(self, fecha_congelar):
        self.estado = "Congelar"
        self.fecha_congelar = fecha_congelar
    
    def cancelar(self):
        self.estado = "Inactivo"



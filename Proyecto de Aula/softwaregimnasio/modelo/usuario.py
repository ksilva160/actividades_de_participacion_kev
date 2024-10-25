class Usuario:
    def __init__(self, nombre: str, correo, membresia, t_documento, n_documento):
        self.nombre = nombre
        self.correo = correo
        self.membresia = membresia
        self.t_documento = t_documento
        self.n_documento = n_documento
        self.membresias = []
        self.medidas = []
        self.asistencias = []

    def estado_membresia(self, membresia, fecha_inicio, fecha_final):
        self.membresias.append(Membresia(membresia, fecha_inicio, fecha_final))

    def medidas_usuarios(self, altura, peso, medidas_corporales, fecha_registro):
        self.medidas.append(Medidas(altura, peso, medidas_corporales, fecha_registro))
    
    def asistencias_usuario(self, fecha, hora_entrada, hora_salida, duracion_entrenamiento):
        self.asistencias.append(Asistencia(fecha, hora_entrada, hora_salida, duracion_entrenamiento))
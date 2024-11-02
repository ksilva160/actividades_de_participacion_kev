from usuario import Usuario
from excepciones import UsuarioExistenteError, UsuarioNoEncontradoError

class Gimnasio:
    def __init__(self):
        self.usuarios = []
    
    def registrar_usuario(self, nombre, correo, membresia, t_documento, n_documento):
        for usuario in self.usuarios:
            if usuario.n_documento == n_documento:
                raise UsuarioExistenteError()
        usuario = Usuario(nombre, correo, membresia, t_documento, n_documento)
        self.usuarios.append(usuario)
        return usuario
    
    def consultar_usuario(self, n_documento):
        for usuario in self.usuarios:
            if usuario.n_documento == n_documento:
                return usuario
        raise UsuarioNoEncontradoError()
    
    def generar_informe(self, usuario):
        informe = []
        informe.append("Informe del usuario:")
        informe.append("Nombre: {}".format(usuario.nombre))
        informe.append("Correo: {}".format(usuario.correo))
        informe.append("Tipo de documento: {}".format(usuario.t_documento))
        informe.append("Número de documento: {}".format(usuario.n_documento))

        informe.append("\nInformación de membresía:")
        for membresia in usuario.membresias:
            informe.append("Estado de membresía: {}".format(membresia.estado))
            informe.append("Fecha de inicio: {}".format(membresia.fecha_inicio))
            informe.append("Fecha final: {}".format(membresia.fecha_final))
        
        informe.append("\nMedidas:")
        for medida in usuario.medidas:
            informe.append("Fecha de registro: {}".format(medida.fecha_registro))
            informe.append("Altura: {}".format(medida.altura))
            informe.append("Peso: {}".format(medida.peso))
            informe.append("Medidas corporales: {}".format(medida.medidas_corporales))

        informe.append("\nAsistencias:")
        for asistencias in usuario.asistencias:
            informe.append("Fecha: {}".format(asistencias.fecha))
            informe.append("Hora de entrada: {}".format(asistencias.hora_entrada))
            informe.append("Hora de salida: {}".format(asistencias.hora_salida))
            informe.append("Duración del entrenamiento: {}".format(asistencias.duracion_entrenamiento))

        return "\n".join(informe)

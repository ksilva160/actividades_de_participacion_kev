class UsuarioExistenteError(Exception):
    """Excepción lanzada cuando se intenta registrar un usuario que ya existe."""
    def __init__(self, mensaje="El usuario ya está registrado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class UsuarioNoEncontradoError(Exception):
    """Excepción lanzada cuando se intenta consultar un usuario que no existe."""
    def __init__(self, mensaje="El usuario no se ha encontrado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MembresiaInactivaError(Exception):
    """Excepción lanzada cuando se intenta usar una membresía inactiva."""
    def __init__(self, mensaje="La membresía está inactiva."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

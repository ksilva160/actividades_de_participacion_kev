from validadorclave.modelo.validador import ReglaValidacion

class ValidadorError(Exception):
    def __init__(self, clave:ReglaValidacion):
        self.clave = clave

class NoCumpleLongitudMinimaError(ValidadorError):
    def __init__(self, clave: ReglaValidacion):
        super().__init__(clave)

    def __str__(self):
        return f"La clave no cumple con la longitud minima"

class NoTieneLetraMayusculaError(ValidadorError):
    def __init__(self, clave: ReglaValidacion):
        super().__init__(clave)

    def __str__(self):
        return f"La clave no tiene letra mayuscula"

class NoTieneLetraMinusculaError(ValidadorError):
    def __init__(self, clave: ReglaValidacion):
        super().__init__(clave)

    def __str__(self):
        return f"La clave no tiene letra minuscula"

class NoTieneNumeroError(ValidadorError):
    def __init__(self, clave: ReglaValidacion):
        super().__init__(clave)

    def __str__(self):
        return f"La clave no tiene numero"
    

class NoTieneCaracterEspecialError(ValidadorError):
    def __init__(self, clave: ReglaValidacion):
        super().__init__(clave)

    def __str__(self):
        return f"La clave no tiene caracter especial"

class NoTienePalabraSecretaError(ValidadorError):
    def __init__(self, clave: ReglaValidacion):
        super().__init__(clave)
    
    def __str__(self):
        return f"La clave no tiene palabra secreta"
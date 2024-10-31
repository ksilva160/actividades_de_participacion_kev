from abc import ABC, abstractmethod

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada:int):
        self.longitud_esperada = longitud_esperada
    
    def _validar_longitud(self, clave:str)-> bool:
        return len(clave) > self.longitud_esperada

    def _contiene_mayusculas(self, clave:str)-> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minusculas(self, clave:str)-> bool:
        return any(c.islower() for c in clave) 

    def _contiene_numero(self, clave:str)-> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave:str)-> bool:
        raise NotImplementedError
    

class Validador(ReglaValidacion):
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave:str)-> bool:
        return self.regla.es_valida(clave)


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave:str)-> bool:
        caracteres_especiales = "@_#$%"
        for caracter in clave:
            if caracter in caracteres_especiales:
                return True
        return False

    def es_valida(self, clave:str)-> bool:
        return self._validar_longitud(clave)
        

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave:str)-> bool:
        palabra = "calisto"
        posicion = clave.find(palabra)
        if posicion >= 0:
            mayusculas_contador = sum(1 for letra in clave if letra.isupper())
            if mayusculas_contador >= 2:
                mayusculas_calisto_contador = sum(1 for letra in clave[posicion:posicion + len(palabra)] if letra.isupper())
                if mayusculas_calisto_contador < len(palabra):
                    return True
        return False

    def es_valida(self, clave:str)-> bool:
        if not self._validar_longitud(clave):
            return True
        if not self.contiene_calisto(clave):
            return True
        return False
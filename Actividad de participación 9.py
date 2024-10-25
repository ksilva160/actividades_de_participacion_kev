import math
from collections import Counter
from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        # Inicializar las listas para almacenar los valores
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento = []
        
        # Mapeo de direcciones de viento a grados
        direccion_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90,
            "ESE": 112.5, "SE": 135, "SSE": 157.5, "S": 180,
            "SSW": 202.5, "SW": 225, "WSW": 247.5, "W": 270,
            "WNW": 292.5, "NW": 315, "NNW": 337.5
        }
        grados_a_direccion = {v: k for k, v in direccion_a_grados.items()}

        # Leer el archivo
        with open(self.nombre_archivo, 'r') as file:
            for line in file:
                # Procesar cada línea para obtener los datos relevantes
                if "Temperatura" in line:
                    temperaturas.append(float(line.split(":")[1].strip()))
                elif "Humedad" in line:
                    humedades.append(float(line.split(":")[1].strip()))
                elif "Presion" in line:
                    presiones.append(float(line.split(":")[1].strip()))
                elif "Viento" in line:
                    velocidad, direccion = line.split(":")[1].strip().split(",")
                    velocidades_viento.append(float(velocidad))
                    direcciones_viento.append(direccion)
        
        # Calcular promedios
        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        velocidad_viento_promedio = sum(velocidades_viento) / len(velocidades_viento)
        
        # Convertir direcciones de viento a grados y calcular la dirección predominante
        grados = [direccion_a_grados[dir] for dir in direcciones_viento if dir in direccion_a_grados]
        promedio_grados = sum(grados) / len(grados)
        
        # Encontrar la dirección más cercana al promedio calculado
        direccion_predominante = min(grados_a_direccion.keys(), key=lambda x: abs(x - promedio_grados))
        direccion_predominante_str = grados_a_direccion[direccion_predominante]

        return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_predominante_str)

# Ejemplo de uso
datos = DatosMeteorologicos('datos.txt')
estadisticas = datos.procesar_datos()
print(f"Temperatura promedio: {estadisticas[0]:.2f} °C")
print(f"Humedad promedio: {estadisticas[1]:.2f} %")
print(f"Presión promedio: {estadisticas[2]:.2f} hPa")
print(f"Velocidad promedio del viento: {estadisticas[3]:.2f} km/h")
print(f"Dirección predominante del viento: {estadisticas[4]}")

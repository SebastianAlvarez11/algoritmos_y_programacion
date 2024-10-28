from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo = nombre_archivo
    
    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperaturas= []
        humedades = []
        presion = []
        velocidad_viento = []

        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
            lineas = contenido.splitlines()

            for linea in lineas:
        
                if "Temperatura: " in linea:
                    temp_str = linea.replace("Temperatura: ", "").strip()
                    temp_modificada = float(temp_str)
                    temperaturas.append(temp_modificada)
            
                elif "Humedad: " in linea:
                    temp_str = linea.replace("Humedad: ", "").strip()
                    temp_modificada = float(temp_str)
                    humedades.append(temp_modificada)

                elif "Presion: " in linea:
                    temp_str = linea.replace("Presion: ", "").strip()
                    temp_modificada = float(temp_str)
                    presion.append(temp_modificada)

                elif "Viento: " in linea:
                    temp_str = linea.replace("Viento: ", "").replace(",ESE", "").replace("N", "").replace(",S", "").replace(",NE", "").replace("W", "").replace(",NW", "").replace(",SW", "").replace("E", "").replace(",SE", "").replace(",ENE", "").replace(",", "").strip()
                    if temp_str.endswith("E"):
                        temp_str += "1"
                    temp_modificada = float(temp_str)
                    velocidad_viento.append(temp_modificada)

            temperatura_promedio = sum(temperaturas)/ len(temperaturas)
            humedad_promedio = sum(humedades) / len(humedades)
            presion_promedio = sum(presion)/ len(presion)
            velocidad_viento_promedio = sum(velocidad_viento) / len(velocidad_viento)
            #direccion_del_viento

            return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio


datos = DatosMeteorologicos("datos.txt")
esta = datos.procesar_datos()
print(esta)
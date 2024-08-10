class Vehiculo:
    
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        print("El vehículo de velocidad máxima {} y  kilometraje de {}". format(self.velocidad_maxima  , self.kilometraje))

mi_vehiculo = Vehiculo(120,3000)


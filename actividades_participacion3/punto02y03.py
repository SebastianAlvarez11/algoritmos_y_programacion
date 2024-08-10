import math

class Punto:
    def __init__(self, coordenada1, coordenada2):
        self.coordenada1 = coordenada1
        self.coordenada2 = coordenada2
        
    def __str__(self):
        return "Punto({}, {})". format(self.coordenada1, self.coordenada2)

    def origen(self):
        return(self.coordenada1 ** 2 + self.coordenada2 ** 2) ** 0.5
    
    def mover(self,cnueva1, cnueva2):
        self.coordenada1 += cnueva1
        self.coordenada2 += cnueva2
    
    def punto_nuevo(self, nuevo_punto):
        return((self.coordenada1 - nuevo_punto.coordenada1) ** 2 + (self.coordenada2 - nuevo_punto.coordenada2) **2) ** 0.5

punto1 = Punto(2, 6)
punto2 = Punto(5, 5)

print(punto1)
print(punto2)

print("Origen de punto 1:", punto1.origen())
print("Origen de punto 2:", punto2.origen())

punto1.mover(10, 8)
punto2.mover(11, 9)

print(punto1)
print(punto2)

print("Distancia entre puntos: ", punto1.punto_nuevo(punto2))

import math

class Circulo:
    def __init__(self, centro1, centro2, radio):
        self.centro1 = centro1
        self.centro2 = centro2
        self.radio = radio
    
    def area(self):
        return math.pi *(self.radio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto(self, punto1, punto2):
        dentro = math.sqrt((punto1 - self.centro1) ** 2 + (punto2 - self.centro2)** 2)
        return dentro <= self.radio
     
circulo = Circulo(2, 4, 4)

print("Centro1:",circulo.centro1,"Centro2:" ,circulo.centro2)
print("El área es:", circulo.area())
print("El perímetro es:", circulo.perimetro())
print("Los puntos 3,5 estan dentro del círculo:", circulo.punto(3,5))





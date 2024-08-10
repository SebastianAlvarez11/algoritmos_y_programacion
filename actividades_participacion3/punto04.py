import math

class Rectangulo:
    def __init__(self, esquinasuperior1, esquinasuperior2, esquinainferior3, esquinainferior4):
        self.esquinasuperior1 = esquinasuperior1
        self.esquinasuperior2 = esquinasuperior2
        self.esquinainferior3 = esquinainferior3
        self.esquinainferior4 = esquinainferior4

    def largo(self):
        if self.esquinasuperior1 > self.esquinasuperior2:
            large = self.esquinasuperior1 - self.esquinasuperior2
        else:
            large = self.esquinasuperior2 - self.esquinasuperior1
        return large
    
    def ancho(self):
        if self.esquinainferior3 > self.esquinainferior4:
            width = self.esquinainferior3 - self.esquinainferior4
        else:
            width = self.esquinainferior4 - self.esquinainferior3
        return width
    
    def perimetro(self):
        large = self.largo()
        width = self.ancho()
        return 2 * (large + width)
    
    def area(self):
        large = self.largo()
        width = self.ancho()
        return large * width
    
    def cuadrado(self):
        return self.ancho == self.largo
    
    def resultados(self):
        print("Esquinas superiores: {}, {}. Esquinas inferiores: {}, {}.". format(self.esquinasuperior1, self.esquinasuperior2, self.esquinainferior3, self.esquinainferior4))
        print("El largo es:", rectangulo.largo())
        print("El ancho es:", rectangulo.ancho())
        print("El per+imetro es:", rectangulo.perimetro())
        print("El área es:", rectangulo.area())
        print("Es un cuadrado:", rectangulo.cuadrado())
    

esquinasuperior1 = (2)
esquinasuperior2 = (8)
esquinainferior3 = (2)
esquinainferior4 = (8)

rectangulo = Rectangulo(esquinasuperior1, esquinasuperior2, esquinainferior3, esquinainferior4)
rectangulo.resultados()


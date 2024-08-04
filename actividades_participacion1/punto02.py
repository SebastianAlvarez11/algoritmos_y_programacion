import math

def circulo(radio):
    return math.pi * radio **2

radio = float(input("Ingrese el radio del círculo: "))
area = circulo(radio)

print("El área del círculo con radio ", radio ,"es: ", area)
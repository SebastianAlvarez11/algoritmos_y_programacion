def sumar(a, b):
    e = a + b
    return e
def resta(a, b):
    e = a - b
    return e
def multiplicacion(a, b):
    e = a * b
    return e
def division(a, b):
    e = a / b
    return e

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

a = sumar(numero1, numero2)
print("La suma es: ", a)

a = resta(numero1, numero2)
print("La resta es: ", a)

a = multiplicacion(numero1, numero2)
print("La multiplicación es: ", a)

a = division(numero1, numero2)
print("La división es: ", a)
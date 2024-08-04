numeros = [1, 4, 6, 7, 4, 2, 9, 10]

mayor = numeros[0]
menor = numeros[0]

for i in range(0,8):
    if numeros[i] > mayor:
        mayor = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]

print("El núemro mayor es: ", mayor)
print("El número menor es: ", menor)
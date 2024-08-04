import random

matriz = []
for i in range(0,5):
    matriz.append([0] * 5)

for i in range(0,5):
    for j in range(0, 5):
        matriz[i][j] = (random.randint(0, 99))

for i in range(0, 5):
    celdas = ""
    for j in range(0, 5):
        celdas = celdas + str(matriz[i][j]) + " "
    print(celdas)
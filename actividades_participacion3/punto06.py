class Carta:
    
    pinta_corazones = "Corazones"
    pinta_diamantes = "Diamantes"
    pinta_treboles = "Tréboles"
    pinta_picas = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return (self.valor + " de " + self.pinta)
    
carta1 = Carta("Rey", Carta.pinta_corazones)
carta2 = Carta("10", Carta.pinta_picas)

print(carta1)
print(carta2)
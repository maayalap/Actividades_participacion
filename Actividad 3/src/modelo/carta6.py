class carta:
    diamante = "Pinta_Pica"
    corazon = "Pinta_Corazon" 
    trebol = "Pinta_Trebol"
    rombo = "Pinta_Rombo"
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

mi_carta = carta(5, carta.diamante)

print(mi_carta.valor)
print(mi_carta.pinta)
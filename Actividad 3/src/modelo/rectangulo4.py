class Rectángulo:
    def __init__(self, esquina_superior_izquierda, esquina_inferior_derecha):
        self.esquina_superior_izquierda = esquina_superior_izquierda
        self.esquina_inferior_derecha = esquina_inferior_derecha

    def calcular_perímetro(self):
        base = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        altura = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return 2 * (base + altura)

    def calcular_área(self):
        base = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        altura = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        altura = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return base == altura


esquina_superior = (1, 4)
esquina_inferior = (5, 1)
mi_rectángulo = Rectángulo(esquina_superior, esquina_inferior)

print("Perímetro:", mi_rectángulo.calcular_perímetro())
print("Área:", mi_rectángulo.calcular_área())
print("¿Es un cuadrado?", mi_rectángulo.es_cuadrado())

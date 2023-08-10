import math
class punto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def mostrar(self):
        return f"({self.x},{self.y})"
    
    def Coordenadas(self,a,b):
        self.x = a
        self.y = b
        
    def calcular_distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return distancia
        
        
        
        
mi_punto = punto(3,5)

mi_punto2.Coordenadas = punto()


#mi_punto.Coordenadas(5, 8)
print("Coordenadas del punto:", mi_punto.mostrar())
print(mi_punto2.Coordenadas(8,9))
print(mi_punto.calcular_distancia(mi_punto2))

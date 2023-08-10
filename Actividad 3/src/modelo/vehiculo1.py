class vehiculo:
    def __init__(self, velocidad_max, kilometraje):
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje

mi_vehiculo = vehiculo(80,1500)
print("La velocidad de mi vehiculo es: ", mi_vehiculo.velocidad_max)
print("El kilometraje de mi vehiculo es:", mi_vehiculo.kilometraje)
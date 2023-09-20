from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, otro_objeto):
        if isinstance(otro_objeto, Elemento):
            return self.nombre == otro_objeto.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento)-> bool:
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        for elemento in self.elementos + otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos_resultantes = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        return cls(nombre_resultante, elementos_resultantes)

    def __str__(self):
        elementos_str = ', '.join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


# Crear objetos de la clase Elemento
elemento1 = Elemento("Elemento1")
elemento2 = Elemento("Elemento2")
elemento3 = Elemento("Elemento3")

# Crear objetos de la clase Conjunto
conjunto1 = Conjunto("Conjunto A")
conjunto2 = Conjunto("Conjunto B")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

# Imprimir información de los elementos
print("Información de los elementos:")
print(elemento1)
print(elemento2)
print(elemento3)

# Imprimir información de los conjuntos
print("\nInformación de los conjuntos:")
print(conjunto1)
print(conjunto2)

# Verificar si un conjunto contiene un elemento
print("\nVerificar si un conjunto contiene un elemento:")
print(f"¿{conjunto1.nombre} contiene {elemento1.nombre}?: {conjunto1.contiene(elemento1)}")
print(f"¿{conjunto2.nombre} contiene {elemento1.nombre}?: {conjunto2.contiene(elemento1)}")

# Unir conjuntos
nuevo_conjunto = conjunto1 + conjunto2
print("\nUnión de conjuntos:")
print(nuevo_conjunto)

# Intersectar conjuntos
conjunto_interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print("\nIntersección de conjuntos:")
print(conjunto_interseccion)

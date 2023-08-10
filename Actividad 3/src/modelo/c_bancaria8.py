class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance=0):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se han depositado {cantidad} unidades. Nuevo saldo: {self.balance}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("123456789","Alice y Bob")

# Mostrar información de la cuenta
print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Saldo inicial:", cuenta.balance)

# Realizar un depósito
cantidad_deposito = 1000
cuenta.depositar(cantidad_deposito)

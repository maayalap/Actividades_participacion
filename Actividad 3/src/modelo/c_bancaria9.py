class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance=0):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se han retirado {cantidad} unidades. Nuevo saldo: {self.balance}")
        else:
            print("Monto de retiro no válido.")

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("123456789", "Alice y Bob", 1500)

# Mostrar información de la cuenta
print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Saldo inicial:", cuenta.balance)

# Realizar un retiro
cantidad_retiro = 800
cuenta.retirar(cantidad_retiro)

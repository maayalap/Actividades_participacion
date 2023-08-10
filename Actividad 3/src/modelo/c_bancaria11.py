class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("123456789", "Alice y Bob", 1500)

# Mostrar detalles de la cuenta
cuenta.mostrar_detalles()

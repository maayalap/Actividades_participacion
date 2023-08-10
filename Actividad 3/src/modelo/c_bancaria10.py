class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance=0):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2% ({cuota} unidades). Nuevo saldo: {self.balance}")

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria("123456789", "Alice y Bob", 1500)

# Mostrar información de la cuenta antes de aplicar la cuota
print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Saldo inicial:", cuenta.balance)

# Aplicar la cuota de manejo
cuenta.aplicar_cuota_manejo()

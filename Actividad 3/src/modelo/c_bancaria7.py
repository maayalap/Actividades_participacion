class CuentaBancaria:
     
     def __init__(self, n_cuenta, prop, balan):
        self.n_cuenta = n_cuenta
        self.prop = prop
        self.balan = balan

primer_cuenta = CuentaBancaria(1234, "Alejandra y Felipe", 300000)
print("Numero de cuenta: ", primer_cuenta.n_cuenta)
print("Propietarios: ", primer_cuenta.prop)
print("Balance: ", primer_cuenta.balan)
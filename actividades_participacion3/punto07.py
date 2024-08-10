class CuentaBancaria:
    
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def saldo(self):
        return self.balance
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print("Se ha depositado {}$ a la cuenta. Su saldo actual es: {}$". format(cantidad, self.balance))
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.balance -= cantidad
            print("Se ha retirado {}$ de la cuenta. Su saldo actual es: {}$". format(cantidad, self.balance))
    
    def cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print("Se ha aplicado una couta de manejo del 2%: {}$. Su saldo actual es: {}$". format(cuota, self.balance))
    
    def detalles(self):
        print("Detalles de la cuenta")
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Saldo: {}$" .format(self.balance))

c = CuentaBancaria(454645112, "Juan Carlos Ochoa", 5000)

c.detalles()
c.depositar(1000)
c.retirar(2100)
c.cuota_manejo()


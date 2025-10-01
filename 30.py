#Cuenta bancaria - Métodos para depositar
#retirar y mostrar saldo

class CuentaBancaria():
    def __init__(self, titular, monto=0):
        self.titular = titular
        self.monto = monto
    def depositar(self, monto):
        if(monto<=0):
            print("Aumenta el monto!!")
        else:
            self.monto += monto
            print(f"Se deposito {monto}")
    def retirar(self,monto):
        if(self.monto<monto):
            print("No puedes retirar esa cantidad!!")
        elif(monto<=0):
            print("Retira un monto mayor!!")
        else:
            self.monto -= monto
            print(f"Se retiro {monto}")
    def mostrarSaldo(self):
        print(f"{self.titular} tienes : {self.monto}")

cuenta1 = CuentaBancaria("TheUchy",400)

cuenta1.depositar(50)

cuenta1.retirar(30)

cuenta1.mostrarSaldo()
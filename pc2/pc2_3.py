#Tercera Cuestión

class BilleteraSol:
    def __init__(self, saldo, nombre_titular, apellido_titular):
        self.__saldo = saldo
        self.nombre = nombre_titular
        self.apellido = apellido_titular

    def mostrar_saldo(self):
        print(f"{self.nombre} tiene S/ {self.__saldo:.2f}")

    def transferir_a_dolares(self, receptor, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            monto_dolares = monto / 3.66
            receptor._BilleteraDol__saldo = receptor._BilleteraDol__saldo + monto_dolares
            print(f"Transferencia exitosa de S/ {monto:.2f} (de $ {monto_dolares:.2f}) de {self.nombre} a {receptor.nombre}")
        else:
            print(f"{self.nombre}: Saldo insuficiente para transferir S/ {monto:.2f}")

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            print(f"{self.nombre} retiró S/ {monto:.2f}")
        else:
            print(f"{self.nombre}: Saldo insuficiente para retirar S/ {monto:.2f}")


class BilleteraDol:
    def __init__(self, saldo, nombre_titular, apellido_titular):
        self.__saldo = saldo
        self.nombre = nombre_titular
        self.apellido = apellido_titular

    def mostrar_saldo(self):
        print(f"{self.nombre} tiene $ {self.__saldo:.2f}")

    def transferir_a_soles(self, receptor, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            monto_soles = monto * 3.66
            receptor._BilleteraSol__saldo = receptor._BilleteraSol__saldo + monto_soles
            print(f"Transferencia exitosa de $ {monto:.2f} (de S/ {monto_soles:.2f}) de {self.nombre} a {receptor.nombre}")
        else:
            print(f"{self.nombre}: Saldo insuficiente para transferir $ {monto:.2f}")

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            print(f"{self.nombre} retiró $ {monto:.2f}")
        else:
            print(f"{self.nombre}: Saldo insuficiente para retirar $ {monto:.2f}")

#Instanciar 3 veces los casos de transferencias para ver reflejado el
#uso de tus métodos creados


ana = BilleteraSol(500, "Ana", "Rojas")
ana.mostrar_saldo()
kimberlyn = BilleteraDol(100, "Kimberlyn", "Saldaña")
kimberlyn.mostrar_saldo()
cielo = BilleteraSol(10000,"Cielo","Cardenas")
cielo.mostrar_saldo()

ana.transferir_a_dolares(kimberlyn, 100)
kimberlyn.transferir_a_soles(ana, 20)
cielo.transferir_a_dolares(kimberlyn, 1000)
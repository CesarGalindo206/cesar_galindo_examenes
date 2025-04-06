#Segunda Cuestión

class Empleado:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f"{self.nombre} tiene un saldo de: S/ {self.__saldo:.2f}")
        return self.__saldo

    def transferencia(self, receptor, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            receptor._Empleado__saldo = receptor._Empleado__saldo + monto
            print(f"Transferencia exitosa de S/ {monto:.2f} de {self.nombre} a {receptor.nombre}")
        else:
            print(f"{self.nombre}: Saldo insuficiente para transferir S/ {monto:.2f}")


class Persona(Empleado):


    def __init__(self, nombre, edad, saldo):
        super().__init__(nombre, edad, saldo)



persona1 = Persona("Luis", 30, 500)
persona2 = Persona("Ana", 28, 200)

persona1.mostrar_saldo()
persona2.mostrar_saldo()

persona1.transferencia(persona2, 150)

persona1.mostrar_saldo()
persona2.mostrar_saldo()

persona2.transferencia(persona1, 1000)

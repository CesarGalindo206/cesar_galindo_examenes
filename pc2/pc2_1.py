#Primera Cuestión

class Empleado:

    def __init__(self, nombre, edad, saldo, nacionalidad = "peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def cumpleaños(self):
        self.edad = self.edad + 1

    def aumentoSueldo(self):
        self.saldo = self.saldo + 30*(self.saldo/100)
        return self.saldo

    def indicar(self, año_futuro):
        año_actual = 2024
        edad_futura = self.edad + (año_futuro - año_actual)
        return f"En el año {año_futuro}, el/la empleado {self.nombre} tendrá {edad_futura} años."

empleado1 = Empleado("Clemencia", 61, 6000)
empleado2 = Empleado("Leonardo", 61, 3500)

print(f"Sueldo actualizado de {empleado1.nombre}: {empleado1.aumentoSueldo()}")
print(f"Sueldo actualizado de {empleado2.nombre}: {empleado2.aumentoSueldo()}")

print(empleado1.indicar(2050))
print(empleado2.indicar(2050))



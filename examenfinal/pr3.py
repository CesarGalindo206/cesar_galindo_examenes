
from datetime import datetime


def darhora_sumar(fun):
    def wrapper(**kwargs):

        ahora = datetime.now()
        print(f"El decorador está siendo ejecutado a las {ahora.hour} con {ahora.minute} minutos")


        suma = sum(kwargs.values())
        print(f"Suma total de los valores: {suma}")

        resultado = fun(**kwargs)
        return resultado
    return wrapper


@darhora_sumar
def encontrar_mayor(**kwargs):
    mayor = max(kwargs.values())
    print(f"El mayor de los valores es: {mayor}")
    return mayor


print("\nEjemplo 1:")
encontrar_mayor(a=10, b=25, c=18, d=7, e=3, f=12)

print("\nEjemplo 2:")
encontrar_mayor(x=100, y=250, z=175)

print("\nEjemplo 3:")
encontrar_mayor(num1=4, num2=5, num3=9, num4=3)

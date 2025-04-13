from datetime import datetime

tiempoactual = datetime.now()

hora = tiempoactual.hour
minutos = tiempoactual.minute


def decorador_de_conteo(fun):
    def wrapper(*args):
        if len(args) > 1:
            try:
                print("La función fue ejecutada correctamente")
                return fun(*args)
            except IndexError:
                print("\nError: No se pasaron suficientes argumentos "
                      "para calcular la media.")
        else:
            print("\nLa función no tiene suficientes parámetros. "
                  "Debe recibir al menos 2.")
    return wrapper


@decorador_de_conteo
def datomedia(*args):
    media = (args[4] + args[5] + args[6] + args[7]) / 4

    print(f"\n{args[0]} de {args[1]} años ha sido registrado a "
          f"las {hora} horas con {minutos} minutos")

    print(f"\nLa media de las cuatro notas ingresadas es {media}")

    return datomedia


datomedia("César", 20, hora, minutos, 15, 11, 10, 8)


import random


def aleatorios():
    lista_al = []

    for numer in range(0, 10):
        numer = random.randint(0, 15)
        lista_al.append(numer)

    return lista_al


def almacen_norep(lis):
    lista_norep = []
    for numero in lis:
        if lis.count(numero) == 1:
            lista_norep.append(numero)

    return lista_norep


def maymeno(lis):

    lista_may = sorted(lis)
    lista_menor = sorted(lis, reverse=True)

    return lista_may, lista_menor


def maxlis(lis):
    lispar = []
    for numero in lis:
        if numero % 2 == 0:
            lispar.append(numero)

    nummay = max(lispar)

    return nummay

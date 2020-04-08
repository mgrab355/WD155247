import math as m
import random as r
# brak zadan 6; 11; 12


# 1
A = [1/x for x in range(1, 11)]
B = [2**y for y in range(11)]
C = [z for z in B if z % 4 == 0]
# print(A)
# print(B)
# print(C)


#2
macierz = [[r.randint(0, 11) for x in range(4)] for x in range(4)]
lista = [macierz[index][index] for index in range(4)]
# print(macierz)
# print(lista)


#3
slownik = {
    "cukierki": "kg",
    "mak": "kg",
    "chleb": "szt",
    "maseczki": "szt",
    "woda": "l"
}
slownik2 = [key for key, value in slownik.items() if value == "szt"]
# print(slownik2)


# 4
def monoF(a, b):
    if (a > 0):
        return "Funkcja jest rosnaca"
    elif (a == 0):
        return "Funkcja jest stała"
    else:
        return "Funkcja jest malejąca"
# print(monoF(-3, 5))


# 5
def proste(a1, b1, a2, b2):
    if (a1 == a2):
        return "Proste są równoległe"
    elif (a1*a2 == -1):
        return "Proste są prostopadłe"



# 7
def pitagoras(a=1, b=1):
    return m.sqrt(a**2+b**2)
# print(pitagoras(5,12))


# 8
def SumaC(a1=1, r=1, ile=10):
    return ((2*a1+(ile-1)*r)/2)*ile
# print(SumaC())


# 9
def IloczynC(* liczba):
    iloczyn = 1
    if len(liczba) == 0:
        return 0
    for i in liczba:
        iloczyn *= i
    return iloczyn
# print(IloczynC(1,2,3,4,5))


# 10
def ilosc(** nazwa):
    suma = 0
    for cos in nazwa:
        suma += nazwa[cos]
    print(suma)
# ilosc(maseczki=4, chleb=1)


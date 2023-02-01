"""Generar una lista con numeros al azar entre A y B y crear una nueva lista con los elementos de la primera que
sean pares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla.
Resolver utilizando funciones para modularizar el programa. """

import random

def generarListaPares(lista):
    listaPares=[lista[i] for i in range(len(lista)) if lista[i]%2==0]
    return listaPares

def generarLista(a,b):
    if a<b:
        menor=a;mayor=b
    else:
        menor=b;mayor=a 
    while True:
        try:
            cantidad=int(input("Ingrese la cantidad de numeros a generar: "))
            lista=[random.randint(menor,mayor) for i in range(cantidad)]
            break
        except ValueError:
            print("Error, debe ingresar un numero")
    return lista


def parametros():
    while True:
        try:
            a=int(input("Ingrese numero A: "))
            b=int(input("Ingrese numero B: "))
            break
        except ValueError:
            print("Error, debe ingresar un numero.")
    return a,b


def main():
    numA,numB=parametros()
    lista=generarLista(numA,numB)
    listaPares=generarListaPares(lista)
    print(lista)
    print(listaPares)


if __name__=="__main__":
    main()
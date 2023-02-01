"""Desarrollar una función para crear una matriz de NxM (por omisión4x3) con números al azar positivos 
(por omisión entre 1 y 50)
crear un programa para crear una matriz e informe el menor número par no repetido de la matriz"""


import random

def informar(menor,longitud):
    if longitud!=0:
        print(f"El menor numero par no repetido de la matriz es {menor}")
    else:
        print("No hay numero par no repetido.")

def menorPar(lista):
    repetido=True
    menor=0
    while len(lista)>0:
        menor=min(lista)
        if lista.count(menor)>1:
            for i in range(lista.count(menor)):
                lista.remove(menor)
        elif lista.count(menor)==1:
            break
    informar(menor,len(lista))

def listaPares(matriz):
    lista=[matriz[f][c] for f in range(4) for c in range(3) if matriz[f][c]%2==0]
    print(lista)
    return lista

def mostrarMatriz(matriz):
    for f in range(4):
        for c in range(3):
            print(matriz[f][c],end=" ")
        print()

def rellenarMatriz(matriz):
    for f in range(4):
        for c in range(3):
            matriz[f][c]=random.randint(1,10)


def generarMatriz():
    matriz=[[0]*3 for f in range(4)]
    return matriz

def main():
    matriz=generarMatriz()
    rellenarMatriz(matriz)
    mostrarMatriz(matriz)
    lista=listaPares(matriz)
    menorPar(lista)

if __name__=="__main__":
    main()
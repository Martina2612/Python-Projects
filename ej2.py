"""Desarrollar una funcion para crear una matriz de NxN (por omision 4) con numeros al azar positivos (por omision
entre 100 y 999) sin repetidos.
Crear un programa principal para crear una matriz de NxN, N se solicita del teclado y se debe validar que sea
positivo y menor a 20. Mostrar la  matriz creada por pantalla. 
Luego se solicita crear una lista por comprension que contenga la suma de los elementos pares de cada fila. 
Mostrar por pantalla.
Utilizando indices negativos eliminar de la lista aquellos valores que sean mayores al promedio de la lista. """

import random 

def promedioLista(lista):
    promedio=sum(lista)//len(lista)
    print("Promedio de la lista: ", promedio)
    for i in range(-len(lista),0,1):       #HECHO CON INDICES NEGATIVOS: ARREGLADO. COSTO 
        if lista[i]>promedio:
            lista.remove(lista[i])
    print(f"Lista con valores menores al promedio de la lista anterior: {lista}")

def sumaLista(matriz,suma=0,lista=[]):
    #NO ESTA HECHO POR COMPRENSION
    for f in range(4):
        suma=0
        for c in range(4):
            if matriz[f][c]%2==0:
                suma+=matriz[f][c]
        if suma!=0:
            lista.append(suma)
    print(f"Lista con la suma de los valores pares de las filas de la matriz: {lista}")
    promedioLista(lista)

def mostrarMatriz(matriz):
    for f in range(4):
        for c in range(4):
            print(matriz[f][c],end=" ")
        print()

def encontrado(matriz,num):
    esta=False
    for f in range(4):
        for c in range(4):
            if matriz[f][c]==num:
                esta=True
                break
    return esta 

def rellenarMatriz(matriz):
    for f in range(4):
        for c in range(4):
            num=random.randint(100,999)
            while encontrado(matriz,num)==True:
                num=random.randint(100,999)
            matriz[f][c]=num 
    return matriz 


def crearMatriz(n=4):
    matriz=[[0]*n for i in range(n)]
    return matriz

def main():
    matrizCeros=crearMatriz()
    matriz=rellenarMatriz(matrizCeros)
    mostrarMatriz(matriz)
    sumaLista(matriz)

if __name__=="__main__":
    main()



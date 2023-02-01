"""Desarrollar un programa para crear una matriz de NxM con valores al azar entre a y b sin repetir en la fila.
Crear una lista por comprension con la suma de las filas de la matriz. 
Utilizar indices negativos para recorrer y duplicar el valor de aquellos valores que sean menores al promedio de 
la lista.
Utilizar funciones. """

import random 

def promedioLista(lista):
    promedio=sum(lista)//len(lista)
    print("Promedio de la lista: ", promedio)
    for i in range(-len(lista),0,1):       #HECHO CON INDICES NEGATIVOS: ARREGLADO. COSTO 
        if lista[i]<promedio:
            lista[i]=lista[i]*2
    print(f"Lista con valores menores al promedio de la lista anterior duplicados: {lista}")

def sumaFilas(matriz,fil,suma=0,lista=[]):
    lista=[sum(matriz[f]) for f in range(fil)]
    print(f"Lista con la suma de los valores de las filas de la matriz: {lista}")
    promedioLista(lista)

def mostrarMatriz(matriz,fil,col):
    for f in range(fil):
        for c in range(col):
            print(matriz[f][c],end=" ")
        print()

def rellenarMatriz(matriz,fil,col,a,b):
    for f in range(fil):
        for c in range(col):
            num=random.randint(a,b)
            while num in matriz[f]:
                num=random.randint(a,b)
            matriz[f][c]=num 
    return matriz 

def parametros():
    while True:
        try:
            a=int(input("Ingrese numero A: "))
            b=int(input("Ingrese numero B: "))
            if a<b:
                menor=a;mayor=b
            else:
                menor=b;mayor=a 
            break
        except ValueError:
            print("Error, debe ingresar un numero.")
    return menor,mayor

def crearMatriz():
    while True:
        try:
            n=int(input("Ingrese numero de filas: "))
            m=int(input("Ingrese numero de columnas: "))
            matriz=[[0]*m for i in range(n)]
            break
        except ValueError:
            print("Error. Ingrese un numero entero.")
    return matriz,n,m 

def main():
    matrizCeros,fil,col=crearMatriz()
    menor,mayor=parametros()
    matriz=rellenarMatriz(matrizCeros,fil,col,menor,mayor)
    mostrarMatriz(matriz,fil,col)
    sumaFilas(matriz,fil)

if __name__=="__main__":
    main()

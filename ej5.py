"""Desarrollar un programa para cifrar las cadenas que se ingresan, reemplazando las vocales (a,e,i,o,u) 
por (4,3,1,0,5) y los espacios por un guion bajo, si tiene mas de un espacio seguido debe quedar un solo
guion entre las palabras.
Finalizar el ingreso de cadenas, cuando se ingresa una cadena vacia. 
Desarrollar utilizando funciones. """


def modificarCadena(cadena,siguiente=1):
    nueva=""
    for i in range(0,len(cadena)):
        if cadena[i] in ["a","e","i","o","u"]:
            if cadena[i]=="a":
                nueva+="4"
            elif cadena[i]=="e":
                nueva+="3"
            elif cadena[i]=="i":
                nueva+="1"
            elif cadena[i]=="o":
                nueva+="0"
            elif cadena[i]=="u":
                nueva+="5"
        elif cadena[i]==" ":
            if i!=0:
                if cadena[i-1]!=" ":
                    nueva+="_"
            elif i==0:
                nueva+="_"
        else:
            nueva+=cadena[i]
    print(nueva)

def ingresarCadena():
    cad=input("Ingresar cadena: ")
    while cad!="":
        modificarCadena(cad)
        cad=input("Ingresar cadena: ")


def main():
    ingresarCadena()


if __name__=="__main__":
    main()


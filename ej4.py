"""Escribir un programa que permite ingresar cadenas hasta ingresar una vacia.
Al finalizar el ingreso de las cadenas, informar cual fue la palabra mas larga ingresada y en cual de todas las
cadenas se ingreso. (Si mas de una palabra cumple esta condicion, es suficiente con mostrar solo una)
La cadena que contiene la palabra mas larga mostrarla centrada en 80 columnas, en mayusculas solo las vocales 
(no es necesario considerar vocales con acentos).
Utilizar funciones. """


def mostrarPantalla(mayor,cadena,posicion):
    print(f"La palabra más larga ingresada en la cadena es: {mayor}")
    cadenaCentrada=""
    for i in cadena:
        if i in ["a","e","i","o","u"]:
            cadenaCentrada+=i.upper()
        else:
            cadenaCentrada+=i
    print("La cadena que contiene la palabra más larga es: ")
    print(cadenaCentrada.center(80))

def palabraLarga(cad):
    lista=cad.split()
    larga=len(lista[0])
    palabramayor=lista[0]
    for i in range(len(lista)):
        if len(lista[i])>larga:
            larga=len(lista[i])
            palabramayor=lista[i]
    return palabramayor

def ingresarCad(cont=0):
    cad=input("Ingrese cadena: ")
    mayor="0"
    while cad!="":
        cont+=1
        palabramayor=palabraLarga(cad)
        if len(palabramayor)>len(mayor):
            mayor=palabramayor
            posicion=cont 
            cadena=cad 
        cad=input("Ingrese cadena: ")
    return mayor, cadena, posicion 


def main():
    mayor,cadena,posicion=ingresarCad()
    mostrarPantalla(mayor,cadena,posicion)

if __name__=="__main__":
    main()
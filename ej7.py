"""Se solicita crear un programa para ingresar direcciones de mail hasta ingresar una cadena vacía (presionar enter)
Consideramos un mail valido cuando tiene un solo @ y al menos un “punto”luego de @. 
Como máximo dos veces un “punto” luego de @. No puede comenzar con @.
No aceptamos sólo números luego del @. Tener en cuenta que no siempre tiene una extensión referenciando al código 
del país. Ejemplo: usuario@yahoo.com.ar otro_usuario@gmail.com ejemplo23@gmail.com 
Al finalizar el ingreso de mails informar cuantos mails cumplen las consideraciones para ser válidos, 
cuantos fueron rechazados. """


def comprobar(mail):
    valido=0
    if mail[0]!="@":
        if mail.count("@")==1:
            ubicacion=mail.index("@")
            if mail[ubicacion:].count(".")>=1 and mail[ubicacion:].count(".")<=2:
                if mail[ubicacion:].isdigit()==False:
                    punto=mail.index(".")
                    if mail[punto+1]!=".":
                        valido=1
    return valido


def main():
    mail=input("Ingrese su mail: ")
    invalido,valido=0,0
    while mail!="":
        validez=comprobar(mail)
        if validez==0:
            invalido+=1
        elif validez==1:
            valido+=1
        mail=input("Ingrese su mail: ")
    print(f"Mails validos: {valido}")
    print(f"Mails invalidos: {invalido}")


if __name__=="__main__":
    main() 





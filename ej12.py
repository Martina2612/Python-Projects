""""Escribir una lista por compresion con los naipes de la baraja española. La lista debe contener 
cadena de caracteres. Ejemplo: ["1 Oro","2 Oro"..] """

palos=["Oro","Espada","Basto","Copa"]

baraja=[str(j)+" "+palos[i] for i in range(len(palos)) for j in range(1,13)]
print(baraja)





#programa que encuentra la secuencia de collatz

#funcion para calcular la secuencia
def encnum(numeros):
    archivo=open("coorto.txt", "a")
    milista=[numeros]
    while numeros != 1:
        if numeros % 2 == 0:
            numeros = numeros / 2
            milista.extend([numeros])
        else:
            numeros = (numeros * 3) + 1
            milista.extend([numeros])
    print(milista[:])
    archivo.write(str(milista)+ "\n")
    if numeros == 1:
        archivo.close()
        pass

numero=1
while(numero!=613):
    numero=numero+1
    encnum(numero)

#encnum(4)

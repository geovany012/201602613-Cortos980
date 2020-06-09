#programa que encuentra la secuencia de collatz

#fucnion que determina si un numero es para encontrar la secuencia

def encnum(numeros):
    milista=[]
    while numeros != 1:
        if numeros % 2 == 0:
            numeros = numeros / 2
            milista.extend([numeros])
        else:
            numeros = (numeros * 3) + 1
            milista.extend([numeros])
    print(milista[:])
    if numeros == 1:
        print("1")


#contador para que evalue uno por uno, como el carnet termina en 613
numero=1
while(numero!=613):
    numero=numero+1
    encnum(numero)







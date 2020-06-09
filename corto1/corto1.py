#programa que encuentra la secuencia de collatz

#fucnion que determina si un numero es par o impar

def deter(n):
    if n%2==0:
        return True
        print ("par")
    else:
        return False
        print("impar")


#contador para que evalue uno por uno

for i in range(2,613):
    deter(i)





n = int(input("digite uma sequencia de numeros: "))
positivo = 0
negativo = 0
while (n!=0):    
    if n > 0:
        positivo = positivo + n
    else:
        negativo = negativo + n
    n = int(input("digite o proximo numero: "))
    
print ("A soma dos numeros positivos: ", positivo)
print ("A soma dos numeros negativos: ", negativo)

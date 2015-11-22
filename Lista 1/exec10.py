qtda = int(input("Digite a quantidade de numeros: "))
l = []
cont = 0
while cont < qtda:
    n = int(input("Digite o numero: "))
    if n > 0:
        l.append(n)
    cont += 1
print("o maior valor e: ",max(l),"O menor valor e: ",min(l))

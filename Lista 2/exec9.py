print("exec 9 lista 2")
import random
tam = int(input("Digite o tamanho do vetor: "))
while tam < 0:
    print("valor invalido!")
    tam = int(input("Digite um valor positivo"))
va = []
cont = 0
while cont < tam:
    sort = random.randint(0,50)
    va.append(sort)
    cont += 1
print (va)
for x in va:
    if x == 6:
        va.remove(x)
print (va)

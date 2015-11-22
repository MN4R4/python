print("exec 10 lista 2")
import random
minimo = int(input("digito o valor min: "))
maximo = int(input("digito o valor max: "))
tam = maximo - minimo
va = []
cont = 0
while minimo > maximo :
    print("o valor maximo tem que ser maior que o minimo: ")
    maximo = int(input("digito o valor max novamente: "))
while cont < tam:
    sort = random.randint(minimo,maximo)
    if sort%7 == 0:
        va.append(sort)
    cont += 1
print (va)

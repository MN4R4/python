print("exec 11 lista 2")
tam = int(input("digite o tamanho do vetor: "))
cont = 0
va = []
limpa = []
resto = []
while tam < 0:
    print("valor invalido!")
    tam = int(input("digite o tamanho novamente: "))
while cont < tam:
    valor = int(input("digite o valor da seq: "))
    va.append(valor)               
    cont += 1
for x in va:
    if x != x:
        resto.append(x)
    else:
        limpa.append(x)
print("lista limpa: ", limpa, "resto: ", resto)

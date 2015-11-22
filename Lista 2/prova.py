print("prova")
n = int(input("digite a quantidade de numeros: "))
while (n<0):
    print("valor invalido!")
    n = int(input("digite um valor positivo!"))
cont = 0
va = []
soma = 0
while (cont < n):
    var = int(input("digite o numero da sequencia: "))
    va.append(var)
    soma += var
    cont += 1
print(soma,va,min(va),max(va))

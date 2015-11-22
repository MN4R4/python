n = int(input("Digite o numero de elementos: "))
soma = 0
cont = 0
number = int(input("Digite o numero: "))
while cont < n-1:
    soma = soma + number
    number = int(input("Digite outro numero: "))
    cont += 1
print("A soma dos numeros: ",soma)
    

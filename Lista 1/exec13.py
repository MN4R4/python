n = int(input("Digite o valor de n: "))
while n<100:
    n = int(input("Digite o valor maior que 100: "))
soma = 0
lista = range(n)    
for i in lista:
    if i%2==0:
        soma += i
print("A soma dos valores pares e: ",soma)

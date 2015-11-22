n = int(input("Digite um numero: "))
l = []
while n!=0:
    if n%2==0 and n%3==0:
        l.append(n)
    n = int(input("Digite um numero: "))
print("Os numeros divisiveis por 2 e 3 sao: ",l)

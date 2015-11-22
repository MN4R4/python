n = int(input("Digite os valores de n: "))
l = []
soma = 0
cont = 0
while n>=0:
    l.append(n)
    n = int(input("Digite o proximo numero: "))
    soma += n
    cont += 1
media = soma/cont    
print("O menor valor: ",min(l),"O maior valor: ",max(l),"Media: ",media,"Soma: ",soma)    
    
    

# Faça um programa que permaneça em laço até que seja digitado um valor menor ou
# igual a zero. Cada valor válido (positivo) digitado deve ser inserido em um
# vetor na posição imediatamente antes do primeiro elemento que seja maior que
# valor que está sendo inserido. Isso resultará em um vetor ordenado de forma
# crescente.

vetor = []
i = 1
cont = 0
while i > 0:
    i = int(input("digite um valor: "))
    vetor.append(i)       
        
print(vetor)

# Faça um programa que leia um número inteiro N obrigatoriamente maior que 10.
# Preencha um vetor de tamanho N com números inteiros aleatórios.
# Exiba na tela o vetor gerado e em seguida coloque-o em ordem crescente usando
# o método da bolha.

from random import*
vetor = []
n = 0
def bubblesort(vetor):
    for z in range(len(vetor)-1,0,-1):
        for i in range(z):
            if vetor[i]>vetor[i+1]:
                temp = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = temp
                
while n < 10:
    n = int(input("Digite o valor n: "))

for x in range(10,n):
    vetor.append(randint(10,n))

bubblesort(vetor)

print(vetor)

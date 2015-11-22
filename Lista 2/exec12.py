# Faça um programa que leia um número inteiro N bem grande (acima de 5.000).
# Preencha um vetor de tamanho N com números inteiros aleatórios e em
# seguida inicie um laço de pesquisa. O valor a ser pesquisado deve ser
# lido do teclado e o programa deve dizer se tal valor está ou não contido
# no vetor.
from random import*
vetor = []
cont = 0
i = int(input("digite o valor de n: "))
for x in range(0 , i):
    vetor.append(randint(0,i))
for x in vetor:
    if (x == i):
        cont = cont + 1
    
print(vetor)        
print("Valor está contido", cont ,"vezes")

N = -1
while N < 0:
    N = int(input("Digite o numero"))
    if N < 0:
        print("Valor invalido")
fatorial = 1
I = N
while I > 1:
    fatorial = fatorial * I
    I = I - 1
print("Fatorial de ", N, " = ", fatorial)

min = int(input("Digite o valor minimo do intervalo: "))
max = int(input("Digite o valor maximo do intervalo: "))
while min > max:
    print("valor invalido, o valor max tem que ser maior que o min!")
    min = int(input("Digite o valor minimo do intervalo: "))
    max = int(input("Digite o valor maximo do intervalo: "))
else:
    for i in range(min,max+1):
        if i%5 == 0:
            print("Os valores diviseis por 5 sao: " , i)

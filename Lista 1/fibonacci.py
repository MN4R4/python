print("Sequencia de Fibonacci")
QTDE = int(input("digite o numero"))
if QTDE < 0:
    print("qtde invalida")
elif QTDE == 1:
    print("0")
elif QTDE >=2:
    print("0")
    print("1")
    a = 0
    b = 1
    I = 3
    while I <= QTDE:
    #   c = a + b
    #   print (c)
    #   a = b
    #   b = c
    #   I += 1
        b=b+a
        print(b)
        a=b-a
        I=I+1
print(" ")
print("Fim do programa")
    

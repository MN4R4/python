p = int(input("Digite primeiro termo da PG: "))
n = int(input("Digite a quantidade de numeros da soma: "))
r = int(input("Digite o valor da razao: "))
s = 0
for cont in range(n):
    a = p*(r**(cont))
    s = s + a
print("O valor da soma dos termos da PG e: ",s)
        

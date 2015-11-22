print(" exec 5 ")
nA = int(input("digite o tamanho do va: "))
"""nB = int(input("digite o tamanho do vb: "))"""
contA = 0
"""contB = 0"""
va = []
"""vb = []
R = [] """
"""if va == []:
    a = int(input("digite o numero: "))
    va.append(a)
else:"""   
while contA < nA:
    a = int(input("digite o numero: "))
    for x in va:
        if x == a:
            a = int(input("digite um numero diferente: "))
        else:
            va.append(a)
    contA += 1
print (va)
"""if len(vb) == 0:
    b = int(input("digite o numero: "))
    vb.append(b)
else:    
    while contB < nB:
        for y in vb:
            if y == b:
                b = int(input("digite o numero diferente: "))
            else:
                vb.append(b)
    contB += 1
R = va + vb"""
"""print(R)"""

    

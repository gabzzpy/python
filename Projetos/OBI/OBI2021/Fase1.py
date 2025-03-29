print('Idade de Camila') # Deu Certo
A = int(input())
B = int(input())
C = int(input())
soma  = (A+B+C) - max(A,B,C) - min(A,B,C)
print(soma)

print('Zero para cancelar') # Deu Certo
L = []
ctd = int(input())
for c in range(0,ctd):
    n = input()
    if n!='0' and n != '':
        n = int(n)
        L.append(n)
    elif n == '0':
        L.pop()
print(sum(L))

print()

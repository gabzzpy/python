def Camisetas_da_Olimpíada():
# Feito por mim. Deu Certo!
    N = int(input())
    T = map(int, input().split())
    P = int(input())
    M = int(input())
    ct1 = ct2 = 0
    for x in T:
        if x == 1:
            ct1 += 1
        if x ==2:
            ct2 += 1
    if ct1 == P and ct2 == M:
        print('S')
    else:
        print('N')
def Acelerador_de_partículas(): 
# Feito por mim. Deu certo!
    D = int(input())
    D -= 3
    D %= 8 
    if D == 3:
        print(1)
    elif D == 4:
        print(2)
    elif D == 5:
        print(3)

def FissuraPerigosa():
# Não Feito (Sem Resolução em Python)
    return 'Eunãosei'

def Irmaos():
# Feito por mim. Deu certo!
    N = int(input())
    M = int(input())
    print(M+(M-N))

def Pandemia():
# Não Feito (Sem Resolução em Python)
    return 'Nada'

def TresPorDois_Ralouim():
# Não Soube Fazer
    return 'Não Sei'
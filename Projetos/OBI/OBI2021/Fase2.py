def Calculo_Simples():
#Feito Por Mim. Deu Certo
    L = []
    i = int(input())
    a = int(input())
    b = int(input())
    for c in range(a,b+1):
        U = []
        if c >=10:
            x = str(c)
            for l in range(len(x)):
                U.append(int(x[l]))
            if sum(U) == i:
                L.append(c)
            del U
        elif c < 10:
            if c==i:
                L.append(c)
    print(len(L))




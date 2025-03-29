NumeroAmigos ,TotalReunioes = map(int, input().split())
AmigoInf, ReuniInici = map(int, input().split())
Infectados = [AmigoInf]
contador = 1
while True:
    Pessoas = list(map(int, input().split()))
    del Pessoas[0]
    for c in Infectados:
        if c in Pessoas:
            for x in Pessoas:
                Infectados.append(x)
    
    if contador == TotalReunioes:
        break
    contador +=1
print(Infectados)

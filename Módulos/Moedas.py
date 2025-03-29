def aumentar(n=0,qntd=0,formatado=False):
    resp = n + (n*(qntd/100))
    return resp if formatado is False else moeda(resp)
def diminuir(n=0,qntd=0,formatado=False):
    resp = n - (n*(qntd/100))
    return resp if formatado is False else moeda(resp)
def dobro(n=0,formatado=False):
    resp = n * 2
    return resp if not formatado else moeda(resp)
def metade(n=0,formatado=False):
    resp = n/2
    return resp if formatado is False else moeda(resp)
def moeda(n=0,mon = 'R$',formatado=False):
    value = f'{mon}{n:.2f}'.replace('.',',')
    return value 
def resumo(n,aumento=10,diminui=5):
    print(f'''
    {'-'*30}
    {'RESUMO DO VALOR'.center(30)}
    {'-'*30}
    Preço Analisado: \t{moeda(n)}
    Dobro do preço: \t{dobro(n,True)}
    Metade do preço: \t{metade(n,True)}
    {aumento}% de aumento: \t{aumentar(n,aumento,True)}
    {diminui}% de redução: \t{diminuir(n,diminui,True)}
    {'-'*30}
    ''')
    

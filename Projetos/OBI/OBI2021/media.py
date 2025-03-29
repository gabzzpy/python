from time import sleep
produtos = ['arroz','feijao','panela','açucar','faca','garfo','caneta']
simnao=' '
while True:
    contador = 1
    print(f'Aqui está uma lista dos produtos que temos atualmente:')
    for p in produtos:
        print(f'{contador}. {p}')
        contador +=1
    sleep(0.5)
    while simnao not in 'SsNn':
            simnao = str(input('Deseja adicionar um produto? (caso não, o programa irá terminar) ')).upper().strip()[0]

    if simnao in 'Ss':
        add = str(input('Adicionaremos o produto: ')).lower()
        if add in produtos:
            print('Esse produto ja existe.')
        else:
            produtos.append(add)
            print('Produto Adicionado com sucesso!')

    elif simnao in 'Nn':
        break
    sleep(0.8)







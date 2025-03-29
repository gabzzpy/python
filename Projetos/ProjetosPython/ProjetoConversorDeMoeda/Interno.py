moedas = {
    'Euro': 1.08,
    'Dolar': 1.00,
    'Real': 0.20,
}

def LeiaFloat(txt):
    while True:
        try:
            Escolha = float(input(txt))
        except (ValueError, TypeError):
            print('\n\033[0;31mDigite um número Real Válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mPrograma Interrompidos Pelo Usuário\033[m')
        else:
            return Escolha

def titulo(txt):
    print('---' * 10)
    print(f'{txt}'.center(30))
    print('---' * 10)


def Moedas(l=True):
    if l:
        titulo('Moedas Cadastradas')
    for i,v in moedas.items():
        print(f'{i:<2}     {v:3>}')

def opc1():
    titulo('Cadastrar Moeda')
    global moedas
    nome = str(input('Nome da Moeda: '))
    cotac = float(input(f'Cotação da(o) {nome} para U$1.00 (A(O) {nome} equivale em dólar a... : '))
    cotac = float(cotac)
    moedas[nome] = cotac

def opc2():
    global moedas
    titulo('Conventer Moeda')
    print('Nós temos essas Moedas no sistema: ')
    Moedas(l=False)
    m1 = str(input('Digite o nome da moeda que vc tem: '))
    v1 = float(input('Digite o valor que você tem nessa moeda: '))
    m2 = str(input('Digite o nome da moeda que vc quer converter: '))
    moedaval = moedas[m1]
    moedaval2 = moedas[m2]
    if moedaval > 1:
        v1 = v1 / moedaval
    elif moedaval <= 1:
        v1 = v1 * moedaval
    # Transforma na moeda desejada
    if moedaval2 > 1:
        v1 = v1 / moedaval2
    elif moedaval2 <= 1:
        v1 = v1 * moedaval2
    print(f'O valor da conversão de {m1} para {m2} é aproximadamente {v1:.0f}')







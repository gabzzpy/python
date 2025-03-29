from Interno import titulo, opc2,opc1,Moedas
def EscolherOPC(txt):
    while True:
        try:
            Escolha = int(input(txt))
        except (ValueError, TypeError):
            print('\n\033[0;31mDigite um número Inteiro Válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mPrograma Interrompidos Pelo Usuário\033[m')
        else:
            return Escolha


def MenuCDM():
    while True:
        lista = [opc1,opc2,Moedas]
        titulo('Instituto CDM')
        print('[1] Cadastrar Nova Moeda')
        print('[2] Converter Moedas')
        print('[3] Ver Moedas Cadastradas')
        print('[4] Sair do Programa')
        escolha = EscolherOPC('Escolha uma opção: ')
        while escolha not in (1, 2, 3,4):
            escolha = EscolherOPC('Não é uma opção! Tente Novamente: ')
        for i,c in enumerate(lista):
            if escolha-1 == i:
                c()
        if escolha == 4:
            titulo('Volte Sempre')
            break




MenuCDM()
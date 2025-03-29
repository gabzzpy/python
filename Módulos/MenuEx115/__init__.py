def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO \033[m.')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de Dados interrompida pelo Usuário!!\033[m')
            return 0
        else:
            return n

def Linha(a):
    print('-' * (20 + len(a)))
    print(f'{a.center(20+len(a))}')
    print('-' * (20 + len(a)))
def Menu():

    Linha('MENU PRINCIPAL')
    print('1- Ver Pessoas Cadastradas')
    print('2- Cadastrar nova Pessoa')
    print('3- Sair do sistema')
    opc = leiaInt('Sua Opção: ')
    while opc not in (1,2,3):
        print('\033[0;31mERRO! Escolha uma das alternativas. \033[m.')
        opc = leiaInt('Sua Opção: ')
    return opc


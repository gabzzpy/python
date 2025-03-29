import ArquiTes
from Interno import opc1,opc2,opc3,opc4
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
def titulo(txt):
    print('-=-'*12)
    print(f'{txt.center(36)}')
    print('-=-' * 12)


def MenuGDT():
    lista = [opc1, opc2, opc3, opc4]
    arquivo = 'Tarefas.txt'
    if not ArquiTes.arquivoExiste(arquivo):
        ArquiTes.arquivoCriar(arquivo)
    while True:
        titulo('Gerenciador de Tarefas')
        print('[1] Adição de Tarefa')
        print('[2] Ver Tarefas')
        print('[3] Concluir Tarefa')
        print('[4] Remoção de Tarefa')
        print('[5] Terminar Execução')
        esc = leiaInt('Qual sua escolha?')
        if esc not in (1,2,3,4,5):
            esc = leiaInt('Não Temos essa opção. Escolha Novamente: ')
        else:
            for i, c in enumerate(lista):
                if esc == i+1:
                    c(arquivo)
        if esc == 5:
            titulo('Acabou!! Volte Sempre')
            break

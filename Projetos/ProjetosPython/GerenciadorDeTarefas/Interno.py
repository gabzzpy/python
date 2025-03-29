import Interface
def opc1(arq):
    Interface.titulo('Adição de Tarefa')
    tarefa = str(input('Tarefa a ser adicionada: '))
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo')
    else:
        a.write((f'{tarefa}\n'))
        a.close()
    while True:
        a = open(arq, 'at')
        sera = str(input('Quer add mais alguma tarefa? [S/N] ')).upper().strip()[0]
        if sera in 'Nn':
            a.close()
            break
        elif sera in 'Ss':
            tarefa = str(input('Tarefa a ser adicionada: '))
            a.write((f'{tarefa}\n'))
        else:
            print('Não temos essa opção.')


def opc2(arq):
    Interface.titulo('Ver Tarefas')
    a = open(arq, 'rt')
    for i, lugar in enumerate(a):
        print(f'{i + 1}º {lugar}', end='')
    a.close()


def opc3(arq):
    Interface.titulo('Concluir Tarefa --')
    a = open(arq, 'rt')
    print('As tarefas existentes são: ')
    for i, lugar in enumerate(a):
        print(f'{i + 1}º {lugar}', end='')
    a.close()
    print()
    with open(arq, 'rt') as a:
        linha = a.readlines()
    Rlinha = Interface.leiaInt('Digite o número da Tarefa que quer concluir: [Se não tiver nenhuma, escreva 0] ')
    while Rlinha not in range(len(linha)+1):
        print('Não temos essa opção.')
        Rlinha = Interface.leiaInt('Digite o número da Tarefa que quer concluir: [Se não tiver nenhuma, escreva 0] ')
    a = open(arq,'wt')
    for i,l in enumerate(linha):
        if Rlinha-1 == i:
            a.write((f'-- {l}'))
        else:
            a.write((f'{l}'))
    a.close()


def opc4(arq):
    Interface.titulo('Remoção de Tarefa')
    a = open(arq, 'rt')
    print('As tarefas existentes são: ')
    for i,lugar in enumerate(a):
        print(f'{i+1}º {lugar}', end='')
    a.close()
    print()
    with open(arq, 'rt') as a:
        linha = a.readlines()
    Rlinha = Interface.leiaInt('Digite o número da Tarefa que quer remover: ')
    while Rlinha not in range(len(linha) + 1):
        print('Não temos essa opção.')
        Rlinha = Interface.leiaInt('Digite o número da Tarefa que quer remover: [Se não tiver nenhuma, escreva 0] ')
    a = open(arq,'wt')
    for i,l in enumerate(linha):
        if Rlinha-1 == i:
            pass
        else:
            a.write(l)
    a.close()












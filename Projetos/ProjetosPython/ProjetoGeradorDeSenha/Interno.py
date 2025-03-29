import random
import time

def titulo(nome):
    print('---'*10)
    print(nome.center(30))
    print('---' * 10)
    
def Escolhas():
    escolha = int(input('Escolha sua opção: '))
    while escolha not in (1,2):
        escolha = int(input('Erro! Escolha novamente: '))
    if escolha == 2:
        titulo('Volte Sempre!')
    else:
        esc1()
    return escolha


def checagem(txt):
    a = 'F'
    while a not in ('SsNn'):
        a = str(input(txt))
    if a in 'Ss':
        qtd = int(input('Quantos[as]? '))
        return qtd
    else:
        return 0

def esc1():
    senha = []
    lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lista3 = ['$', '#', "@", "!", "%", '&']
    titulo('Vamos Criar uma Senha')
    print('OBS: O tamanho da senha tem relação com a soma da quantidade de cada um dos itens a seguir.')
    nm = checagem('Deseja ter números? [S/N] ')
    LM = checagem('Deseja ter Letras Maiusculas? [S/N] ')
    Lm = checagem('Deseja ter Letras Minusculas? [S/N] ')
    CaracterE = checagem('Deseja ter Caracteres Especiais? [S/N] ')
    print(f'Sua senha terá {nm + LM + Lm + CaracterE} caracteres')
    for c in range(nm):
        a = random.randint(0, 9)
        senha.append(a)
    for c in range(Lm):
        a = random.choice(lista1)
        senha.append(a)
    for c in range(LM):
        a = random.choice(lista2)
        senha.append(a)
    for c in range(CaracterE):
        a = random.choice(lista3)
        senha.append(a)
    random.shuffle(senha)
    print('PARABENS SUA SENHA É: ',end='')
    for z in range(len(senha)):
        print(f'{senha[z]}',end='')
    print()
    time.sleep(5)







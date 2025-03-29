# Não há como expliocar tudo aqui, veja os exercícios para relembrar, ou reveja a aula ._.



print('Desafio101')
import datetime
def voto(Ano):
    anotoday = datetime.date.today().year
    idade = anotoday - Ano
    if 70 >= idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    if 18 > idade >=16 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'


print('---------------------------')
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))

print('Desafio102')
def fatorial(num,show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('------------------------------')
    resul = 1
    tenta = 0
    for c in range(num,0,-1):
        tenta += 1
        if tenta != num and show:
            print(f'{c} x ',end='')
        if tenta == num and show:
            print(f'{c} = ',end='')
        resul *= c
    return resul


print(fatorial(5, show=True))

print('Desafio103')
def ficha(nome ='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Diga-me o nome do jogador: '))
gols = input('Fez quantos gols na partida? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)

print('Desafio104')
def leiaInt(txt):
    valor = 0
    while True:
        n = input(txt)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO \033[m.')
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

print('Desafio105')
def notas(*notas, sit=False):                                                                                                                                                                                                        def notas(*notas, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    cont = media = situ =0
    maior = menor = notas[0]
    for c in notas:
        cont += 1
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        media += c
    media /= cont
    dic = {}
    dic['total'] = cont
    dic['maior'] = maior
    dic['menor'] = menor
    dic['média'] = media   
    if sit:
        if media >= 7:
            situ = 'BOA'
        if media < 6:
            situ = 'RUIM'
        if 7 > media >= 6:
            situ = 'RAZOÁVEL'
        dic['situação'] = situ
    return dic 

resp = notas(5.5,2.5,10,6.5, sit=True) 
print(resp)
help(notas)


print('Desafio106')                                                                                                                                                                                                           c = ( '\033[m', # 0 - sem cores
    cor = ('\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
      '\033[0;30;43m', # 3 - amarelo
      '\033[0;30;44m', # 4 - azul
      '\033[0;30;45m', # 5 - roxo
      '\033[7;30m', # 6 - branco
      )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[6],end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')


while True:
    titulo('Sistema de ajuda PyHelp',3)
    resp = str(input('Função ou Bibioteca > '))
    if resp.upper() == 'FIM':
        print('')
        break
    else:
        ajuda(resp)    
titulo('Até Logo',5)
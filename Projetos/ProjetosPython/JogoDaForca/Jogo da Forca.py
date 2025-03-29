from time import sleep
def titulo(txt):
    l = len(txt) + 8
    print('-'* l )
    print(f'{txt.center(l)}')
    print('-' * l)


def forca(palavra,dica):
    lista1 = []
    lista2 = []
    lista3 = []
    for c in palavra:
        lista1.append(c)
        lista2.append('_')
    palavra.upper()
    titulo('JOGO DA FORCA')
    sleep(0.5)
    print('COMEÇAR!!!!')
    sleep(0.5)
    print(f'A DICA É {dica.upper()}')
    print(' _ '*len(palavra))
    Vida = 6
    Ganhou = False
    jog = ''
    while lista2 != lista1 and Vida != 0:
        tentar = str(input('Quer tentar uma palavra inteira? [S/N] ')).upper().strip()
        while tentar not in 'SsNn':
            tentar = str(input('Quer tentar uma palavra inteira? [S/N] ')).upper().strip()
        if tentar in 'Ss':
            palavra2 = input('Qual a palavra: ').upper()
            for j in palavra2:
                lista3.append(j)
            if lista3 == lista1:
                titulo('PARABÉNS VOCÊ GANHOU!!!!')
                Ganhou = True
                break
            else:
                print('VOCÊ ERROU!!!!! A PALAVRA NÃO É ESSA')
                Ganhou = False
                Vida -= 1
        if tentar in 'Nn':
            jog = str(input('Qual Letra? ')).upper()
        if jog in lista1 and Ganhou == False:
            for i,c in enumerate(palavra):
                if jog == c:
                    lista2[i] = jog
            for x in lista2:
                print(f'{x} ', end='')
            print(f'Acertou!! Existe {jog} na Palavra')
        else:
            if Ganhou == False:
                Vida -= 1
                print(f'ERROU!! Não existe {jog} na Palavra')
        if Vida == 0 and Ganhou == False:
            print(f'VOCÊ PERDEU!!! A palavra era {palavra}')
            break
    if Vida > 0 and Ganhou == False:
        titulo('PARABÉNS VOCÊ GANHOU!!!!')




palavra = 'Russo'
dica = 'nome'
forca(palavra.upper(),dica)
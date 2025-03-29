# uso do break
# ensinando a usar o print(f'{algcoisa}'), q eu ja sabia


print('Desafio066')
Soma = Tnt = 0
while True:
    NTA = int(input('Digite um número [999 para parar]: '))
    if NTA == 999:
        break
    Soma = Soma + NTA
    Tnt += 1
print(f'Você digitou {Tnt} números e a soma entre eles é {Soma}.')

print('Desafio067')
valor = m = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('---'*6)
    for c in range(0,11):
        m = c * valor
        print(f'{valor} x {c} = {m}')
    print('---'*6)
print('PROGRMADA DE TABUADA ENCERRADO. Volte sempre!')

import random
vitorias = 0
print('Desafio068')
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)
while True:
    computadorV = random.randint(0,10)
    valor1 = int(input('Diga um valor: '))
    parI = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = computadorV + valor1
    check = (computadorV + valor1) % 2
    print('---'*10)
    print(f'Você jogou {valor1} e o computador {computadorV}. Total de {soma}', end='')
    if parI == 'I' and check == 0:
        print(', DEU PAR \nVocê PERDEU!') 
        break
    if parI == 'P' and check == 0:
        print(', DEU PAR \nVocê GANHOU!')
        vitorias += 1
    if parI == 'I' and check != 0:
        print(', DEU IMPAR \nVocê GANHOU!')
        vitorias += 1 
    if parI == 'P' and check != 0:
        print(', DEU IMPAR \nVocê PERDEU!')  
        break  
    print('Vamos jogar novamente...')
    print('---'*10)
print(f'GAME OVER! Você venceu {vitorias} vezes')

print('Desafio068')
maisD = 0
muie = 0
homi = 0
while True:
    print('---'*10)
    print('CADASTRE UMA PESSOA')
    print('---'*10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maisD += 1
    if sexo == 'F'and idade < 20:
        muie += 1
    if sexo == 'M':
        homi += 1
    if continuar in 'Nn':
        break
print(muie)
print(f'''Total de pessoas com mais de 18 anos: {maisD}
Ao todo temos {homi} homens cadastrados
E temos {muie} mulheres com menos de 20 anos''')

print('Desafio070')
print('---'*10)
print('      LOJA SUPER BARATÃO')
print('---'*10)
contador = maisM = soma = 0
nomeB = ''
menor = float('inf')

while True:

    nome = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    contador += 1
    if preço < menor:
        menor = preço
        nomeB = nome        
    
    if preço > 1000:
        maisM += 1
    
    soma += preço
    
    Cont = ' '
    while Cont not in 'SsNn':
       Cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if Cont == 'N':
        break
print('-------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maisM} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeB} que custa R${menor:.2f}')


print('Desafio071')
print('==='*10)
print('          BANCO CEV')
print('==='*10)
sacar = int(input('Quanto você quer sacar? R$ '))
total = sacar
totalCéd = 0
céd = 50
while True:
    if total >= céd:
        total -= céd
        totalCéd += 1
    else:
        if totalCéd > 0:
            print(f'Temos {totalCéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        if céd == 20:
            céd = 10
        if céd == 10:
            céd = 1
        totalCéd = 0
        if total == 0:
            break 
print('==='*10)
print('VOLTE SEMPRE!! TENHA UM BOM DIA')

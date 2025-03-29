print('Desafio084')
tudo = list()
umpor = list()
maisP = []
menosP = []
qnt = maiorP = menorP = 0
while True:
    umpor.append(str(input('Nome: ')))
    umpor.append(float(input('Peso: ')))
    tudo.append(umpor[:])
    menorP = 999 
    if umpor[1] > maiorP:
        maiorP = umpor[1]
    elif umpor[1] < menorP:
        menorP = umpor[1]
    umpor.clear()
    qnt += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0] 
    if continuar == 'N':
        break
print(f'A quantidade de pessoas cadastradas é {qnt} pessoas')
for n,p in enumerate(tudo):
    if maiorP == p[1]:
        maisP.append(p[0])
    if menorP == p[1]:
        menosP.append(p[0])
print(f'O maior peso foi de {maiorP} KG. Peso de {maisP} ')
print(f'O menor peso foi de {menorP} KG. Peso de {menosP} ')

print('Desafio085')
lista = [[],[]]
valor = 0
for c in range(0,7):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os valores digitados pares são: {lista[0]}')
print(f'Os valores digitados ímpares são: {lista[1]}')

print('Desafio086')
lista1 = [[0,0,0],[0,0,0],[0,0,0]]
for c in range(0,3):
    for l in range(0,3):
        lista1[c][l] = int(input(f'Digite um valor para [{c},{l}]: '))
print('-='*30)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{lista1[c][l]:^5}]',end='')
    print()

print('Desafio087')
lista1 = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
maior = 0
for c in range(0,3):
    for l in range(0,3):
        lista1[c][l] = int(input(f'Digite um valor para [{c},{l}]: '))
print('-='*30)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{lista1[c][l]:^5}]',end='')
        if lista1[c][l] % 2 == 0:
            soma += lista1[c][l] 
    print()
print(f'A soma dos números digitados pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {lista1[0][2] +lista1[1][2]+lista1[2][2]}')
for l in range(0,3):
    if l == 0 or lista1[1][l] > maior:
        maior = lista1[1][l]
print(f'O maior número da segunda linha é: {maior}')

print('Desafio088')
import random
from time import sleep
print('---'*10)
print(f'{"JOGA NA MEGA SENA":^30}')
print('---'*10)
sorteie = int(input('Quantos jogos vc quer q eu sorteie? '))
jogos = []
tudo = []
print(f'-=-=-=-=-=-=-=- SORTEANDO {sorteie} JOGOS -=-=-=-=-=-=-=-')
for c in range(0, sorteie):
    for l in range(0,6):
        a = random.randint(0,60)
        if a in jogos:
            a = random.randint(0,60)   
        else:
            jogos.append(a) 
    jogos.sort() 
    tudo.append(jogos[:])
    jogos.clear()  
for i, l in enumerate(tudo):
    sleep(1)
    print(f'Jogo {i+1}: {l}')

print('Desafio089')
boletim = []
while True:
    nome = (str(input('Nome: '))) 
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = ((nota1 + nota2) /2)
    boletim.append([nome, [nota1, nota2], media])
    cont = ' '
    while cont not in 'sSnN':
        cont = str(input('Quer Continuar ? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=-'*10)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('---'*10)
for i,a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
    elif opc == 999:
        print('FINALIZANDO...')
        break
print("VOLTE SEMPRE")
   

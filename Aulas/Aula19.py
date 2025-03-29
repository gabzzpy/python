#DICIONÁRIOS { }
# Para add algo ao dicionario so por nomedodicionario['coisas'] = 'coisa1'
# Ou por ja dentro das linhas do dicionario
#print(dicionario.values()) // mostra os valores
#print(dicionario.keys()) // mostra as chaves de cada valor
#print(dicionario.items()) // mostra tudo
# ao invés de copiar assim: [:], se copia o dicioanrio assim .copy()


print("Desafio090")
boletim = {}
boletim['Nome'] = str(input("Diga o nome do Aluno: ")) 
boletim['Nota'] = float(input('Média do Aluno: '))
if boletim['Nota'] >= 7 and boletim['Nota'] <= 10:
    boletim['Situacao'] = 'Aprovado'
elif boletim['Nota'] >= 6 and boletim['Nota'] < 7:
    boletim['Situacao'] = 'Recuperação'
elif boletim['Nota'] < 6 and boletim['Nota'] > 0:
    boletim['Situacao'] = 'Reprovado'
print("-=-"*10)
for p, v in boletim.items():
    print(f'- {p} é igual a {v}')

print("Desafio091")
import random
from operator import itemgetter
from time import sleep
jogadas = {}
E = 1
RANKING = []
print('Valores Sorteados:')
for c in range(0,4):
    jogadas[f'Jogador{E}'] = random.randint(0,10)
    E += 1
for k,v in jogadas.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
RANKING = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=-'*10)
print('==', 'RANKING DOS JOGADORES', '==')
for i,v in enumerate(RANKING):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

print("Desafio092")
from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
pessoa ['Idade'] = datetime.now().year - ano 
pessoa['Ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if pessoa['Ctps'] != 0:
    pessoa['Contratação'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = ((pessoa['Contratação'] + 35) - datetime.now().year) + pessoa['Idade']
print('-=-'*12)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')


print("Desafio093")
Jogador = {}
partidas = []
Jogador['nome'] =  str(input("Nome do jogador: "))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0,tot):
    partidas.append(f"Quantos gols na partida {c}? ")
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-='*12)
print(jogador)
print('-=-='*12)
for k,v in jogador.items:
    print(f'O campo {k} tem valor {v}')
print('-=-='*12)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador["gols"]):
    print(f' => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

print("Desafio094")
dici = {}
lista = []
tenta = media =  0
while True:
    dici['Nome'] = str(input('Nome: '))
    dici['Idade'] = int(input('Idade: '))
    dici['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    media += dici['Idade']
    lista.append(dici.copy())
    while dici['Sexo'] not in 'FfMm':
        dici['Sexo'] = str(input('Erro!. Por favor digite apenas M ou F: '))
    tenta += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('ERRO! Respomda apenas S ou N. ')).strip().upper()[0]
    if continuar == 'N':
        break
media /= tenta
print('-=-'*15)
print(f'A) Ao todo temos {tenta} pessoas cadastradas. ')
print(f'B) A média de idade entre todas as {tenta} pessoas é {media:5.2f} ')
print('C) As mulheres cadastradas são: ', end='')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da média: \n')
for p in lista:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f' {k} = {v}; ',end='')
        print()
print('<<<   ENCERRADO  >>>')

print('Desafio095')
time = list()
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        gols = int(input(f"Quantos gols na partida {c+1}? "))
        partidas.append(gols)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS S/N. ')
    if resp == 'N':
        break
print('-=-=' * 15)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end ='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO: Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'      No jogo {i+1} fez {g} gols.')
    print()
print('VOLTE SEMPRE!')

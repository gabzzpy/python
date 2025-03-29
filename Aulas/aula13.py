#comando 'for'
# c = algo
# for c in range(1,10):
# laço c no intervalo de um a 10
# vai repetir até chegar no 10
# s += n, no caso do video do for
import time
for c in range(1,6):
    print('Oi!')
print(' FIM ')

print('Desafio046')
f = 11
for c in range(1, 11):
    f = f-1
    print(f"Os fogos vão estourar em: {f}")
    time.sleep(1)
print("BOOM!")

print('Desafio047')
a = 50
for c in range(50,-2, -2):
    print(a, end=' ')
    time.sleep(0.5)
    a -= 2
#outro jeito de fazer o 047:
for c in range(2, 51, 2):
    print(c, end=' ')

contador = 0
nn = 0
print('Desafio048')
for c in range(3,500,3):
    if c % 3 == 0 and c % 2 == 1:
     contador = contador + 1
     nn = nn + c
print(f'A soma de todos os {contador} valores é: {nn}')

print('Desafio049')
Valor = int(input('Digite um valor para saber sua tabuada: '))
for c in range(0,11):
    print(f'{Valor} x {c} = {Valor*c}')

print('Desafio050')
n = 0
for c in range(1,7):
    num = int(input('Digite o valor de um número: '))
    if num % 2 == 0:
        n += num
print(f'A soma é{n}')    

print('Desafio051')
PT = int(input('Primeiro termo: ')) 
Razao = int(input('Razão: '))
for c in range(0,10):
    print(f'{PT} ',end= '-> ')
    PT += Razao
print('ACABOU')

print('Desafio052')
num = int(input('Digite um valor: '))
tot = 0
for c in range(1, num + 1):
    
    if num % c == 0:
        tot += 1
        print('\033[33m',end= '')
    else:
        print('\033[31m',end= '')
    print(f'{c} ', end=' ')
print(f'\n\033[mO número {num} foi dívisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele NÃO é primo')

print('Desafio053 // Eu entendi como que faz, mas é bem grande e não estou com vontade de fazê-la')

print("Desafio054")
from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for pessoa in range(1,8):
    nasc = int(input(f"Em que ano a {pessoa}º nasceu? "))
    idade = atual - nasc
    if idade >= 18:
        totMaior += 1
    else :
        totMenor += 1
print(f"""
A quantidade de pessoas maiores de idade é {totMaior}
A quantidade de pessoas menores de idade é {totMenor}""")

print("Desafio055")
maior = 0
menor = 0

for c in range(1,6):
    peso = float(input(f"Qual o peso da {c}º pessoa? "))
    if c == 1:
        maior  = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso é de: {:.1f} / O menor peso é de {:.1f}".format(maior, menor))

print("Desafio056")
maiorI = 0
nomeM = 'a' 
qntdM = 0
media = 0
for c in range(1,5):
    print(f"---- {c}º pessoa ----")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: ')) 
    sexo = str(input('Sexo [M/F]: ')).strip()
    if idade > maiorI and sexo in 'Mm':
        maiorI = idade
        nomeM = nome
    if sexo == 'F' and idade < 20:
        qntdM += 1
    media += idade
media /= 4
print(f'''
A média entre as idades é {media} anos
O nome do homem com maior idade é {nomeM} e tem {maiorI} anos
Existem {qntdM} mulheres com menos de 20 anos
''')
    





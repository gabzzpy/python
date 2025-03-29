print('Desafio096')
def area(L, C):
    area = L * C
    print(f'A área de um terreno {L} x {C} é de {area} m^2.')


print('  Controle de Terrenos  ')
print('-'*24)
L = float(input('LARGURA (m): '))
C = float(input('COMPRIMENTO (m): '))
area(L,C)

print('Desafio097')
def escreva(txt):
    tam = len(txt) +4
    print('~' * tam)
    print(f'  {txt:^}')
    print('~'* tam)


escreva(str(input()))

print('Desafio098')
import time
def contador(i,f,p):
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    print('-=-'*10)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += p
    elif i > f :
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= p
    print('FIM!')
    print('-=-'*10)
        

contador(1,10,1)
contador(10,0,2)
print('PRONTO!! AGORA FAÇA SUA PROPRIA CONTAGEM PERSONALIZADA')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pulando: '))
contador(i,f,p)

print('Desafio099')
def maior(* num):
    print('-=-'*10)
    print('Analisando os valores passados...')
    maior = cont = 0
    for c in num:
        print(f'{c} ',end='',flush=True)
        time.sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if maior < c:
                maior = c
        cont +=1
    print(f'Foram analisados {len(num)} valores ao todo.')
    time.sleep(0.5)
    print(f'O maior valor informado foi: {maior}.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

print('Desafio100')

import random
import time
def sortear(lista):
    print('Somando os valores da lista ',end='')
    for c in range(0,5):
        a = random.randint(0,100)
        lista.append(a)
        print(f'{a} ',end='', flush = True)
        time.sleep(0.5)
    print('PRONTO!!')
    


def somaPar(x):  
    soma = 0  
    for c in x:
        if c %2 == 0:
            soma += c
    print(f'Somando os valores pares {x}, temos {soma}')


lista = []
sortear(lista)
somaPar(lista)



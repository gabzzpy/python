#TUPLAS
# () TUPLAS {} DICIONARIOS [] LISTAS
# Para pegar uma posição de uma lista, tupla ou qlr coisa se usa o []
# TUPLAS SÃO IMUTÁVEIS 
# del(tupla) -> deleta a tupla
# Comandos: len, .count, .index , sorted, min, max

lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata Frita')
print(sorted(lanche)) #Põe em ordem mas não altera o valor da tupla

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# O comando de cima e o de baixo dão o mesmo resultado
for pos, comida in enumerate(lanche):  # Enumerate enumera a posição e pode dizer o que há dentro da tupla 👍
    print(f'Eu vou comer {comida} na posição {pos}')   

a = (2,5,4)
b =(5,8,1,2)
c = a + b # é diferente de por b +a
print(c.count(9))# conta quantas vezes aparece o numero 9, ou o elemento 9 na tupla C
print(c.index(2))# mostra em qual posição esta o 2 // e se for (2, 5) vai procurar o 2 a partir da posição 5 👍

print('Desafio072')
tupla020 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if número <= 20 and número >= 0:
        break
    print('Tente Novamente. ', end='')
print(f'Seu número [{número}], escrito por extenso é: {tupla020[número]}')

print('Desafio073')
print('Me recuso a fazer, pq é literalmente so uso de print e de comandos [0:5] ou [-4:] ou o proprio index')

import random
print('Desafio074')
numerosA = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
M = sorted(numerosA)
print('Os valores sortreados foram: ',end='')
for n in numerosA:
    print(f'{n} ',end='')
print(f'\nO menor valor foi: {max(numerosA)}')
print(f'O maior valor foi: {min(numerosA)}')

print('Desafio075')
Num4 = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))
print(f'Você diigtou os valores: {Num4}')
print(f'O valor 9 apareceu {Num4.count(9)} vezes')
if 3 in Num4:
    print(f'O valor 3 apareceu na {Num4.index(3)+1}º posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('Os valores pares são: ', end='')
for n in Num4:
    if n % 2 == 0:
        print(n, end=' ')

print('Desafio076')
tupla_tabela = ('Lápis', 1.75,'Borracha', 2.00,
                'Caderno',15.90,'Estojo', 25.00,
                'Transferidor',4.20,'Compasso', 9.99,
                'Mochila',120.32,'Canetas',22.30,
                'Livro',34.90,)
print('-----'*8)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-----'*8)
for item in range(0, len(tupla_tabela)):
    if item % 2 == 0:
        print(f'{tupla_tabela[item]:.<30}',end='')
    if item % 2 == 1:
        print(f' R$ {tupla_tabela[item]:.2f}', end='\n')
print('-----'*8)

print('Desafio077')
tupla_palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for palavras in tupla_palavras:
    print(f'\nNa palavra {palavras} temos ',end='')
    for vogal in palavras:
        if vogal.lower() in 'aeiou':
            print(vogal,end=' ')


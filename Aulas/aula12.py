# elif = else + if
print('Desafio036')
valorcasa = float(input('Qual o valor da casa? '))
salarioc = float(input('Quanto você recebe por mês? '))
anosapagar = float(input('quantos anos você planeja pagar a casa? '))
mes = anosapagar * 12
presmen = valorcasa / mes
salariovdd = salarioc * 0.3
if presmen > salariovdd :
    print("Seu empréstimo foi Negado, pois a prestação excede 30% de seu salario")
elif presmen <= salariovdd :
    print('Seu emprestimo foi aprovado!!')
    print('Você deverá pagar R${} por mês'.format(presmen))

print('Desafio037 (Pediu p olhar, pq é bases numericas)')
nint = int(input('Escreva um número INTEIRO: '))

print('Desafio038')
n1 = int(input('Diga-me um número:'))
n2  = int(input('Agora, diga-me outro: '))
if n1 > n2 :
    print('O número {} é maior que {}'.format(n1, n2))
elif n1 < n2 :
   print('O número {} é maior que {}'.format(n2, n1))
else : 
    print('Os números: {} e {} são iguais'.format(n1, n2))

from datetime import date

print('Desafio039')
atual = date.today().year
nascimento = int(input('Que ano você nasceu? '))
idade = (atual - nascimento) 
falta = 18 - idade 
passa =  idade - 18
if idade == 18 :
    print('Esta na hora de você se alistar para o exercito, cara')
elif idade > 18 :
    print('Oxi... Já passou sua hora de se alistar, rapaz. Você já passou {} anos da idade, melhor ir AGORA.'.format(passa))
else : 
    print('Opa meu garotinho, ainda falta tempo para você se alistar. Faltam exatos: {} anos'.format(falta))

print('Desafio040')
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2) / 2
if media < 5 :
    print('Sua média é: {}. E por isso foi Reprovado'.format(media))
elif media >= 7 :
    print('Sua média é: {}. E por isso foi Aprovado'.format(media))
elif 7> media >= 5 :
    print('Sua média é: {}. E por isso está em Recuperação'.format(media))

print('Desafio041')
nadador = int(input('Diga-me sua idade? '))
if nadador > 0 and nadador <= 9:
    print('Sua categoria é MIRIM')
elif nadador > 9 and nadador <= 14:
    print('Sua categoria é INFANTIL')
elif nadador > 14 and nadador <= 19:
    print('Sua categoria é JUNIOR')
elif nadador > 19 and nadador <= 20:
    print('Sua categoria é SÊNIOR')
elif nadador > 20:
    print('SUA CATEGORIA É MASTER!!!')

print('Desafio042 tem haver com triangulos, coisa chata que mal estudamos')
print('NO FIZ CARALHO')

print('Desafio043')
Peso = float(input('Diga-me seu peso em kilogramas: '))
Altura = float(input('Diga-me sua altura em metros:'))
imc = Peso / (Altura ** 2)
if imc < 18.5 :
    print('Você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso normal. PARABÉNS!!')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc > 30 and imc <= 40:
    print('Você está com Obesidade')
elif imc > 40:
    print('VOCÊ ESTÁ COM OBESIDADE MÓRBIDA. PROCURE AJUDA RAPIDAMENTE')

print('Desafio044')

preço1 = float(input('Diga-me o preço do produto: '))
formdepag = float(input(""" \n
Para à vista (dinheiro ou cheque), 10% de desconto. Digite: 1
Para à vista no cartão, 5% de desconto. Digite: 2
Em até 2x no cartão, preço normal. Digite: 3
3x ou mais vezes no cartão, 20% de juros. Digite: 4 
"""))
if formdepag == 1:
    aa = preço1 - (preço1 * 0.1)
    print('Você deverá pagar {}'.format(aa))
elif formdepag == 2:
    aa = preço1 - (preço1 * 0.05)
    print('Você deverá pagar {}'.format(aa)) 
elif formdepag == 3:
    aa = preço1
    print('Você deverá pagar {} SEM JUROS'.format(aa))
elif formdepag == 4:
    aa = preço1 + (preço1 * 0.2)
    totalparc = int(input('Quantas parcelas?'))
    parcela = aa / totalparc
    print('Você deverá pagar no total R${}. Parcelando fica: R${} '.format(aa,parcela))
elif formdepag < 4:
    print('Essa opção não existe :( )')
import random
import time 
print('Desafio045')
computerjogada = random.randint(0, 2)
playerjogada = int(input("""
Qual sua jogada?
[0] Pedra
[1] Papel
[2] Tesoura
"""))
print('=-' * 11)
print('O computador jogou: {}'.format(computerjogada))
print('E você jogou: {}'.format(playerjogada))
if computerjogada == 0:
    if playerjogada == 0:
        print('Empate!')
    elif playerjogada == 1:
        print('Você Ganhou!')
    elif playerjogada == 2:
        print('Você Perdeu!')
if computerjogada == 1:
    if playerjogada == 0:
        print('Você Perdeu!')
    elif playerjogada == 1:
        print('Empate!')
    elif playerjogada == 2:
        print('Você Ganhou!')
if computerjogada == 2:
    if playerjogada == 0:
        print('Você Ganhou!')
    if playerjogada == 1:
        print('Você Perdeu!')
    if playerjogada == 2:
        print('Empate!')
print('=-' * 11)


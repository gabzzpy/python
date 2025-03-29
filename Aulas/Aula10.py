# if tem :
# else tb tem
# segue exemplo abaixo:
import random 
import math
import time 

print('Desafio028')
numero_p = int(input('A máquina sorteou um número, tente adivinhar qual é.\nDigite um numero de 1 à 5: '))
numero_sorteado = int(random.randint(1,5))
if numero_p == numero_sorteado :
    print('PROCESSANDO...')
    time.sleep(3) # faz dormir ♠
    print('Você acertou o número!! Parabéns')
 
else :
    print('PROCESSANDO...')
    time.sleep(3)
    print('Você errou!! O verdadeiro número era: {}'.format(numero_sorteado))

print('Desafio029')
velocidade = float(input('Qual a velocidade que você andou? '))
if velocidade > 80.0 :
    multa = (velocidade - 80.0) * 7.0
    print('Você ultrapassou a kilometragem. Por isso foi multado! Sua multa é de R${:.2f}'.format(multa))
else :
    print('Você não foi multado! CONTINUE NA LEI :) ')

print('Desafio030 ')
numero30 = int(input('Digite um número: '))
imparoun = numero30 % 2
if imparoun == 0 :
    print('O número {} é par'.format(numero30))
else :
    print('O número {} é impar'.format(numero30))

print('Desafio031')
dis = float(input('Qual a distancia da sua viagem, em km? '))
if dis <= 200.0 :
    preço1 = 0.50 * dis
    print('O custo da sua viagem no nosso transporte é de: R${} '.format(preço1))
else :
    preço2 = 0.45 * dis
    print('O custo da sua viagem é de mais de 200km ou seja, o custo será de: R${}'.format(preço2))

from datetime import date
print('Desafio032 ')
ano = int(input('Qual o ano desejado? (Ano 0, vai automaticamente para o ano atual) ')) #!= significa que é diferente de. Por explo != 2 significa que o resultado é um numero diferente de 2 
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('Sim! {} é um ano bissexto'.format(ano))
else :
    print('Não! {} não é um ano bissexto'.format(ano))

print('Desafio033 ')
num1 = float(input('Diga um número :'))
num2 = float(input('Diga um número :'))
num3 = float(input('Diga um número :'))
if num1 > num2 and num1 > num3 :             #Existe um jeito mais simples, soq esse tb esta certo, o jeito mais simples poupa umas 2 linhas apenas!!
    print('{} é o maior'.format(num1))       # Lembre-se de seguir o Zen do Python
if num2 > num1 and num2 > num3 :             # Seria colocar um menor = a ou namior = a, dependnedo da parte
    print('{} é o maior'.format(num2))       # Pq ai faria uma tecnica de ficar 2 if apenas e não 3
if num3 > num1 and num3 > num2 :
    print('{} é o maior '.format(num3))
if num1 < num2 and num1 < num3 :
    print('{} é o menor'.format(num1))
if num2 < num1 and num2 < num3 :
    print('{} é o menor'.format(num2))
if num3 < num1 and num3 < num2 :
    print('{} é o menor '.format(num3))

print('Desafio034')
salario = float(input('Diga o seu salario: R$'))
if salario > 1250.0 :
    aumento1 = salario * 1.10
    print('Seu salario de R${} teve um aumento, foi para R${}'.format(salario,aumento1))
else :
    aumento2 = salario * 1.15
    print('Seu salario de R${} teve um aumento, foi para R${}'.format(salario,aumento2))

print('Desafio035 esse desafio, é o dos triangulos, os quais vc não estudou ainda em matematica eu acho ne, ent faça apos aprender ')




n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
if  n1 > n2 : 
    print('O primeiro número é o maior')
else :
    print('É menor que 10')
carvelho = int(input('Quantos anos tems eu carro '))

if carvelho >= 5 :
    print('Seu carro está velho :.<')
    print('---FIM---')
else :
    print('Seu carro está novo!! ')
    print('---FIM---')
print('Carro velho' if carvelho >=5 else 'Carro novo')
# while é amms coisa de um for, soq vc n sabe a quantidade de vezes
# nenhum dos dois é melhor ou pior, vai d vc escolher

print('Desafio057')
sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Dados Inválidos. Por favor, informe seu sexo: [M/F] ")).strip().upper()[0]
print(f'O sexo {sexo}. Registrado com Sucesso')

print('Desafio058')
import random
computador_jogada = int(random.randint(0,10))
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que vc consegue adivinhar qual foi?''')
player_jogada = int(input('Qual seu palpite? '))
while player_jogada != computador_jogada:
    if player_jogada > 10 or player_jogada < 0:
        player_jogada = int(input('Que putaria é essa? Eu disse q era entre 0 e 10, caralho. C colocou {} porra. Tenta Dnv crlh: '.format(player_jogada)))
    if computador_jogada > player_jogada:
        player_jogada = int(input('Mais... Tente outra vez. '))
    elif computador_jogada < player_jogada:
        player_jogada = int(input('Menos... Tente outra vez. '))
print(f'Você acertou!. O número era {computador_jogada}')

print('Desafio059') 
import time 
N1 = int(input('Primeiro Valor: '))
N2 = int(input('Segundo Valor: '))
Escolha = 10
while Escolha != 5:
    print('''=-=-=-=-=-=-=-=-=-=-=-=-=
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    =-=-=-=-=-=-=-=-=-=-=-=-=''')
    Escolha = int(input('>>>> Qual é sua opção? '))
    time.sleep(0.5)
    if Escolha == 1:
        print(f'A soma entre {N1} e {N2} é {N1 + N2}')
    elif Escolha == 2:
        print(f'A multiplicação entre {N1} e {N2} é {N1 * N2}')
    elif Escolha == 3:
        if N1 > N2:
            print(f'O maior número é {N1}.')
        elif N1 < N2:
            print(f'O maior número é {N2}.')
        else:
            print('Os números são iguais.')
    elif  Escolha == 4:
        N1 = int(input('Primeiro Valor: '))
        N2 = int(input('Segundo Valor: '))
        time.sleep(0.5)
    elif Escolha > 5 or Escolha < 0:
        print('Opção Inválida. Tente Novamente ')
        print('''=-=-=-=-=-=-=-=-=-=-=-=-=
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        =-=-=-=-=-=-=-=-=-=-=-=-=''')
        Escolha = int(input('>>>> Qual é sua opção? '))

print('Finalizando...')
time.sleep(2)
print('=-=-=-=-=-=-=-=-=')
print('Fim do Programa. Volte Sempre!')

print("Desafio060")
FN = int(input('Digite um número para saber seu fatorial: '))
FNR = 1
if FN == 0:
    print("O fatorial de 0 é 0.")
else:    
    print(f'Calculando o fatorial de {FN}')
    while FN !=0:
        print(f'{FN}', end='')
        print(' x ' if FN > 1 else ' = ', end = '')
        FNR *= FN
        FN -= 1
    print(f'{FNR}') 

print("Desafio061")
print('''Gerador de PA
=-=-=-=-=-=-=-=-=-=-=-=-=''') # =- * 10, tb serve
PT = int(input('Primeiro termo: ')) 
Razao = int(input('Razão: '))
Tentativas = 0
while Tentativas < 10:
    print(f'{PT} ',end= '-> ')
    PT += Razao
    Tentativas += 1
print('FIM')

print('Desafio062') 
print('''Gerador de PA
=-=-=-=-=-=-=-=-=-=-=-=-=''') # =- * 10, tb serve
PT = int(input('Primeiro termo: ')) 
Razao = int(input('Razão: '))
Tentativas = 0
amais = 10
total = 0
while amais != 0:
    total += amais 
    while Tentativas <= total:
        print(f'{PT} ',end= '-> ')
        PT += Razao
        Tentativas += 1
    print('PAUSA')
    amais = int(input("Quantos termos vc quer mostrar a mais? "))
print('FIM')

print("Desafio063")
print('-=-' * 10)
print("Sequêcia de Fibonacci")
t1 = 0
t2 = 1
tt = 0
Tentativas = 2
print('-=-' * 10)
nTermos = int(input('Quantos termos vc quer? '))
print('~' * 60)
print(f'{t1} -> {t2}', end=' -> ')
while nTermos != Tentativas:
    tt = t1 + t2
    print(f'{tt}', end=' -> ')
    t1 = t2
    t2 = tt
    Tentativas += 1
print('FIM',end='\n')
print('~' * 60)

print('Desafio064')
Soma = Tnt = 0
NTA = int(input('Digite um número [999 para parar]: '))
while NTA != 999:
    Soma = Soma + NTA
    Tnt += 1
    NTA = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {Tnt} números e a soma entre eles é {Soma}.')

print('Desafio065')
maior = menor = tentativas = media = 0
continuar = 'S'
while continuar == 'S':
    número = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    tentativas += 1
    media += número
    if maior == 0 and menor == 0:
        maior = menor = número
    if maior < número:
        maior = número
    elif menor > número:
        menor = número
media /= tentativas
print(f'Você digitou {tentativas} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
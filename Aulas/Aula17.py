# LISTAS SÃO MUTAVIES
Lista1 = ['a','b','c','d']
print(Lista1)
Lista1[2] = 'L' #TROCA A LETRA DA POSIÇÃO 2 NA LISTA 
print(Lista1)
Lista1.append('e') # ADICIONA 'E' A LISTA (NA ULTIMA POSIÇÃO)
print(Lista1)
Lista1.insert(0,'Z') # ADICIONA Z A LISTA NA POSIÇÃO ESCOLHIDA (NO CASO É ZERO)
print(Lista1)

# ESSES 3 COMANDOS FAZEM A MESMA COISA, DELETAM ALGO DA LISTA
# Deleta pela posição // Lista1.pop(3)        
# # Deleta pela posição // del Lista1[3]      
# Deleta pelo q é dentro da lista // Lista1.remove('L')  

valoresLista2 = list(range(4,11)) # LEMBRANDO, RANGE COMEÇA NO 4 E VAI ATÉ O 10, NÃO 11
print(valoresLista2)

valoresLista3 = [8,2,5,4,9]
valoresLista3.sort() # Coloca em ordem os valores da lista, ordem crescente
print(valoresLista3)
valoresLista3.sort(reverse=True) # Coloca em ordem os valores da lista, ordem decrescente
print(valoresLista3)
len(valoresLista3) # Diz quantos elementos tem na lista

a = [1,2,3]
b = a[:] #recebe osvalores de A sem criar uma ligação entre eleas, podendo mudar um sem mudar o outro


print('Desafio078')
maioremenor = []
maior = 0
menor = 0
for valor in range(0,5):
    maioremenor.append(int(input(f'Digite um valor para posição {valor}: ')))
    if valor == 1:
        maior = menor = maioremenor[valor]
    if maioremenor[valor] > maior:
        maior = maioremenor[valor]
    if maioremenor[valor] < menor:
        menor = maioremenor[valor]
print('=-='*20)
print(f'Você digitou os valores {maioremenor}')
print(f'O maior valor digitado foi {maior} nas posições ',end='')
for c, v in enumerate(maioremenor):
    if v == maior:
        print(f'{c}...',end='')
print(f'\nO menor valor digitado foi {menor} nas posições ',end='')
for c, v in enumerate(maioremenor):
    if v == menor:
        print(f'{c}...',end='')


print('Desafio079')
VN = []
while True:
    v = int(input('Digite um valor: '))
    if v not in VN:
        VN.append(v)
        print('Valor registrado com sucesso!')
    else:
        print('Valor Negado! Ja existe esse valor na lista!')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'SsNn':    
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
VN.sort()
print('=-='*20)
print(f'Você digitou os valores: {VN}')

print('Desafio080')
print("Se quiser saber va la ver pq eu to com trauma")

print('Desafio081')
Número = []
ele = 0
while True:
    Número.append(int(input("Digite um número: ")))
    ele += 1
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar not in 'SN':
        continuar = str(input("Tente Novamente. Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break
Número.sort(reverse=True)
print('=-='*10)
print(f'Você digitou {ele} elementos')   #outra possibilidade fazer o len de valores
print(f'Os valores na ordem descrescente são: {Número}')
if 5 in Número:
    print('O número 5 aparece na lista!')
else:
    print('O número 5 não aparece na lista  :(')

print('Desafio082')
lista = []
Par = []
impar = []
while True:
    a = int(input('Digite um valor: '))
    lista.append(a)
    if a % 2 == 0:
        Par.append(a)
    else:  
        impar.append(a)  
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar not in 'SN':
        continuar = str(input("Tente Novamente. Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''A lista completa é {lista}
A lista de pares é {Par}
A lista de impares é {impar}''')

expr = str(input("Digite a expressão númerica: "))
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append ('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida!')



#str = string, que é uma cadeia de caracteres como: 'Curso em video python'
frase1 = 'Curso em Vídeo Python' # <-- Guardado dentro do computador em espaços, em sequencia de 0-infinito
frase2 = '   Aprenda Python  '
# C é 0  [9:21:2] esse ultimo 2 seria pulando de 2 em 2 V ,pula, r, pula. Fatiamento de String:
print(len(frase1)) # mostra a quantidade de caracteres
print(frase1.count('o',0,13)) #quantas vezes tem a letra o (minuscula) em numero e 0,13 seria do caractere 0 até o 12
print(frase1.find('deo')) #vai me indicar em qual numero de caractere começa 'deo'
#se tiver uma string que não existe vai mostrar -1 mostrando que não existe
print('Curso' in frase1 ) # vai mostrar se tem a palavra 'Curso' em frase1
print(frase1[9:14])
print(frase1[:5]) # é a msm coisa que [0:5]
print(frase1[15:]) # é a msm coisa que [15:21] ja que não indicaria o final
print(frase1.replace('Python', 'Android'))
print(frase1.upper())
print(frase1.lower())
print(frase1.capitalize()) # vai pegar a frase e deixar tudo minusculo, menos a primeira letra
print(frase1.title())
# parecido com capitalize, mas ele quebra a cada espaço deixando tds as primeiras
# letras de cada palavra em maiusculo
print(frase2.strip()) # remove os espaços antes das polavras e depois delas
print(frase2.rstrip()) #remove os espaços da direita ( não remove os espaços entre as palavras)
print(frase2.lstrip()) # remove os espaços da esquerda ( não remove os espaços entre as palavras)
print(frase1.split()) # Vai dividir em pedaços a string, a cada espaço, a letra apos ela retorna a 0, 1 e por ai vai
print('-'.join(frase1))
frase1 = frase1.replace('Python', 'Android')
print(frase1)

print('Desafio022')
nomecc = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é {} '.format(nomecc.upper()))
print('Seu nome em minúsculas é {}'.format(nomecc.lower()))
nomecc1 = nomecc.replace(' ','') # ou pode ser .format(len(nome) - nome.count(' ')))
print('Seu nome tem ao todo {} letras'.format (len(nomecc1)))
print('Seu primeiro nome tem {} letras'.format(nomecc.find(' ')))

print('Desafio023')
Num = int(input('Digite um número de 0 a 9999: '))
unidade = Num // 1 % 10
dezena = Num // 10 % 10
centena = Num // 100 % 10
milhar = Num // 1000 % 10
print('Sua unidade é {} \nSua Dezena é {} \nSua Centena é {} \nSeu milhar é {}'.format(unidade,dezena,centena,milhar))


print('Desafio024')
Cidade = str(input('Qual nome da sua cidade? '))
Cidade1 = Cidade.strip()
Cidade2 = Cidade1.capitalize()
print('Santo' in Cidade2)
#
print('Desafio025')
Nome1 = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}' .format('silva' in Nome1))
 
print('Desafio026')
Frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} na frase'.format(Frase.count('A')))
print('A primeira Letra A apareceu na posição: {}'.format(Frase.find('A') + 1))
print('A ultima letra A apareceu na posição: {}'.format(Frase.rfind('A')+1 ))

print('Desafio027')
n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
#Se qusier entender ative os comandos:
#print(nome)
#print(len(nome))
#print(nome[0])
#print(nome[1])
#print(nome[2])
#print(nome[3])
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome a é {}'.format(nome[len(nome)-1]))
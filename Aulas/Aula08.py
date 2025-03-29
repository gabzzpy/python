# Pode-se importar muitas coisas, como math e random // CONTROL + ESPAÇO
# classe: bebida, dentro dela tem: pudim, rosquinha, chocolate
# import bebida = pudim, rosquinha, chocolate
# from doce import pudim  = apenas pudim
# para import math completa
# from math import sqrt para importar apenas o 'sqrt'
# para arredondar:
# ceil = arredondar pra cima
# floor = arredondar pra baixo
# trunc = eliminar da virgula pra frente sem arredondar
# pow = potencia
# sqrt = raiz quadrada
# factorial = fatorial de um números
import math
import random 
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))

print('A raiz de {} de maneira muito aproximada é {}'.format(num, math.ceil(raiz)))
print('A raiz de {} de maneira aproximada para baixo é {}'.format(num, math.floor(raiz)))
print('A raiz de {} de maneira (trunc) aproximada é {}'.format(num, math.trunc(raiz)))

sortear = random.randint(1,1000)
print(sortear)

print('Desafio016')
pint = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(pint,math.trunc(pint)))

print('Desafio017')
CatO = float(input('Digite o valor do cateto oposto: '))
CatA = float(input('Digite o valor do cateto Adjacente: '))
Hipotenusa = ((CatO**2) + (CatA**2)) **(1/2)
print('O valor da hipotenusa é {}'.format(Hipotenusa))

print('Desafio018')
angulo = float(input('Digite o valor do angulo: '))
Cos = math.cos(math.radians(angulo))
Tg = math.tan(math.radians(angulo))
sen = math.sin(math.radians(angulo))
print('O angulo {} têm: \nSeno de: {} \nCosseno de: {} \nTangente de: {}'.format(angulo,sen,Cos,Tg))


print('Desafio019')
a1 = str(input('Digite o nome do  1* aluno: '))
a2 = str(input('Digite o nome do  2* aluno: '))
a3 = str(input('Digite o nome do  3* aluno: '))
a4 = str(input('Digite o nome do  4* aluno: '))
alunos = [a1, a2, a3, a4]
escolha = random.choice(alunos)
print('O aluno sorteado foi: {}'.format(escolha))

print('Desafio020')
escolha2 = random.shuffle(alunos)
print('Os mesmos alunos do exercicio passado, em ordem aleatoria ficam: {} '.format(alunos))


print('Desafio021')
print('Para o mp3 precisa salvar ele em forma de mp3 e usar o import pygame para programar e tocar a musica')
print("""aasasasasasasas
sasasasasasasaa
sasasasasas
asasasasa""")
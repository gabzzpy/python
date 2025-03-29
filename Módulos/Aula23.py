print('Desafio113')
def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO \033[m.')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de Dados interrompida pelo Usuário!!\033[m')
            return 0
        else:
            return n

def leiaFloat(txt):
    while True:
        try:
            f = float(input(txt))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO \033[m.')
            continue
        except KeyboardInterrupt:
            print('Entrada de Dados interrompida pelo Usuário!!')
            return 0
        else:
            return f

n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'O valor inteiro Digitado foi {n} e o real foi {f}')

print('Desafio114')
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site {site} não está acessível no momento.')
else:
    print(f'Consegui acessar o site {site} com sucesso!')
    # print(site.read())

print('Desafio115')
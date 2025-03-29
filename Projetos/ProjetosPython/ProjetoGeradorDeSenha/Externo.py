import Interno
from Interno import Escolhas, titulo


def GDS():
    while True:
        titulo('Gerador De Senhas')
        print('''[1] Criar uma Senha
[2] Sair do programa
        ''')
        hm = Escolhas()
        if hm == 2:
            break

GDS()


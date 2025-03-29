from Módulos.MenuEx115 import Linha
from Módulos.MenuEx115.opções.arquivo import arquivoExiste,arquivoCriar,cadastro,lerArquivo
from time import sleep
from Módulos.MenuEx115 import leiaInt
def opcoes(a):
    arquivo = 'Pcadastradas.txt'
    if not arquivoExiste(arquivo):
        arquivoCriar(arquivo)
    if a == 1:
        Linha('PESSOAS CADASTRADAS')
        lerArquivo(arquivo)
        sleep(2)
    elif a == 2:
        Linha('CADASTRAR PESSOAS')
        Nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arquivo,Nome,idade)
    elif a == 3:
        Linha('Saindo do sistema... Até Depois!!!!')
        sleep(2)
    return a




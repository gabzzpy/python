from Módulos.utilidades.moedas import resumo
def leiaDinheiro(n):
    válido = False
    while not válido:
        entrada = str(input(n)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{n}\". Preço Inválido\033[m')
        else:
            válido = True
            return float(entrada)

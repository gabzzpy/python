def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arquivoCriar(nome):
    a = open(nome,'wt+')
    a.close()

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
def cadastro(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo')
    else:
        try:
            a.write((f'{nome};{idade}\n'))
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro feito com sucesso!!')
            a.close()

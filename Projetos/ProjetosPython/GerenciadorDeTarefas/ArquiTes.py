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
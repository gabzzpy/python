from dbcontrol import *
from tkinter import filedialog
from PIL import Image, ImageTk
from string import ascii_letters,punctuation
#['gabzz',1,'gabzz@gabzz.com','1234']
edit = what = img_atual = None
contador = 0

def Organizar_imagens(path,x,y):
    imagem_original = Image.open(path)
    imagem_redimensionada = imagem_original.resize((x, y))
    imagem_atualizada = ImageTk.PhotoImage(imagem_redimensionada)
    return imagem_atualizada

def Login(useroremail='',senha=''):
    global user_in_moment
    try:
        rows = get_lines('users')
        check = False
        for row in rows:
            userdb = row[1]
            emaildb = row[2]
            senhadb = row[3]
            if (userdb == useroremail or emaildb == useroremail) and senhadb == senha:
                check = True
                user_in_moment = [userdb,row[4],row[2],row[3],row[0]]
                return(True,'Logado com Sucesso!',user_in_moment)
            
    except Error as e:
        print('ERRO:', e)
        return (False,e)

    else:
        if not check:
            return(False,'Alguma das informações está inválida')

def Register(user='',email='',senha=''):
    return create_user(user,email,senha)
    

def AdicionarJogos(nome,genero,desenvolvedor,data,sinopse):
    global img_atual
    checagem_data = False
    if nome == '' or genero == '' or desenvolvedor == '' or data == '' or sinopse == '':
        return (False,'Existe alguma informação faltando')
    elif data:
        check_data = CorrigirDATA(data)

        if check_data[0]:
            checagem_data = True
        if not check_data[0]:
            return check_data

    if checagem_data:
        if not img_atual:
            print('Não tem imagem selecionada')
            return (False, "Nenhuma imagem foi selecionada para o jogo")
        else:
            try:
                print('A função create_game será executada')
                check = create_game(nome, genero, desenvolvedor, data, sinopse, img_atual)
                if check[0]:  # Se o jogo foi criado com sucesso, limpa a imagem atual
                    img_atual = None
                print(check)
                return check
            except Exception as e:
                print('Erro ao criar o jogo')
                return (False, f"Erro ao criar o jogo: {e}")

def SelecionarImagens():
    global img_atual
    caminho_arquivo = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=[("Arquivos de imagem", "*.png;")])
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, "rb") as arquivo:
                img_atual = arquivo.read()
        except Error as e:
            print(e)
            print('Não deu Bom por essa imagem aew')
            return (False,'A imagem não foi selecionada')
        else:
            return (True,'Imagem Colocada com Sucesso!')

def Edit_or_remove(edit_or_remove='',what='',where='',change=''):
    print(edit_or_remove,what,where)
    if edit_or_remove == '' or what == ''or where == '':
        return (False,'Existe alguma informação faltando')
    try:
        error = edit_game(edit_or_remove=edit_or_remove,what=what,where=where,change=change)
    except Error as e:
        print(e)
        return (False,'Não foi possível realizar a ação')
    else:
        return error
     
def PegarImagemdaDB():
    CorrigirIDS()
    try:
        rows = get_lines('JOGOS')
        for row in rows:
            try:
                with open(f'ImagensJogos/Jogo{row[0]}.png', "wb") as file:
                    file.write(row[6])
            except:
                continue
    except Error as e:
        print(f"Erro ao extrair imagem: {e}")

    else:
        print('Imagens Extraídas com Sucesso!')

def ColocarJogos(id_user,id_jogo,text):
    checagem_data = False
    if id_user == '' or id_jogo == '' or text == '':
        return (False,'Existe alguma informação faltando')
    try:
        print('A função ColocarJogos será executada')
        check = create_bibliouser(id_user=id_user,id_jogo=id_jogo,text=text)
        return check
    except Exception as e:
            print('Erro ao adicionar o jogo na biblioteca')
            return (False, f"Erro ao adicionar o jogo: {e}")

import os # Função feita usando GPT, pois não sei utilizar biblioteca OS e só faltava isso para terminar
def apagar_fotos_pasta(caminho_pasta):
    # Verifica se a pasta existe
    if not os.path.exists(caminho_pasta):
        print("A pasta não existe.")
        return

    # Pega a lista de arquivos na pasta
    arquivos = os.listdir(caminho_pasta)

    # Apaga cada arquivo dentro da pasta
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)  # Caminho completo do arquivo
        
        if os.path.isfile(caminho_arquivo):  # Se for um arquivo, apaga
            os.remove(caminho_arquivo)
        elif os.path.isdir(caminho_arquivo):  # Se for uma pasta, apaga junto com o que tem dentro
            os.rmdir(caminho_arquivo)  # Só funciona se a pasta estiver vazia

    print("Todos os arquivos foram apagados!")



from customtkinter import *
from PIL import Image,ImageTk
from functions import *
from random import randint

# Cores
Verde_Escuro = '#011E11'
Verde_Escuro_Editar = '#1a4330'
Cinza_Editar = '#4c4c4c'
Verde_Neon = '#12FF46'
Verde_Claro1 = '#2ECC71'
Verde_Claro2 = '#20cd8d'
Branco = '#FFFFFF'
Verde_erro = '#528e78'
Azul_erro= '#5ce1e6'
Preto = '#000000' 
Vermelho_Neon = '#ff1212'
Verde_Escuro_Dados = '#172627'
Verde_Biblioteca = '#222b21'
azul_Lista = '#084383'

# Criação da Janela Principal
janela = CTk()
janela.geometry('1280x720')
janela.title('SuperIF Steam')
janela.config(bg=Branco)
janela.resizable(False,False)
janela.iconbitmap("Imagens/logosuperifnobg.ico")

# Funções usadas durante o código para poupar linhas
def Apagar():
    try:
        list =['senha_entry.delete(0,END)','email_entry.delete(0,END)','usuario_entry.delete(0,END)','email_label.place_forget()','senha_label.place_forget()',
            'usuario_label.place_forget()','cadastro_label.place_forget()','cadastro_button.place_forget()','return_button.place_forget()','email_entry.place_forget()','voltar.place_forget()',
            'Gênero_entry.delete(0,END)','info_1_entry.delete(0,END)','info_2_entry.delete(0,END)','Sinopse_entry.delete(0,END)','Nome_do_jogo_entry.delete(0,END)','Desenvolvedor_entry.delete(0,END)',
            'Data_lançamento_entry.delete(0,END)','info_1_label.place_forget()','info_2_label.place_forget()','info_1_entry.place_forget()','info_2_entry.place_forget()','enviar_button.place_forget()',
            'name_user.place_forget()','Imagem_User.place_forget()','Login_Button_Password.place_forget()','usuario_entry2.delete(0,END)','senha_entry2.delete(0,END)','email_entry2.delete(0,END)','Login_Button_Password2.place_forget()',
                'Mostrar_Mensagens.place_forget()','GameSelect.place_forget()']
        for value in list:
            eval(value)
    except:
        pass

def ApagarFrame():
    try:
        list =['lista_gFrame.place_forget()','adicionar_gFrame.place_forget()','delete_gFrame.place_forget()','dados_uFrame.place_forget()','biblioteca_gFrame.place_forget()']
        for value in list:
            eval(value)
    except:
        pass

user_in_moment = []

# Tela Inicial
def GoLoginPage(register='no'):
    if register == 'yes':
        senha = senha_entry.get()
        email = email_entry.get()
        user = usuario_entry.get()
        check = Register(user,email,senha)
        if check[1] != 'Usuário Criado com Sucesso!':
            GoRegisterPage()
        Posicionar_Erro(check[1])
    else:
        Apagar()
        senha_entry.configure(show='*')

        global imagem_tk
        Tela_Inicial.place_forget()
        Tela_Login.place(x=0,y=0)

        titulo.configure(text='Iniciar Sessão',font=('DM Sans',50,'bold'))
        titulo.place(x=70,y=60)
        subtitulo.configure(font=('DM Sans',15),text='Entre na sua conta')
        subtitulo.place(x=80,y=140)

        usuario_label.configure(font=('DM Sans',20,'bold'),text='USUÁRIO')
        usuario_label.place(x=90,y=200)
        usuario_entry.place(x=80,y=250)

        senha_label.configure(font=('DM Sans',20,'bold'),text='SENHA')
        senha_label.place(x=90,y=310)
        senha_entry.place(x=80,y=360)

        Login_Button_Password.place(x=530,y=360)

        entrar.configure(font=('Neue Machina',15,'bold'),text='ENTRAR',corner_radius=30,height=60,width=200,command=use_Login_function)
        entrar.place(x=90,y=420)

        imagem_tk = Organizar_imagens("Imagens/Tela_LoginIMG.png",633,699)
        Imagem_Jogo.configure(image=imagem_tk)
        Imagem_Jogo.place(x=700,y=80)

        cadastro_label.configure(font=('DM Sans',22),text='Não tem uma conta?')
        cadastro_label.place(x=90,y=520)
        cadastro_button.configure(font=('DM Sans',22,'bold'),text='CADASTRE-SE',command=GoRegisterPage)
        cadastro_button.place(x=95,y=545)

Tela_Inicial = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)
Tela_Inicial.place(x=0,y=0)

titulo = CTkLabel(Tela_Inicial,text='Jogue Agora\nna SuperIF\nSteam',fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',80,'bold'),anchor=E)
titulo.place(x=100,y=180)

iniciar_sessao = CTkButton(Tela_Inicial,corner_radius=20,command=GoLoginPage,text='Iniciar Sessão',font=('Neue Machina',18,'bold'),fg_color=Verde_Neon,text_color=Verde_Escuro,height=60,width=450,hover_color=Verde_Claro1)
iniciar_sessao.place(x=100,y=550)

nome_do_app = CTkLabel(Tela_Inicial,text='SUPERIF STEAM',fg_color=Verde_Escuro,text_color=Verde_Neon,font=('Neue Machina',25,'bold'),anchor=E)
nome_do_app.place(x=80,y=40)

# Imagem Tela de Início
imagem_tk = Organizar_imagens("Imagens/Tela_InicialIMG.png",633,699)
Imagem_Jogo = CTkLabel(Tela_Inicial, image=imagem_tk, text="")
Imagem_Jogo.place(x=700, y=70)  


# Tela de Login
def GoRegisterPage():
    Apagar()
    
    global imagem_tk
    senha_entry.configure(show='*')

    Tela_Inicial.place_forget()
    Tela_Login.place(x=0,y=0)

    titulo.configure(text='Registre-se',font=('DM Sans',50,'bold'))
    titulo.place(x=70,y=60)
    subtitulo.configure(font=('DM Sans',15),text='Crie sua conta')
    subtitulo.place(x=80,y=140)

    usuario_label.configure(font=('DM Sans',20,'bold'),text='USUÁRIO')
    usuario_label.place(x=90,y=180)
    usuario_entry.place(x=80,y=230)

    senha_label.configure(font=('DM Sans',20,'bold'),text='SENHA')
    senha_label.place(x=90,y=380)
    senha_entry.place(x=80,y=430)
    Login_Button_Password.place(x=530,y=430)

    email_label.place(x=90,y=280)
    email_entry.place(x=80,y=330)

    entrar.configure(font=('Neue Machina',15,'bold'),text='CRIAR',corner_radius=30,height=60,width=200,command=lambda:GoLoginPage('yes'))
    entrar.place(x=90,y=500)

    return_button.configure(font=('Neue Machina',15,'bold'),text='VOLTAR',corner_radius=15,height=30,width=80)
    return_button.place(x=90,y=600)

    imagem_tk = Organizar_imagens("Imagens/Tela_RegistroIMG.png",633,699)
    Imagem_Jogo.configure(image=imagem_tk)
    Imagem_Jogo.place(x=700,y=80)

def use_Login_function():
    useroremail = usuario_entry.get()
    senha = senha_entry.get()
    mensagem = Login(useroremail,senha)
    Posicionar_Erro(mensagem[1])
    if mensagem[0] == True:
        global user_in_moment
        user_in_moment = mensagem[2]
        print(user_in_moment)
        Apagar()
        GoPrincipalPage()


Tela_Login = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)

titulo = CTkLabel(Tela_Login,fg_color=Verde_Escuro,text_color=Verde_Neon)
subtitulo = CTkLabel(Tela_Login,fg_color=Verde_Escuro,text_color=Verde_Neon)

usuario_label = CTkLabel(Tela_Login,fg_color=Verde_Escuro,text_color=Verde_Neon)
usuario_entry = CTkEntry(Tela_Login,font=('DM Sans',20),fg_color=Verde_Escuro,text_color=Branco,width=420)
usuario_entry.insert(0,'Digite aqui o seu usuário* ')

senha_label = CTkLabel(Tela_Login,fg_color=Verde_Escuro,text_color=Verde_Neon)
senha_entry = CTkEntry(Tela_Login,font=('DM Sans',20),fg_color=Verde_Escuro,text_color=Branco,width=420)
senha_entry.insert(0,'Digite aqui a sua senha* ')

entrar = CTkButton(Tela_Login,fg_color=Verde_Neon,text_color=Verde_Escuro,hover_color=Verde_Claro1)

imagem_tk = Organizar_imagens("Imagens/Tela_LoginIMG.png",682,668) 
Imagem_Jogo = CTkLabel(Tela_Login,image=imagem_tk,text='')

cadastro_label = CTkLabel(Tela_Login,fg_color=Verde_Escuro,text_color=Branco)
cadastro_button = CTkButton(Tela_Login,fg_color=Verde_Escuro,text_color=Verde_Neon,hover_color=Verde_Escuro)


# Tela de Registro
email_label = CTkLabel(Tela_Login,font=('DM Sans',20,'bold'),text='EMAIL',fg_color=Verde_Escuro,text_color=Verde_Neon)
email_entry = CTkEntry(Tela_Login,font=('DM Sans',20),fg_color=Verde_Escuro,text_color=Branco,width=420)
email_entry.insert(0,'Digite aqui o seu email* ')
return_button = CTkButton(Tela_Login,fg_color=Verde_Neon,text_color=Verde_Escuro,hover_color=Verde_Claro1,text='VOLTAR',font=('Neue Machina',10,'bold'),command=GoLoginPage)

# Frames dos botões da tela principal
# Frame Adicionar Jogos
def GoAddgames():
    #Verificação Admin
    if user_in_moment[1] == 1:
        Apagar()

        global img_atual

        Tela_Principal.place_forget()
        adicionar_gFrame.place(x=0,y=0)

        detalhe_imagem_label.place(x=-40,y=-40)
        detalhe_verde_frame.place(x=700,y=60)
        por_img.place(x=120,y=200)
        por_img.configure(text='Selecione\na imagem')
        img_atual = None

        titulo3.place(x=40,y=40)
        widget_verde2.place(x=30,y=40)

        Nome_do_jogo_label.place(x=10,y=10)
        Nome_do_jogo_entry.place(x=10,y=45)

        Gênero_label.place(x=10,y=90)
        Gênero_entry.place(x=10,y=125)

        Desenvolvedor_label.place(x=10,y=170)
        Desenvolvedor_entry .place(x=10,y=205)

        Data_lançamento_label.place(x=10,y=250)
        Data_lançamento_entry.place(x=10,y=285)

        Sinopse_label.place(x=10,y=330)
        Sinopse_entry.place(x=10,y=365)

        adicionar_gButton2.place(x=125,y=455)

        voltar.place(x=60,y=120)
    else:
        Posicionar_Erro('Você não pode acessar essa aba pois não é administrador!')

def AdicionarJogo():
    genero = Gênero_entry.get()
    sinopse = Sinopse_entry.get()
    desenvolvedor = Desenvolvedor_entry.get()
    data = Data_lançamento_entry.get()
    nome = Nome_do_jogo_entry.get()
    check = AdicionarJogos(nome=nome,data=data,genero=genero,sinopse=sinopse,desenvolvedor=desenvolvedor)
    print(check)
    Posicionar_Erro(check[1])
    if check[0]:
        por_img.configure(text='Selecione\na imagem')
        Apagar()
        apagar_fotos_pasta("C:/Users/gabmo/OneDrive/Área de Trabalho/Estim/ImagensJogos")
        GoAddgames()
        Posicionar_Erro(check[1])
        voltar.place(x=60,y=120)
    
def SelecionarImagem():
    check = SelecionarImagens()
    Posicionar_Erro(check[1])

    global img_atual
    por_img.configure(image=img_atual,text='',anchor=N)

adicionar_gFrame = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)

detalhe_imagem_label = CTkLabel(adicionar_gFrame,image=Organizar_imagens("Imagens/PlanodeFundoAddGames.png",1700,1400) ,text='')

detalhe_verde_frame = CTkFrame(adicionar_gFrame,height=600,width=500,fg_color=Verde_Claro2)

Nome_do_jogo_label = CTkLabel(detalhe_verde_frame,fg_color=Verde_Claro2,text_color=Preto,text='Nome do jogo',font=('DM Sans',20,'bold'))
Nome_do_jogo_entry = CTkEntry(detalhe_verde_frame,fg_color=Verde_Claro2,font=('DM Sans',20),text_color=Branco,width=420)

Gênero_label = CTkLabel(detalhe_verde_frame,fg_color=Verde_Claro2,text_color=Preto,text='Gênero',font=('DM Sans',20,'bold'))
Gênero_entry = CTkEntry(detalhe_verde_frame,fg_color=Verde_Claro2,font=('DM Sans',20),text_color=Branco,width=420)
Desenvolvedor_label = CTkLabel(detalhe_verde_frame,fg_color=Verde_Claro2,text_color=Preto,text='Desenvolvedor(a)',font=('DM Sans',20,'bold'))
Desenvolvedor_entry = CTkEntry(detalhe_verde_frame,fg_color=Verde_Claro2,font=('DM Sans',20),text_color=Branco,width=420)

Data_lançamento_label = CTkLabel(detalhe_verde_frame,fg_color=Verde_Claro2,text_color=Preto,text='Data de Lançamento: (YYYY-MM-DD) ',font=('DM Sans',20,'bold'))
Data_lançamento_entry = CTkEntry(detalhe_verde_frame,fg_color=Verde_Claro2,font=('DM Sans',20),text_color=Branco,width=420)

Sinopse_label = CTkLabel(detalhe_verde_frame,fg_color=Verde_Claro2,text_color=Preto,text='Sinopse',font=('DM Sans',20,'bold'))
Sinopse_entry = CTkEntry(detalhe_verde_frame,fg_color=Verde_Claro2,font=('DM Sans',20),text_color=Branco,width=420)

adicionar_gButton2 = CTkButton(detalhe_verde_frame,text='ADICIONAR JOGO',font=('Neue Machina',20,'bold'),fg_color=Verde_Neon,text_color=Verde_Escuro,height=60,width=250,corner_radius=25,command=AdicionarJogo)

por_img = CTkButton(adicionar_gFrame,text='Selecione\na imagem',font=('DM Sans',40,'bold'),fg_color=Verde_Claro2,text_color=Verde_Escuro,height=300,width=250,corner_radius=0,command=SelecionarImagem)

titulo3 = CTkLabel(adicionar_gFrame,text='Adicionar\nJogos',font=('DM Sans',30,'bold'),fg_color="transparent")
widget_verde2 = CTkLabel(adicionar_gFrame,fg_color=Verde_Claro1,height=50,width=5,text='')

# Frame Listar Jogo
def GoListargames():
    Apagar()
    Tela_Principal.place_forget()
    lista_gFrame.place(x=0,y=0)

    lista_jogosFrame.place(x=200,y=0)
    detalhe_imagem_label3.place(x=-40,y=-40)

    titulo4.place(x=40,y=40)
    widget_verde2.place(x=30,y=40)

    voltar.place(x=30,y=150)

    Imagem_User.place(x=30,y=605)
    name_user.place(x=80,y=610)

    MostrarJogos()

def MostrarJogos():
    apagar_fotos_pasta("C:/Users/gabmo/OneDrive/Área de Trabalho/Estim/ImagensJogos")
    rows =  get_lines('JOGOS')
    PegarImagemdaDB()
    linha_label = 0
    linha_button = 1
    coluna = 0

    for row in rows:
        
        CTkLabel(lista_jogosFrame,text=f'{row[1]}',font=('DM Sans',20,'bold'),fg_color=azul_Lista,text_color=Branco).grid(row=linha_label,column=coluna,padx=80,pady=20)
        CTkButton(lista_jogosFrame,fg_color=azul_Lista,text_color=azul_Lista,image=Organizar_imagens(f'ImagensJogos/Jogo{row[0]}.png',200,300),text='',font=('Neue Machina',12,'bold'),corner_radius=25,hover_color='#3b77b8',command=lambda id_jogo=row: Posicionar_Sinopse(id_jogo[0])).grid(row=linha_button,column=coluna,padx=80,pady=20)

        coluna +=1
        if coluna == 3:
            coluna = 0
            linha_label += 2
            linha_button += 2

lista_gFrame = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)

detalhe_imagem_label3 = CTkLabel(lista_gFrame,image=Organizar_imagens("Imagens/PlanodeFundoAddGames.png",1700,1400) ,text='')

lista_jogosFrame = CTkScrollableFrame(lista_gFrame,height=720,width=1060,fg_color=azul_Lista)

titulo4 = CTkLabel(lista_gFrame,text=' Lista de\nJogos',font=('DM Sans',30,'bold'),fg_color="transparent",text_color=Branco)
widget_verde2 = CTkLabel(lista_gFrame,fg_color=Verde_Claro1,height=50,width=5,text='')


# Frame Remover Jogos
def GoRemovegames():
    #Verificação Admin
    if user_in_moment[1] == 1:
        Apagar()
        Tela_Principal.place_forget()
        delete_gFrame.place(x=0,y=0)

        detalhe_imagem_label2.place(x=-40,y=-40)
        detalhe_verde_frame2.place(x=100,y=300)

        titulo5.place(x=40,y=40)
        widget_verde4.place(x=30,y=40)

        titulo_question.place(x=480,y=20)

        Nome_do_jogo_Button.place(x=25, y=25)      
        Gênero_Button.place(x=25, y=100)         
        Desenvolvedor_Button.place(x=25, y=175)   
        Data_lançamento_Button.place(x=25, y=250) 
        Sinopse_Button.place(x=25, y=325) 
        Remover_Jogo.place(x=230,y=165)

        voltar.place(x=60,y=120)

    else:
        Posicionar_Erro('Você não pode acessar essa aba pois não é administrador!')

def ColocarEdits(EDIT='',WHAT=''):
    Apagar()
    voltar.place(x=60,y=120)

    if not EDIT and not WHAT:
        print('Como????')

    global edit
    global what
    edit = EDIT
    what = WHAT
    
    detalhe_cinza_frame.place(x=500,y=20)
    info_1_entry.place(x=20,y=200)
    info_1_label.place(x=20,y=150)
    if EDIT != 'remove':
        info_2_entry.place(x=20,y=70)
        info_2_label.place(x=20,y=20)

    enviar_button.place(x=235,y=270)

def EditorRemove():
    global edit
    global what

    if edit == '' or what == '':
        GoRemovegames()
        Posicionar_Erro('Selecione primeiro um botão')

    where = info_1_entry.get()
    change = info_2_entry.get()

    if edit == 'editar':
        erro = Edit_or_remove(edit_or_remove=edit,what=what,where=where,change=change)
    elif edit == 'remove':
        erro = Edit_or_remove(what=what,edit_or_remove=edit,where=where)

    if erro[0]:
        apagar_fotos_pasta("C:/Users/gabmo/OneDrive/Área de Trabalho/Estim/ImagensJogos")
        Apagar()
        GoRemovegames()
        voltar.place(x=60,y=120)
    Posicionar_Erro(erro[1])

delete_gFrame = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)

detalhe_imagem_label2 = CTkLabel(delete_gFrame,image=Organizar_imagens("Imagens/PlanodeFundoEditarGames.png",1700,1400) ,text='')

detalhe_verde_frame2 = CTkFrame(delete_gFrame,height=400,width=1080,fg_color=Verde_Claro2,corner_radius=2)
detalhe_cinza_frame = CTkFrame(detalhe_verde_frame2,height=360,width=550,fg_color=Cinza_Editar,corner_radius=25)

Nome_do_jogo_Button = CTkButton(detalhe_verde_frame2,fg_color=Verde_Neon,text_color=Verde_Escuro,text='NOME',font=('Neue Machina',12,'bold'),corner_radius=25,height=45,width=80,command=lambda:ColocarEdits('editar','nome'))
Gênero_Button = CTkButton(detalhe_verde_frame2,fg_color=Verde_Neon,text_color=Verde_Escuro,text='GÊNERO',font=('Neue Machina',12,'bold'),corner_radius=25,height=45,width=80,command=lambda:ColocarEdits('editar','genero'))
Desenvolvedor_Button = CTkButton(detalhe_verde_frame2,fg_color=Verde_Neon,text_color=Verde_Escuro,text='DESENVOLVEDOR',font=('Neue Machina',12,'bold'),corner_radius=25,height=45,width=80,command=lambda:ColocarEdits('editar','desenvolvedor'))
Data_lançamento_Button= CTkButton(detalhe_verde_frame2,fg_color=Verde_Neon,text_color=Verde_Escuro,text='DATA',font=('Neue Machina',12,'bold'),corner_radius=25,height=45,width=80,command=lambda:ColocarEdits('editar','data_de_lançamento'))
Sinopse_Button = CTkButton(detalhe_verde_frame2,fg_color=Verde_Neon,text_color=Verde_Escuro,text='SINOPSE',font=('Neue Machina',12,'bold'),corner_radius=25,height=45,width=80,command=lambda:ColocarEdits('editar','sinopse'))
Remover_Jogo = CTkButton(detalhe_verde_frame2,fg_color=Vermelho_Neon,text_color=Verde_Escuro,text='REMOVER',font=('Neue Machina',35,'bold'),corner_radius=25,height=65,width=70,command=lambda:ColocarEdits('remove','remove'))

info_1_label = CTkLabel(detalhe_cinza_frame,fg_color=Cinza_Editar,text_color=Branco,text='Nome ou ID do jogo',font=('DM Sans',20,'bold'))
info_1_entry = CTkEntry(detalhe_cinza_frame,fg_color=Cinza_Editar,font=('DM Sans',20),text_color=Branco,width=420,border_color=Verde_Escuro)
info_2_label = CTkLabel(detalhe_cinza_frame,fg_color=Cinza_Editar,text_color=Branco,text='Informação que deseja atualizar',font=('DM Sans',20,'bold'))
info_2_entry = CTkEntry(detalhe_cinza_frame,fg_color=Cinza_Editar,font=('DM Sans',20),text_color=Branco,width=420,border_color=Verde_Escuro)
enviar_button = CTkButton(detalhe_cinza_frame,fg_color=Verde_Neon,text_color=Verde_Escuro,text='ENVIAR',font=('Neue Machina',12,'bold'),corner_radius=25,height=45,width=80,command=EditorRemove)

titulo5 = CTkLabel(delete_gFrame,text='Editar\nJogos',font=('DM Sans',30,'bold'),fg_color='#5fd5ff',text_color=Branco)
widget_verde4 = CTkLabel(delete_gFrame,fg_color=Verde_Claro1,height=45,width=5,text='')
titulo_question = CTkLabel(delete_gFrame,text='Qual das informações\ndeseja editar?',font=('DM Sans',30,'bold'),fg_color='#5fd5ff',text_color=Branco)


# Frame Dados do Usuário
def GoDados():
    Apagar()

    voltar.place(x=30,y=80)

    Tela_Principal.place_forget()
    dados_uFrame.place(x=0,y=0)

    detalhe_cinza_frame2.place(x=390,y=35)

    usuario_label2.place(x=173,y=150)
    usuario_entry2.insert(0,f'{user_in_moment[0]}')
    usuario_entry2.configure(state="readonly")
    usuario_entry2.place(x=40,y=200)

    senha_label2.place(x=173,y=250)
    senha_entry2.insert(0,f'{user_in_moment[3]}')
    senha_entry2.configure(state="readonly")
    senha_entry2.place(x=40,y=300)

    email_label2.place(x=173,y=350)
    email_entry2.insert(0,f'{user_in_moment[2]}')
    email_entry2.configure(state="readonly")
    email_entry2.place(x=40,y=400)

    Login_Button_Password2.place(x=710,y=290)
    editar_info_Button.place(x=125,y=510)

    Imagem_User2.place(x=190,y=0)
    editar_info_Button.configure(command=GoDados2)

def GoDados2():
    usuario_entry2.configure(state="normal")
    senha_entry2.configure(state="normal")
    email_entry2.configure(state="normal")

    Apagar()

    Posicionar_Erro('Edite seus dados, deixe em branco o que não quiser mudar')

    voltar.place(x=30,y=80)
    Login_Button_Password2.place(x=710,y=290)

    editar_info_Button.configure(command=EditDados)
    
def EditDados():
    user = usuario_entry2.get()
    senha = senha_entry2.get()
    email = email_entry2.get()
    user_old = user_in_moment[0]
    password_old = user_in_moment[3]
    email_old =  user_in_moment[2]

    if user == '' and senha == '' and email == '':
        GoPrincipalPage()
        Posicionar_Erro('Não existe o que atualizar, essas já são suas informações')
        
    else:
        if user == '':
            user = user_old
        if senha == '':
            senha = password_old
        if email == '':
            email = email_old

        check = edit_user(user_old=user_old,email=email,senha=senha,user=user)

        if check[0]:
            Tela_Principal.place_forget()
            ApagarFrame()
            Tela_Inicial.place(x=0,y=0)
            Apagar()

            editar_info_Button.configure(command=GoDados)
        Posicionar_Erro(check[1])

dados_uFrame = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro_Dados)

detalhe_cinza_frame2 = CTkFrame(dados_uFrame,height=650,width=500,fg_color=Verde_Claro2,corner_radius=25)

imagem_tk2 = Organizar_imagens(f"Imagens/user_image.png",150,150)
Imagem_User2 = CTkLabel(detalhe_cinza_frame2,image=imagem_tk2,text='',fg_color=Verde_Claro2)

usuario_label2 = CTkLabel(detalhe_cinza_frame2,fg_color=Verde_Claro2,text_color=Preto,text=F'USUÁRIO:',width=154,font=('Neue Machine',30,'bold'))
usuario_entry2 = CTkEntry(detalhe_cinza_frame2,font=('DM Sans',20),fg_color=Branco,text_color=Preto,width=420)

senha_label2 = CTkLabel(detalhe_cinza_frame2,fg_color=Verde_Claro2,text_color=Preto,font=('Neue Machine',30,'bold'),width=154,text='SENHA:')
senha_entry2 = CTkEntry(detalhe_cinza_frame2,font=('DM Sans',20),fg_color=Branco,text_color=Preto,width=420)

email_label2 = CTkLabel(detalhe_cinza_frame2,fg_color=Verde_Claro2,text_color=Preto,text=f'EMAIL:',font=('Neue Machine',30,'bold'),width=154)
email_entry2 = CTkEntry(detalhe_cinza_frame2,font=('DM Sans',20),fg_color=Branco,text_color=Preto,width=420)

editar_info_Button = CTkButton(detalhe_cinza_frame2,fg_color=Preto,text_color=Branco,text='EDITAR\nINFORMAÇÕES',font=('Neue Machina',25,'bold'),corner_radius=25,height=55,width=250,command=GoDados2)

# Frame Biblioteca Jogos
def GoBibliotecagames():
    Apagar()
    Tela_Principal.place_forget()
    biblioteca_gFrame.place(x=0,y=0)

    biblioteca_jogosFrame.place(x=200,y=0)

    detalhe_imagem_label4.place(x=-20,y=-40)

    titulo6.place(x=20,y=40)
    widget_verde3.place(x=10,y=40)

    voltar.place(x=30,y=150)

    Imagem_User.place(x=30,y=605)
    name_user.place(x=80,y=610)

    MostrarJogosBiblio()

def AdicionarJogoBiblioteca(id,text):
    id_jogo = id
    id_user = user_in_moment[4]

    check = ColocarJogos(id_user,id_jogo,text)
    Posicionar_Erro(check[1])

def MostrarJogosBiblio():
    apagar_fotos_pasta("C:/Users/gabmo/OneDrive/Área de Trabalho/Estim/ImagensJogos")
    rows =  get_lines('BIBLIOTECA')
    rows_j = get_lines('JOGOS')
    PegarImagemdaDB()
    linha_label = 0
    linha_button = 1
    coluna = 0

    for row in rows:
        if row[1] == user_in_moment[4]:
            for row_j in rows_j:
                if row_j[0] == row[2]:
                    nome_j = row_j[1]
            CTkLabel(biblioteca_jogosFrame,text=f'{nome_j}',font=('DM Sans',20,'bold'),fg_color=Verde_Biblioteca,text_color=Verde_Neon).grid(row=linha_label,column=coluna,padx=80,pady=20)
            CTkButton(biblioteca_jogosFrame,fg_color=Verde_Biblioteca,text_color=Verde_Biblioteca,image=Organizar_imagens(f'ImagensJogos/Jogo{row[2]}.png',200,300),text='',font=('Neue Machina',12,'bold'),corner_radius=25,hover_color=Cinza_Editar,command=lambda id_jogo=row: Posicionar_GameSelect(id_jogo)).grid(row=linha_button,column=coluna,padx=80,pady=20)

            coluna +=1
            if coluna == 3:
                coluna = 0
                linha_label += 2
                linha_button += 2

biblioteca_gFrame = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)

detalhe_imagem_label4 = CTkLabel(biblioteca_gFrame,image=Organizar_imagens("Imagens/PlanodeFundoBIBLIOTECA.png",1700,1400) ,text='')

biblioteca_jogosFrame = CTkScrollableFrame(biblioteca_gFrame,height=720,width=1060,fg_color=Verde_Biblioteca)

titulo6 = CTkLabel(biblioteca_gFrame,text=' Biblioteca de\nJogos',font=('DM Sans',28,'bold'),fg_color="transparent",text_color=Branco)
widget_verde3 = CTkLabel(biblioteca_gFrame,fg_color=Verde_Claro1,height=50,width=5,text='')





# Tela Principal
def GoPrincipalPage():
    Apagar()
    ApagarFrame()

    Tela_Login.place_forget()
    Tela_Principal.place(x=0,y=0)

    name_user.configure(text=f'{user_in_moment[0]}')

    titulo2.place(x=40,y=40)
    widget_verde.place(x=30,y=40)

    adicionar_gButton.place(x=420,y=60)
    delete_gButton.place(x=420,y=380)
    lista_gButton.place(x=690,y=60)
    dados_uButton.place(x=960,y=60)
    biblioteca_gButton.place(x=60,y=280)

    Imagem_Jogo2.place(x=690,y=380)
    Imagem_User.place(x=30,y=145)
    name_user.place(x=80,y=150)

    PassarImagens()

def PassarImagens():
    global contador
    contador += 1
    if contador == 10:
        contador = 0
        imagem_tk = Organizar_imagens(f"Imagens/Paisagem{randint(1,14)}.png",647,380)
        Imagem_Jogo2.configure(image=imagem_tk)
        Imagem_Jogo2.place(x=690,y=380)

    Imagem_Jogo2.after(1000,PassarImagens)

Tela_Principal = CTkFrame(janela,height=720,width=1280,fg_color=Verde_Escuro)

titulo2 = CTkLabel(Tela_Principal,text='SuperIF\nSteam',font=('DM Sans',40,'bold'))
widget_verde = CTkLabel(Tela_Principal,fg_color=Verde_Claro1,height=50,width=5,text='')

imagem_tk = Organizar_imagens(f"Imagens/Paisagem3.png",647,380)
Imagem_Jogo2 =CTkLabel(Tela_Principal,image=imagem_tk,text='')

adicionar_gButton = CTkButton(Tela_Principal,text='Adicionar\nJogos',anchor=SW,font=('DM Sans',40,'bold'),fg_color=Verde_Claro2,text_color=Verde_Escuro,height=300,width=250,corner_radius=25,command=GoAddgames)
lista_gButton = CTkButton(Tela_Principal,text='Lista de\nJogos',anchor=SW,font=('DM Sans',40,'bold'),fg_color=Verde_Claro2,text_color=Verde_Escuro,height=300,width=250,corner_radius=25,command=GoListargames)
dados_uButton = CTkButton(Tela_Principal,text='Dados do\nUsuário',anchor=SW,font=('DM Sans',40,'bold'),fg_color=Verde_Claro2,text_color=Verde_Escuro,height=300,width=250,corner_radius=25,command=GoDados)
delete_gButton = CTkButton(Tela_Principal,text='Editar\nJogos',anchor=SW,font=('DM Sans',40,'bold'),fg_color=Verde_Claro2,text_color=Verde_Escuro,height=300,width=250,corner_radius=25,command=GoRemovegames)
biblioteca_gButton = CTkButton(Tela_Principal,text='Biblioteca',image=Organizar_imagens(f"Imagens/biblioteca.png",320,320),compound='top',anchor=SW,font=('DM Sans',40,'bold'),command=GoBibliotecagames,fg_color=Verde_Claro2,text_color=Verde_Escuro,height=400,width=250,hover_color=Verde_Claro2,corner_radius=25)


# Coisas para terem prioridade na tela
voltar  = CTkButton(janela,text='Voltar',font=('Neue Machina',15,'bold'),fg_color=Verde_Escuro,text_color=Verde_Neon,height=40,width=100,corner_radius=15,command=GoPrincipalPage)

name_user = CTkLabel(janela,text=f'',font=('DM Sans',20,'bold'),fg_color=Verde_Escuro)
imagem_tk2 = Organizar_imagens(f"Imagens/user_image.png",50,50)
Imagem_User = CTkLabel(janela,image=imagem_tk2,text='',fg_color=Verde_Escuro)

# Função para mostrar as informações na Entry password, ao invés de ficar em *
def Show_Infos():
    senha_entry.configure(show='')
    senha_entry2.configure(show='')
    Login_Button_Password.configure(command=Show_Infos2)
    Login_Button_Password2.configure(command=Show_Infos2)
    
def Show_Infos2():
    senha_entry.configure(show='*')
    senha_entry2.configure(show='*')
    Login_Button_Password.configure(command=Show_Infos)
    Login_Button_Password2.configure(command=Show_Infos)

Login_Button_Password = CTkButton(janela,fg_color=Verde_Neon,font=('DM Sans',10,'bold'),text_color=Verde_Escuro,corner_radius=20,text='Show',width=20,command=Show_Infos)
Login_Button_Password2 = CTkButton(janela,fg_color=Verde_Escuro_Dados,font=('DM Sans',10,'bold'),text_color=Verde_Neon,corner_radius=0,text='Show',width=20,command=Show_Infos)
senha_entry.configure(show='*')
senha_entry2.configure(show='*')

# Frame para Sinopse
def Posicionar_Sinopse(id):
    rows =  get_lines('JOGOS')
    label_sinopse.configure(state="normal")
    label_sinopse.delete('1.0',END)
    for row in rows:
        if row[0] == id:
            sinopse = row[5]
            text = f'O usuário {user_in_moment[1]} adicionou o jogo {row[1]}'
    print(sinopse)
    print(id)
    Mostrar_Sinopse.place(x=340,y=155)
    label_sinopse.insert('1.0',f'Sinopse:\n\n{sinopse}')
    label_sinopse.configure(state="disabled")
    label_sinopse.place(x=00,y=0)
    botao_sinopse.place(x=130,y=400)
    botao_sinopse.configure(command=lambda:AdicionarJogoBiblioteca(id=id,text=text))
    botao_sinopse_sair.place(x=420,y=400)

def SairErro2():
    Mostrar_Sinopse.place_forget()

Mostrar_Sinopse = CTkFrame(janela,width=700,height=500,fg_color='#6eaaeb',corner_radius=5)
label_sinopse = CTkTextbox(Mostrar_Sinopse,fg_color='#6eaaeb',text_color=Branco,font=('DM Sans',25,'bold'),width=700,height=400)
botao_sinopse = CTkButton(Mostrar_Sinopse,fg_color=Verde_Neon,font=('DM Sans',20,'bold'),text_color=Preto,corner_radius=20,text='Adicionar',width=150)
botao_sinopse_sair = CTkButton(Mostrar_Sinopse,fg_color=Vermelho_Neon,font=('DM Sans',20,'bold'),text_color=Verde_Escuro,corner_radius=20,text='Sair',width=150,command=SairErro2)

# Frame para Tela GameSelect
def Posicionar_GameSelect(linha_tabela):
    rows =  get_lines('JOGOS')

    for row in rows:
        if row[0] == linha_tabela[2]:
            label_sinopse2.configure(state="normal")
            label_sinopse2.delete('1.0',END)

            label1.configure(image=Organizar_imagens(f'ImagensJogos/Jogo{row[0]}.png',160,260))
            label1.place(x=80,y=120)

            if len(row[1]) > 30:
                label2.configure(font=('DM Sans',18,'bold'))
            else:
                label2.configure(font=('DM Sans',25,'bold'))

            label2.configure(text=f'{row[1]}')
            label2.place(x=63,y=340)

            label3.configure(text=f'{row[2]}')
            label3.place(x=560,y=340)

            label4.configure(text=f'{linha_tabela[4]} horas')
            label4.place(x=320,y=340)

            label5.configure(text=f'{row[3]}')
            label5.place(x=320,y=460)

            label6.configure(text=f'{row[4]}')
            label6.place(x=650,y=460)

            label_sinopse2.insert('1.0',f'Sinopse:\n\n{row[5]}')
            
            label_sinopse2.configure(state="disabled")
            label_sinopse2.place(x=260,y=130)

            botao_mudar_horas.configure(command=lambda:Posicionar_MudarHoras(linha_tabela[0]))

    GameSelect.place(x=190,y=60)
    label_GameSelect.place(x=-20,y=0)
    botao_GameSelect_sair.place(x=420,y=550)
    botao_mudar_horas.place(x=120,y=550)



def SairErro3():
    GameSelect.place_forget()


# Frame para mudar horas
def Posicionar_MudarHoras(onde):
    Frame_MudarHoras.place(x=440,y=210)
    label_mudar_horas.place(x=58,y=100)
    entry_mudar_horas.place(x=90,y=150)

    botao_mudar_horas2.configure(command=lambda:MudarHoras(onde))
    botao_mudar_horas2.place(x=125,y=200)

def MudarHoras(onde):
    tempo = entry_mudar_horas.get()
    check = Mudar_Horas_Jogadas(onde,tempo)
    Posicionar_Erro(check[1])
    if check[0]:
        Frame_MudarHoras.place_forget()
        GoBibliotecagames()

GameSelect = CTkFrame(janela,width=900,height=600,fg_color=Verde_Escuro,corner_radius=5)
Frame_MudarHoras = CTkFrame(janela,width=400,height=300,fg_color=Verde_Escuro,corner_radius=5)
label_GameSelect = CTkLabel(GameSelect,text='',fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'),width=700,height=400,image=Organizar_imagens(f'Imagens/GameSelect.png',1200,750))
botao_GameSelect_sair = CTkButton(GameSelect,fg_color=Vermelho_Neon,font=('DM Sans',20,'bold'),text_color=Verde_Escuro,corner_radius=20,text='Sair',width=150,command=SairErro3,hover_color=Verde_Claro1)
label_sinopse2 = CTkTextbox(GameSelect,fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'),width=600,height=120,corner_radius=0)


label1 = CTkLabel(GameSelect,text='',fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'))
label2 = CTkLabel(GameSelect,fg_color=Verde_Claro2,text_color=Branco,font=('DM Sans',25,'bold'),anchor=CENTER,width=80)
label3 = CTkLabel(GameSelect,fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'),anchor=CENTER)
label4 = CTkLabel(GameSelect,fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'),anchor=CENTER)
label5 = CTkLabel(GameSelect,fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'),anchor=CENTER)
label6 = CTkLabel(GameSelect,fg_color=Verde_Escuro,text_color=Branco,font=('DM Sans',25,'bold'),anchor=CENTER)
    
botao_mudar_horas = CTkButton(GameSelect,fg_color=Verde_Neon,font=('DM Sans',20,'bold'),text_color=Verde_Escuro,corner_radius=20,text='Mudar Horas Jogadas',width=150,hover_color=Verde_Claro1)

label_mudar_horas = CTkLabel(Frame_MudarHoras,fg_color=Verde_Claro2,text_color=Preto,text=f'Digite a quantidade de horas:',font=('Neue Machine',20,'bold'),width=284)
entry_mudar_horas= CTkEntry(Frame_MudarHoras,font=('DM Sans',20),fg_color=Branco,text_color=Preto,width=220)
botao_mudar_horas2 = CTkButton(Frame_MudarHoras,fg_color=Verde_Neon,font=('DM Sans',20,'bold'),text_color=Verde_Escuro,corner_radius=20,text='Enviar',width=150,hover_color=Verde_Claro1)



# Frame para casos de erro
def Posicionar_Erro(txt):
    print('Deu o seguinte erro',txt)
    Mostrar_Mensagens.place(x=440,y=260)
    label_erro.configure(text=f'{txt}')
    label_erro.place(x=70,y=40)
    botao_erro.place(x=130,y=150)

def SairErro():
    Mostrar_Mensagens.place_forget()

Mostrar_Mensagens = CTkFrame(janela,width=400,height=200,fg_color=Verde_erro,corner_radius=5)
label_erro = CTkLabel(Mostrar_Mensagens,anchor='center',fg_color=Verde_erro,text_color=Azul_erro,font=('DM Sans',25,'bold'),wraplength=268,text='',width=60,height=80)
botao_erro = CTkButton(Mostrar_Mensagens,fg_color=Verde_Neon,font=('DM Sans',20,'bold'),text_color=Preto,corner_radius=20,text='Sair',command=SairErro)

# Fim
'''user_in_moment = ['admin',1,'admin','admin',1]
name_user.configure(text=f'{user_in_moment[0]}')'''

janela.mainloop()

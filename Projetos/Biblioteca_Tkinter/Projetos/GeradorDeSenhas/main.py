from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from random import sample
import string

# Cores
Black = '#000000'
White = '#FFFFFF'
Red = '#FF0000'
Green = '#00FF00'
Blue = '#0000FF'
Light_Gray = '#464f6b'
Yellow = '#FFFF00'
Gray = '#808080'
Orange = '#d17702'
Purple = '#800080'

# -- Base --
janela = Tk()
janela.geometry('295x350')
janela.title('Gerador de Senhas')
janela.resizable(False,False)
janela.config(bg=White)
janela.iconphoto(False,PhotoImage(file='Projetos\GeradorDeSenhas\chave.png'))

# -- Funções e Variáveis --
senha=''
def GerarSenha():
    global senha
    simbolos = string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    alfabeto_menor = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_maior = string.ascii_uppercase # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = string.digits # '0123456789'
    all= ''
    if check1.get():
        all += alfabeto_maior

    if check2.get():
        all += alfabeto_menor

    if check3.get():
        all += simbolos

    if check4.get():
        all += numeros

    comprimento = int(caracteres.get())
    for c in range(comprimento):
        senha = ''.join(sample(all,comprimento))
    label_senha['text'] = senha

    def Copiar():
        global senha
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)
        messagebox.showinfo('Sucesso!','A senha foi copiada com Sucesso.')

    # Botão só aparece depois de copiar
    copiar = Button(frame_baixo, text='Copiar', relief='solid', width=7, height=2, font='Ivy 8',command=Copiar)
    copiar.place(x=235, y=15)

# -- Divisão de Frames
frame_cima = Frame(width=295,height=60,bg=White)
frame_cima.grid(row=0,column=0)

frame_baixo = Frame(width=295,height=310,bg=White)
frame_baixo.grid(row=1,column=0)

# -- Criação de Widgets de cima

# -- Labels
img= Image.open('Projetos\GeradorDeSenhas\senha.jpeg')
img = img.resize((30,30), Image.Resampling.LANCZOS)
img= ImageTk.PhotoImage(img)

label_imagem = Label(frame_cima,image=img,bg=White,anchor='nw',relief='flat')
label_imagem.place(x=5,y=13)

label_nome = Label(frame_cima,text='GERADOR DE SENHAS',bg=White,font='Ivy 16 bold',fg=Light_Gray)
label_nome.place(x=45,y=16)

label_linha = Label(frame_cima,bg=Orange,width=295,height=1)
label_linha.place(x=0,y=55)


# -- Criação de Widgets de baixo

# -- Labels
label_senha = Label(frame_baixo, text='- - -', relief='solid', width=23, height=2, font='Ivy 11')
label_senha.place(x=10, y=15)

frase = Label(frame_baixo,text='Número total de caracteres na senha:',bg=White,font='Ivy 10 bold',fg=Light_Gray)
frase.place(x=0,y=58)

# -- Spinbox
maxcara=IntVar()
maxcara.set(8)
caracteres = Spinbox(frame_baixo,from_=0,to=20,textvariable=maxcara,width=5)
caracteres.place(x=10,y=82,anchor=NW)

# Escolhas -- 
check1=BooleanVar()
check1.set(False)
escolha1 = Checkbutton(frame_baixo,text='  ABC Maiúsculas',bg=White,font='Ivy 10 bold',onvalue=True,offvalue=False,variable=check1)
escolha1.place(x=10,y=105)

check2=BooleanVar()
check2.set(False)
escolha2 = Checkbutton(frame_baixo,text='  ABC Minúsuculas',bg=White,font='Ivy 10 bold',onvalue=True,offvalue=False,variable=check2)
escolha2.place(x=10,y=130)

check3=BooleanVar()
check3.set(False)
escolha3 = Checkbutton(frame_baixo,text='  $%* Símbolos',bg=White,font='Ivy 10 bold',onvalue=True,offvalue=False,variable=check3)
escolha3.place(x=10,y=160)

check4=BooleanVar()
check4.set(False)
escolha4 = Checkbutton(frame_baixo,text='  123 Números',bg=White,font='Ivy 10 bold',onvalue=True,offvalue=False,variable=check4)
escolha4.place(x=10,y=190)

# -- Botões
gerar_senha = Button(frame_baixo,text='Gerar Senha',width=28,height=1,bg=Orange,font='Ivy 12 bold',command=GerarSenha)
gerar_senha.place(x=2,y=250)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()
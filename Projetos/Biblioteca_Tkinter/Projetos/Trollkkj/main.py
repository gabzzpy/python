from tkinter import *
from random import randint
from PIL import Image,ImageTk

# Cores
Black = '#000000'
White = '#FFFFFF'
Red = '#FF0000'
Green = '#00FF00'
Blue = '#0000FF'
Light_Gray = '#464f6b'
Yellow = '#FFFF00'
Gray = '#a8b1bf'
Orange = '#d17702'
Purple = '#800080'

# -- Principal
janela = Tk()
janela.title('Vc é?')
janela.config(bg=White)
janela.geometry('460x600')
janela.resizable(False,False)
janela.iconphoto(False,PhotoImage(file='Projetos\Trollkkj\Sus2.png'))

# -- Carregar Imagem
imagem = Image.open('Projetos\Trollkkj\Sus.png')
imagem = imagem.resize((600,260), Image.Resampling.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

# -- Funções
contador = 0
def Nao():
    global contador
    contador += 1
    x = randint(100,400)
    y = randint(100,550)
    nao.place(x=x,y=y)
    
    if contador >= 8:
        nao.place(x=-100,y=-100)

def Sim():
    # Tirando coisas do local
    sim.place(x=-100,y=-100)
    nao.place(x=-100,y=-100)
    img.place(x=-100,y=-100)

    # KKKKKKKKKKKKKKKKKKKKKKKK
    Prgt['text'] = 'TU É GAY MANO?????\nTU É GAY MANO?????\nTU É GAY MANO?????\nTU É GAY MANO?????\nTU É GAY MANO?????\nTU É GAY MANO?????'
    Prgt['font'] = 'Ivy 32 bold'
    Prgt.place(x=0,y=200)


# -- Labels
Prgt = Label(text='Mano, por acaso você tem algum...\n traço de homossexualidade? ',bg=White,fg=Black,font='Ivy 16 bold')
Prgt.place(x=50,y=280)

img = Label(image=imagem)
img.place(x=-6,y=10)

# -- Botões
sim = Button(text='Sim',fg=White,bg=Green,font='Ivy 20 bold',command=Sim)
sim.place(x=90,y=400)

nao = Button(text='Não',fg=White,bg=Red,font='Ivy 20 bold',command=Nao)
nao.place(x=300,y=400)


janela.mainloop()
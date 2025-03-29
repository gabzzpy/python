from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
import requests
import json


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

# Funções
def Converter():
    
    # -- Variáveis
    valor = float(entrada_valor.get())
    de = combo1.get()
    para = combo2.get()

    # -- Requests
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{de}')
    dados=json.loads(response.text)
    valores = dados['rates']

    # -- Resultado
    valor_convertido = valor * valores[f'{para}']    
    resultado['text'] = f'{para} {valor_convertido:.2f}' # valor_convertido = str(valor_convertido).replace('.',',')


# -- Base --
janela = Tk()
janela.title('Conversor de Moedas')
janela.geometry('300x320')
janela.config(bg=White)
janela.iconphoto(False,PhotoImage(file='Projetos\ConversorDeMoedas\iconlogo.png'))
janela.resizable(False,False)

# -- Divisão de Frames --
frame_cima = Frame(bg=Light_Gray,width=320,height=50)
frame_cima.place(x=0,y=0)

frame_baixo = Frame(bg=White,width=320,height=270)
frame_baixo.place(x=0,y=50)

# -- Trabalhando no Frame de Cima --

nome = Label(frame_cima,text=' Conversor de Moedas ',bg=Light_Gray,fg=White,font='Ivy 17 bold')
nome.place(x=37,y=10)

# Criando Imagem
img = Image.open('Projetos\ConversorDeMoedas\iconlogo.png')
img = img.resize((30,30), Image.Resampling.LANCZOS)
img= ImageTk.PhotoImage(img)

imagem = Label(frame_cima,image=img,background=Light_Gray)
imagem.place(x=7,y=10)

# -- Trabalhando no Frame de Baixo --

resultado = Label(frame_baixo,width=18,height=2,text='- - -',relief='solid',font='Ivy 14 bold')
resultado.place(x=42,y=10)

de = Label(text='De:',bg=White,font='Ivy 9 bold',fg=Black)
de.place(x=70,y=120)

para = Label(text='Para:',bg=White,font='Ivy 9 bold',fg=Black)
para.place(x=200,y=120)

combo1 = Combobox(frame_baixo,width=5,font='Ivy 9 bold')
combo1['values'] = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "BRL", "AOA"]

combo1.place(x=58,y=110)

combo2 = Combobox(frame_baixo,width=5,font='Ivy 9 bold')
combo2['values'] = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "BRL", "AOA"]
combo2.place(x=196,y=110)

entrada_valor = Entry(frame_baixo,width=15,font='Ivy 15 bold',relief='solid')
entrada_valor.place(x=65,y=160)

converter=Button(text='Converter',fg=White,bg=Light_Gray,width=15,height=2,font='Ivy 13 bold',relief='sunken',overrelief='solid',command=Converter)
converter.place(x=72,y=260)


janela.mainloop()
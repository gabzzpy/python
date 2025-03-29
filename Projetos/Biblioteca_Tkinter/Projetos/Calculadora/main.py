from tkinter import *

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

# -- Funções e Variáveis --
resultado =''
def EntrarValores(parametro):
    global resultado
    if 'Indefinido' in resultado:
        resultado=''

    if parametro == 'Apagar':
        resultado = ''
    else:
        if parametro == '=':  # expressao = re.sub(r'\b0+(\d)', r'\1', resultado)
            
            # if resultado vazio com aperto no '=', nothing
            if '/0' in resultado:
                resultado = 'Indefinido'
            else:
                try:
                    resultado = eval(resultado)
                except:
                    while True:
                        lista_teste = []
                        for c in resultado:
                            lista_teste.append(c)
                        lista_teste.pop(resultado.find('0')) # if antes do resultado.find('0') vier com um número, diferente de 0. nao executa esse pop, passa para outro, else, executa normal
                        try:
                            resultado = ''.join(lista_teste) 
                            resultado = eval(resultado)
                        except:
                            pass
                        else:
                            break
        else:
            resultado = resultado + parametro 
    mostrar['text'] = resultado
    resultado = str(resultado)

# -- Base --
janela = Tk()
janela.title('Calculadora')
janela.geometry('280x340')
janela.resizable(False,False)
janela.iconphoto(False,PhotoImage(file='Projetos\Calculadora\images.png'))

# -- Divisão de Frames --
frame_cima = Frame(bg=Light_Gray,width=280,height=80)
frame_cima.place(x=0,y=0)

frame_baixo = Frame(bg=Black,width=280,height=270)
frame_baixo.place(x=0,y=80)

# -- Label
mostrar = Label(frame_cima,fg=Orange,text='',bg=Light_Gray,font='Ivy 20',width=17,height=2,anchor=E,justify=RIGHT)
mostrar.place(x=0,y=8)

# -- Botões --

# -- Row 0
BOTAO_APAGAR = Button(frame_baixo,text='C',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=13,command=lambda:EntrarValores('Apagar'))
BOTAO_APAGAR.place(x=0,y=0)

BOTAO_PORCENTAGEM = Button(frame_baixo,text='%',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('%'))
BOTAO_PORCENTAGEM.grid(row=0,column=2)

BOTAO_DIVI = Button(frame_baixo,text='/',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('/'))
BOTAO_DIVI.grid(row=0,column=3)

# -- Row 1 
BOTAO_7 = Button(frame_baixo,text='7',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('7'))
BOTAO_7.grid(row=1,column=0)

BOTAO_8 = Button(frame_baixo,text='8',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('8'))
BOTAO_8.grid(row=1,column=1)

BOTAO_9 = Button(frame_baixo,text='9',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('9'))
BOTAO_9.grid(row=1,column=2)

BOTAO_MULTI = Button(frame_baixo,text='*',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('*'))
BOTAO_MULTI.grid(row=1,column=3)

# -- Row 2
BOTAO_4 = Button(frame_baixo,text='4',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('4'))
BOTAO_4.grid(row=2,column=0)

BOTAO_5 = Button(frame_baixo,text='5',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('5'))
BOTAO_5.grid(row=2,column=1)

BOTAO_6 = Button(frame_baixo,text='6',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('6'))
BOTAO_6.grid(row=2,column=2)

BOTAO_MENOS = Button(frame_baixo,text='-',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('-'))
BOTAO_MENOS.grid(row=2,column=3)

# -- Row 3
BOTAO_1 = Button(frame_baixo,text='1',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('1'))
BOTAO_1.grid(row=3,column=0)

BOTAO_2 = Button(frame_baixo,text='2',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('2'))
BOTAO_2.grid(row=3,column=1)

BOTAO_3 = Button(frame_baixo,text='3',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('3'))
BOTAO_3.grid(row=3,column=2)

BOTAO_MAIS = Button(frame_baixo,text='+',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('+'))
BOTAO_MAIS.grid(row=3,column=3)

# -- Row 4
BOTAO_0 = Button(frame_baixo,text='0',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('0'))
BOTAO_0.grid(row=4,column=1)

BOTAO_VIRGULA = Button(frame_baixo,text='.',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=6,command=lambda:EntrarValores('.'))
BOTAO_VIRGULA.grid(row=4,column=0)

BOTAO_IGUAL = Button(frame_baixo,text='=',relief='raised',bg=Gray,fg=Black,font='Ivy 13 bold',height=2,width=13,command=lambda:EntrarValores('='))
BOTAO_IGUAL.place(x=140,y=208)

janela.mainloop()
from tkinter import *


#ColorPicker
Black='#000000' # preta
branco = "#ffffff"
cinza = '#63606e'

contador = 1

def Executador():
    # pego a variaveis contador 
    global contador
    if contador %2 == 0:
        label_1['text']= 'Número par' # Substitui o texto do label
        label_1['fg'] = cinza
        botao_1['text'] = contador
    elif contador%2 !=0:
        label_1['text']= f'Número Impar'
        label_1['fg'] = Black
        botao_1['text'] = contador

    contador +=1


janela = Tk() #Cria a janela
janela.title('Hello World!') #mdua titulo
janela.geometry('640x480') #muda o tamanho de inicio
janela.config(bg=branco) # muda as configs, bg muda a cor do backgroud
janela.iconphoto(False, PhotoImage(file='loucura.png')) #Muda a Foto do icone // False para tirar a antiga

# Não posso mudar a altura nem largura por meio manual, apenas por cod
janela.resizable(width=False, height=False) 

label_1 = Label(janela,width=15,height=2,text='Nothing Here',font='Arial 15',fg= '#6e5000',bg=branco)
label_1.place(x= 40, y=45)

botao_1=Button(janela,command=Executador,width=15,height=2,text='Clique nesse botão',fg=Black,bg=cinza,relief='flat')
botao_1.place(x=200,y=50)


janela.mainloop()
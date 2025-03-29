from tkinter.ttk import *
from tkinter import *

# Cores
Preto = '#000000'
Branco = '#FFFFFF'
Vermelho = '#FF0000'
Verde = '#00FF00'
Azul = '#0000FF'
Amarelo = '#FFFF00'
Cinza = '#808080'
Laranja = '#FFA500'
Roxo = '#800080'

def Obter():
    resultado = combo.get()
    labelresul=Label(text=resultado,bg=Branco)
    labelresul.grid(row=3,column=0,padx=10,pady=15)
    

Janela = Tk()
Janela.title('Combobox')
Janela.geometry('300x250')
Janela.config(bg=Branco)


# -- Botões, Labels e combobox
nome = Label(Janela, width=15,height=2,text='Faça a sua escolha',font='Arial 10',anchor='w',bg=Branco)
nome.grid(row=0,column=0,padx=5,pady=5)

combo = Combobox(Janela)
combo['values'] = (1,2,3,4,'João','Jorge',1.5) # Pode ser lista ou tupla, pode ser mistura, seja int, float, str
combo.current(1) # O valor '2' fica como valor inicial

combo.grid(row=1,column=0,padx=5,pady=5)


botao = Button(command=Obter,text='Ver resposta',relief='raised',bg=Branco,fg=Preto)
botao.grid(row=2,column=0,padx=5,pady=20)



Janela.mainloop()
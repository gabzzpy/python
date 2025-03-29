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



Janela = Tk()
Janela.title('Combobox')
Janela.geometry('300x250')
Janela.config(bg=Branco)

def Obter():
    resultado = selecionado_1.get()
    label_1 = Label(Janela, width=15,height=2,text=resultado,font='Arial 10',anchor='w',bg=Branco)
    label_1.grid(row=0,column=0,padx=5,pady=5)

selecionado_1 = IntVar()
'''selecionado2 = BooleanVar()
selecionado3 = StringVar()'''



# Também é possível colocar command no radiobutton, mas nesse exemplo eu nao coloquei
radio = Radiobutton(width=10,text='Primeiro',value=1,variable=selecionado_1,anchor='w') 
radio.place(x=100,y=100)

radio_2= Radiobutton(width=10,text='Segundo',value=2,variable=selecionado_1,anchor='w')
radio_2.place(x=100,y=120)

radio_3 = Radiobutton(width=10,text='Terceiro',value=3,variable=selecionado_1,anchor='w')
radio_3.place(x=100,y=140)

# Tem que ter o variable, para ser possivel obter o resultado, e isso vai para cada um dos buttons, dependendo se é int, boolean ou str


botao = Button(text='Ver resposta',relief='raised',bg=Branco,fg=Preto,command=Obter)
botao.place(x=30,y=200)


Janela.mainloop()
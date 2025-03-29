from tkinter import *

branco = "#ffffff"
cinza = '#63606e'
black = '#000000'

janela = Tk()
janela.title('Aula03')
janela.geometry('640x480')
janela.config(bg=branco)
janela.resizable(False,False)

#label_4 = Label(width=10,height=2,text='Loucura',fg=black, bg=cinza)
#label_4.grid(row=2,column=2) row = linha, column = coluna. Ele faz por coluna e linha

label_1 = Label(width=10,height=2,text='Teste',fg=black, bg=cinza)
label_1.place(x=0,y=0) #Coordenadas tipo no pygame

label_2 = Label(width=10,height=2,text='Loucura',fg=black, bg=cinza)
label_2.place(x=0,y=30) #Coordenadas tipo no pygame

label_3 = Label(width=12,height=2,text='Vagabundagem',fg=black, bg=cinza)
label_3.pack(side=LEFT) #.pack() sem atributo =  centralizado, se forem 2 sempre vai ser um ao lado ou embaixo do outro


janela.mainloop()
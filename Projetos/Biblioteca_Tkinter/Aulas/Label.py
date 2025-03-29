from tkinter import *

branco = "#ffffff"
cinza = '#63606e'

janela = Tk()
janela.title('Olá Mundo!')
janela.geometry('640x480')
janela.config(bg=cinza)
janela.resizable(False,False)
 
# fg = foreground - fontcolor. bg = background
label_nome = Label(janela,width=10,height=2,text='Nome : ',font='Arial 15', fg= '#6e5000',bg=branco) 
label_nome.grid(row=0, column=0, pady=10) #pady, padx = cada um corresponde a uma distancia dada entre os labels, y para cima e baixo e x para esquerda e direita

label_pais = Label(janela,width=10,height=2,text='País : ',font='Arial 15 bold',fg= '#6e5000',bg=branco)
label_pais.grid(row=2, column=0, pady=10)

label_idade = Label(janela,width=10,height=2,text='Idade : ',font='Arial 15',fg= '#6e5000',bg=branco)
label_idade.grid(row=1, column=0, pady=10)

janela.mainloop()
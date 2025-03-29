from tkinter import *

# Cores
branco = "#ffffff"
cinza = '#63606e'
black = '#000000'

# Janela
janela = Tk()
janela.title('Entry')
janela.geometry('640x480')
janela.resizable(False,False) 

# Funções
def obter_info(): #Obtém as informações das funções
    nome = Entry_N.get()
    idade = Entry_I.get()
    pais = Entry_P.get()
    Label_1['text'] = nome
    Label_3['text'] = idade
    Label_2['text'] = pais

    Entry_N.delete(0,END)
    Entry_I.delete(0,END)
    Entry_P.delete(0,END)



# Entrada
Label_N = Label(janela, height=2,width=8,fg=black,text='Nome: ',anchor=W) #anchor caso queiramos mudar a posição das letras, tipo colocar a palavra pora a esquerda, ao inves do centro
Label_N.grid(row=0,column=0, padx= 10, pady= 8) #sticky caso queiramos mudar a posição das letras, tipo colocar a palavra pora a esquerda, ao inves do centro
Entry_N = Entry(janela,width=10,font='Arial 10')
Entry_N.grid(row=0,column=1,padx=10,pady=8)

Label_P = Label(janela, height=2,width=8,fg=black,text='País: ',anchor=W)
Label_P.grid(row=1,column=0, padx= 10, pady= 8)
Entry_P = Entry(janela,width=10,font='Arial 10') #PARA DESATIVAR UMA ENTRY COLOQUE stare='disabled'
Entry_P.grid(row=1,column=1,padx=10,pady=8) 

Label_I = Label(janela, height=2,width=8,fg=black,text='Idade: ',anchor=W)
Label_I.grid(row=2,column=0,padx=10,pady=8)
Entry_I = Entry(janela,width=10,font='Arial 10')
Entry_I.grid(row=2,column=1,padx=10,pady=8)

# Respostas
Label_1 = Label(janela, height=2,width=8,fg=black,text='',anchor=W,font='Arial 10')
Label_1.grid(row=0,column=2,padx=10,pady=8)

Label_2 = Label(janela, height=2,width=8,fg=black,text='',anchor=W,font='Arial 10')
Label_2.grid(row=1,column=2,padx=10,pady=8)

Label_3 = Label(janela, height=2,width=8,fg=black,text='',anchor=W,font='Arial 10')
Label_3.grid(row=2,column=2,padx=10,pady=8)

# Button
Enviar=Button(width=8,height=2,text='Ver Info',command=obter_info,font='Arial 10')
Enviar.place(x=50,y=160)

janela.mainloop()
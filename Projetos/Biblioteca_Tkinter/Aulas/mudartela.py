'''Feito pelo chat gpt, para uso de explicativo'''
from tkinter import *

# Função para mudar de tela
def mostrar_tela(frame_para_mostrar):
    # Esconde todos os frames
    tela1.place_forget() #Oculta um Widget, mas ele ainda existe na memória. Ou seja, coloco para tela1 ser oculta/esquecer seu local
    tela2.place_forget()
    # Mostra o frame desejado
    frame_para_mostrar.place(x=0, y=0, width=300, height=200) #Coloco a tela 1 de volta para um local

# Janela principal
janela = Tk()
janela.geometry('300x200')

# Criação das telas (frames)
tela1 = Frame(janela, bg='lightblue')
tela2 = Frame(janela, bg='lightgreen')

# Widgets da tela 1
Label(tela1, text="Esta é a tela 1", font=('Arial', 18), bg='lightblue').place(x=60, y=50)
Button(tela1, text="Ir para a tela 2", command=lambda: mostrar_tela(tela2)).place(x=100, y=100)

# Widgets da tela 2
Label(tela2, text="Esta é a tela 2", font=('Arial', 18), bg='lightgreen').place(x=60, y=50)
Button(tela2, text="Voltar para a tela 1", command=lambda: mostrar_tela(tela1)).place(x=90, y=100)

# Mostrar a tela inicial
mostrar_tela(tela1)

# Executar o loop da janela
janela.mainloop()




# Outro Método

'''from tkinter import *

def mostrar_tela1():
    # Esconde tela 2 e mostra tela 1
    tela2.place_forget()
    tela1.place(x=0, y=0, width=300, height=300)

def mostrar_tela2():
    # Esconde tela 1 e mostra tela 2
    tela1.place_forget()
    tela2.place(x=0, y=0, width=300, height=300)

# Criação da janela principal
janela = Tk()
janela.geometry("300x300")
janela.title("Troca de Telas com .place_forget()")

# Criação da primeira tela
tela1 = Frame(janela, bg='lightblue')
label1 = Label(tela1, text="Esta é a Tela 1", font=('Arial', 16), bg='lightblue')
label1.place(x=80, y=120)
botao_tela2 = Button(tela1, text="Ir para Tela 2", command=mostrar_tela2)
botao_tela2.place(x=100, y=200)

# Criação da segunda tela
tela2 = Frame(janela, bg='lightgreen')
label2 = Label(tela2, text="Esta é a Tela 2", font=('Arial', 16), bg='lightgreen')
label2.place(x=80, y=120)
botao_tela1 = Button(tela2, text="Ir para Tela 1", command=mostrar_tela1)
botao_tela1.place(x=100, y=200)

# Mostrar a primeira tela inicialmente
mostrar_tela1()

janela.mainloop()'''

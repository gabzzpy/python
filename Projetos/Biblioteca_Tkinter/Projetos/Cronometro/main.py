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

# -- Váriaveis
contador=0
reiniciar = rodar = False

# - Funções
def Iniciar():
    # Váriaveis para início
    global contador
    global reiniciar
    global rodar
    
    # Pausar
    if reiniciar == True:
        contador = 0
        rodar = False
        
        #Zerando Crômetro
        segundo = hora = minuto = ''
        texto = '00:00:00'
        Label_tempo['text']=texto
        

    # Dar Inicio ao cronometro, esse if permite podermos pausá-lo
    if rodar == True:
        segundo = hora = minuto = ''
        
        #Salvando o contador para depois
        save_contador = contador 

        # If's para contar o tempo
        hora='0'+str(contador//3600)
        contador = contador - ((contador//3600) * 3600)
        minuto ='0'+str(contador//60)
        contador = contador - ((contador//60) * 60)
        segundo = '0'+str(contador)

        # Reset do contador, pois subtraimos ele nos if's
        contador = save_contador

        # Atualizando a tela
        texto = f'{hora[-2:]}:{minuto[-2:]}:{segundo[-2:]}'
        Label_tempo['text']=texto
        Label_tempo.after(1000,Iniciar)

        contador += 1

def Rodar():
    global rodar
    global reiniciar
    rodar = True
    reiniciar = False
    Botao_Iniciar['text'] = 'Iniciar'
    Iniciar()

def Pausar():
    global rodar
    rodar = False
    Botao_Iniciar['text'] = 'Voltar'

def Reiniciar():
    global reiniciar
    reiniciar = True


# -- Base

Janela = Tk()
Janela.title('Crônometro')
Janela.geometry('300x180')
Janela.resizable(False,False)
Janela.configure(bg=Preto)
Janela.iconphoto(False,PhotoImage(file='Projetos\Cronometro\Cronometro.png'))

# -- Criando Labels

Label_nome=Label(text='Crônometro',fg=Branco,bg=Preto,font='Arial 10')
Label_nome.place(x=20,y=10)

Label_tempo = Label(text='00:00:00',bg=Preto,fg=Verde,font='Times 50 bold')
Label_tempo.place(x=20,y=30)

# -- Criando Botôes

Botao_Iniciar = Button(text='Iniciar',bg=Preto,fg=Branco,font='Arial 15 bold',command=Rodar)
Botao_Iniciar.place(x=25,y=120)

Botao_Pausar = Button(text='Pausar',bg=Preto,fg=Branco,font='Arial 15 bold',command=Pausar)
Botao_Pausar.place(x=95,y=120)

Botao_Reiniciar = Button(text='Reinicar',bg=Preto,fg=Branco,font='Arial, 15 bold',command=Reiniciar)
Botao_Reiniciar.place(x=175,y=120)


Janela.mainloop()


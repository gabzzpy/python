from tkinter import *


# Cores
Black = '#000000'
White = '#FFFFFF'
Red = '#FF0000'
Green = '#00FF00'
Blue = '#0000FF'
Yellow = '#FFFF00'
Gray = '#808080'
Orange = '#FFA500'
Purple = '#800080'

janela = Tk()
janela.title("Frame")
janela.geometry('400x400')
janela.resizable(False,False)
janela.config(bg=White)

# Criação de Widgets

frame=Frame(width=200,height=100,bg=Blue)
frame.grid(row=0,column=0,pady=2)

frame1=Frame(width=200,height=100,bg=Green)
frame1.grid(row=1,column=0,pady=2)

frame2=Frame(width=200,height=100,bg=Red)
frame2.grid(row=0,column=1,padx=2,pady=2)

frame3=Frame(width=200,height=100,bg=Yellow)
frame3.grid(row=1,column=1,padx=2,pady=2)

janela.mainloop()
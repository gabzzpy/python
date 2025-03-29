from bancodedados import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

'''
Falta Criar:
Colocar Imagens para fins estéticos 
Fazer um jeito de reescrever os ID's quando apagar um, no momento quando se apaga o ID 2 por exemplo, continua seguindo a ordem e nunca mais se tem algo com id dois

'''

# Colors
black = '#000000'
white = '#FFFFFF'
red = '#FF0000'
green = '#00FF00'
blue = '#0000FF'
light_Gray = '#464f6b'
light_Gray_dark = '#4c515e'
light_Blue = '#7c98c4'
light_Gray_Blue ='#7f89b0'
yellow = '#FFFF00'
gray = '#808080'
orange = '#d17702'
purple = '#800080'

# Window Configuration
window = Tk()
window.title('VirtualLibrary')
window.config(bg=white)
window.resizable(False,False)
window.geometry('780x480')
#window.iconphoto(False,PhotoImage(file='Projetos\Gerenciamento_de_livros\logo.png'))

style = ttk.Style(window)
style.theme_use('clam')

# Funções referentes a tela de Login
check_adm = False

# Função para logar numa conta já existente
def Login():
    global check_adm
    check_adm = False
    # Pega as inormações das entrys para lançar no banco de dados
    emailuser = Login_Entry_EmailUser.get()
    password = Login_Entry_Password.get()

    LOGIN = Login_FUNCTION(emailuser,password)

    # Verifica se as informações estão no banco de dados, se n estiverem, é mostrado uma mensagem de erro
    if LOGIN[0] == True:
        User_In_Moment['text'] = f'User:  {LOGIN[2]}'
        Login_Frame.place_forget()
            
        Left_App_Frame.place(x=0,y=70)
        RightDown_App_Frame.place(x=220,y=70)
        RightUp_App_Frame.place(x=0,y=0)

        if LOGIN[1] == 1: #Se ele for adm vai ter 1 e vai mostrar todos os botões
            check_adm = True
            pass
        else:
            NewBook.place_forget()
            NewUser.place_forget()
            BooksInReserve.place_forget()
            ShowUsers.place_forget()
            ShowBooks.place(x=22,y=10)
            ReserveBook.place(x=22,y=60)
            ReturnReservation.place(x=22,y=110)
            
    else:
        text = 'Wrong Informations'
        messagebox.showinfo('Error! ',text)

    CorrectIds('BOOKS')
    CorrectIds('USERS')
    
# Função para criar um novo usuário
def SignUp():
    # Pega as inormações das entrys para lançar no banco de dados
    user = Login_Entry_User.get()
    email = Login_Entry_EmailUser.get()
    password = Login_Entry_Password.get()

    check = SignUp_FUNCTION(user,email,password)
    if check == True:
        messagebox.showinfo('Sucess!','The user is cadastred')
        Change_Frame_Login()
    else:
        messagebox.showinfo('Error! ',check)

# Função para mostrar as informações na Entry password, ao invés de ficar em *
def Show_Infos():
    Login_Entry_Password.config(show='')
    Login_Button_Password.config(command=Show_Infos2)
    
def Show_Infos2():
    Login_Entry_Password.config(show='*')
    Login_Button_Password.config(command=Show_Infos)

#Função que muda para o frame de Sign Up
def Change_Frame_SignUp():
        # Mudanças pra tela de Cadastro
        Login_Label['text'] = 'SignUp'
        Login_Label.place(x=72,y=20)

        Login_Label_EmailUser['text'] = 'Email'
        Login_Label_EmailUser.place(x=20,y=75)
        Login_Label_Password.place(x=20,y=195)

        Login_Button.place_forget()
        Login_Button_Password.place(x=230,y=195)

        Login_Button_SingUp['font'] = 'Ivy 15 bold'
        Login_Button_SingUp.place(x=90,y=300)
        Login_Button_SingUp['command'] = SignUp

        Login_Entry_EmailUser.place(x=30,y=100)
        Login_Entry_Password.place(x=30,y=220)

        Login_Entry_User.place(x=30,y=160)
        Login_Label_User.place(x=20,y=135)
        Login_Button_Return.place(x=104,y=345)

        # Apaga oq estiver Escrito na Entry
        Login_Entry_EmailUser.delete(0,END)
        Login_Entry_Password.delete(0,END)
        Login_Entry_User.delete(0,END)
# Função que muda para o frame de Login, caso o usuário tenha ido para tela de SignUp
def Change_Frame_Login():
    # Mudanças para tela de Login Novamente
    Login_Label['text'] = 'LOGIN'
    Login_Label.place(x=83,y=20)

    Login_Label_EmailUser['text'] = 'Email or User'
    Login_Label_EmailUser.place(x=20,y=75)
    Login_Label_Password.place(x=20,y=175)

    Login_Button.place(x=90,y=300)
    Login_Button_Password.place(x=230,y=175)


    Login_Button_SingUp['font'] = 'Ivy 8 bold'
    Login_Button_SingUp.place(x=121,y=270)
    Login_Button_SingUp['command'] = Change_Frame_SignUp

    Login_Entry_EmailUser.place(x=30,y=100)
    Login_Entry_Password.place(x=30,y=200)

    Login_Entry_User.place_forget()
    Login_Label_User.place_forget()
    Login_Button_Return.place_forget()

    # Apaga oq estiver Escrito na Entry
    Login_Entry_EmailUser.delete(0,END)
    Login_Entry_Password.delete(0,END)
    Login_Entry_User.delete(0,END)


#  Funções para os botões

# Funções primeiro botão (registrar usuário)
def CHANGE_REGISTERUSER(edit='normal'):
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    clear_all()

    if edit == 'normal':
        DescriptionName_Label.config(text='Insert new user:')
        Save_Info.config(command=REGISTERUSER,text='Save')
        Info3_Label.place(x=15,y=170)
        Info3_Entry.place(x=300,y=170)

        Info1_Label.place(x=15,y=10)
        Info1_Entry.place(x=300,y=10)

        Info2_Label.place(x=15,y=90)
        Info2_Entry.place(x=300,y=90)

        Info3_Label.config(text="Insert user's password: ")
        Info1_Label.config(text="Insert user's username: ")
        Info2_Label.config(text="Insert user's email: ")

        Save_Info.place(x=205,y=250)

    elif edit == 'edit':
        Save_Info.config(command=lambda:EDIT('users'),text='Update')
        DescriptionName_Label.config(text=f'Edit users table:')
        Info3_Label.place(x=15,y=120)
        Info3_Entry.place(x=300,y=120)

        Info1_Label.place(x=15,y=0)
        Info1_Entry.place(x=300,y=0)

        Info2_Label.place(x=15,y=60)
        Info2_Entry.place(x=300,y=60)

        Info4_Label.place(x=15,y=180)
        Info4_Entry.place(x=300,y=180)

        Info6_Label.place(x=15,y=240)
        Info6_Entry.place(x=300,y=240)

        Info3_Label.config(text="Insert new user's email: ")
        Info1_Label.config(text="Insert user's ID: ")
        Info2_Label.config(text="Insert new user's username: ")
        Info4_Label.config(text="Insert new user's password:")
        Info6_Label.config(text="Insert new user's ADM \n(0 or 1):")
        Save_Info.place(x=205,y=280)

        
    DescriptionName_Label.place(x=180,y=10)

def REGISTERUSER():
    user = Info1_Entry.get()
    email = Info2_Entry.get()
    password = Info3_Entry.get()

    check = SignUp_FUNCTION(user,email,password)
    if check == True:
        messagebox.showinfo('Sucess!','The user is cadastred')
        clear_all()
        CHANGE_REGISTERUSER()
    else:
        messagebox.showinfo('Error! ',check)


# Funções segundo botão (registrar livro)
def CHANGE_REGISTERBOOK(edit='normal'):
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    clear_all()

    if edit == 'normal':
        DescriptionName_Label.config(text='Insert new book:')
        Save_Info.config(command=REGISTERUSER,text='Save')
        Info3_Label.place(x=15,y=120)
        Info3_Label['text'] = "Insert book's publisher: "
        Info3_Entry.place(x=300,y=120)

        Info1_Label.place(x=15,y=0)
        Info1_Label.config(text="Insert book's name: ")
        Info1_Entry.place(x=300,y=0)

        Info2_Label.place(x=15,y=60)
        Info2_Label.config(text="Insert book's author: ")
        Info2_Entry.place(x=300,y=60)

        Info4_Label.place(x=15,y=180)
        Info4_Label.config(text="Insert book's year: ")
        Info4_Entry.place(x=300,y=180)

        Save_Info.place(x=205,y=250)
        Save_Info.config(command=REGISTERBOOK)
    elif edit == 'edit':
        Save_Info.config(command=lambda:EDIT('books'),text='Update')
        DescriptionName_Label.config(text=f'Edit books table:')
        
        Info3_Label.place(x=15,y=120)
        Info3_Entry.place(x=300,y=120)

        Info1_Label.place(x=15,y=0)
        Info1_Entry.place(x=300,y=0)

        Info2_Label.place(x=15,y=60)
        Info2_Entry.place(x=300,y=60)

        Info4_Label.place(x=15,y=180)
        Info4_Entry.place(x=300,y=180)

        Info6_Label.place(x=15,y=240)
        Info6_Entry.place(x=300,y=240)

        Info3_Label.config(text="Insert new book's author: ")
        Info1_Label.config(text="Insert book's ID: ")
        Info2_Label.config(text="Insert new book's name: ")
        Info4_Label.config(text="Insert new book's publisher:")
        Info6_Label.config(text="Insert new book's year: ")
        Save_Info.place(x=205,y=280)

    DescriptionName_Label.place(x=180,y=10)

def REGISTERBOOK():
    # Pega as informações para registrar o livro
    name = Info1_Entry.get()
    author = Info2_Entry.get()
    publisher = Info3_Entry.get()
    year = Info4_Entry.get()
    # Faz a verificação se o resultado foi True
    check = insert_table_books(name,author,publisher,year)

    if check == True:
        messagebox.showinfo('Sucess','The book is registered')
        clear_all()
        CHANGE_REGISTERBOOK()
    else:
        messagebox.showinfo('Error! ',check)

        
# Funções terceiro botão (mostrar livros)
def CHANGE_SHOWBOOKS():
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    clear_all()

    DescriptionName_Label.config(text='Books: ')
    DescriptionName_Label.place(x=250,y=10)

    # Verifica se o usuário tem adm, se sim mostra o botão de deletar um livro

    if check_adm:
        Remove_Info.config(command=lambda:CHANGE_REMOVE('BOOKS'),text='Delete Book')
        Remove_Info.place(x=30,y=5)
        Correct_Info.config(text='Sort Ids',command=lambda:CHANGE_CORRECTIDS('BOOKS'))
        Correct_Info.place(x=400,y=15)

    check = get_lines('BOOKS')
    if check[0]:
        rows = check[1]
    else:
        messagebox.showinfo('Error!',check[1])

    tree.place(x=0,y=0)
    column = ("ID","Name","Author","Publisher","Year","Reserved?","Reserve Date")
    tree.config(columns=column)

    list_headings = [f'tree.heading("{value}",text="{value}")' for value in column ]
    for value in list_headings:
        eval(value)
    
    list_columns =['tree.column("Name",width=178)','tree.column("ID",width=20)','tree.column("Author",width=60)','tree.column("Publisher",width=90)',
    'tree.column("Year",width=40)','tree.column("Reserved?",width=80)','tree.column("Reserve Date",width=90)',]
    for value in list_columns:
        eval(value)

    for row in rows:
        row_updated =[]
        counter =0
        for value in row:
            counter +=1
            if value == 1 and counter ==6:
                value = 'Yes'
            elif value == 0 and counter ==6:
                value = 'No'
            elif value == None and counter ==7 :
                value = "Don't reserved"
            row_updated.append(value) 

        tree.insert("",END,values=row_updated)

# Funções quarto botão (mostrar usuarios)
def CHANGE_SHOWUSERS():
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    clear_all()
    Correct_Info.config(text='Sort Ids',command=lambda:CHANGE_CORRECTIDS('USERS'))
    Correct_Info.place(x=400,y=15) 

    DescriptionName_Label.config(text='Users: ')
    DescriptionName_Label.place(x=250,y=10)

    Save_Info

    Remove_Info.config(command=lambda:CHANGE_REMOVE('USERS'),text='Remove User')
    Remove_Info.place(x=30,y=5)

    check = get_lines('USERS')
    if check[0]:
        rows = check[1]
    else:
        messagebox.showinfo('Error!',check[1])

    tree.place(x=0,y=0)
    column=("ID","Users","Email","Password","Adm?")
    tree.config(columns=column)

    column=("ID","Users","Email","Password","Adm?")
    list_headings = [f'tree.heading("{value}",text="{value}")' for value in column ]
    for value in list_headings:
        eval(value)

    list_columns =['tree.column("Users",width=178)','tree.column("ID",width=20)','tree.column("Email",width=178)','tree.column("Password",width=142)',
    'tree.column("Adm?",width=40)']
    for value in list_columns:
        eval(value)

    for row in rows:
        row_updated = []
        counter = 0
        for value in row:
            counter+=1
            if value == 1 and counter == 5:
                value = 'Yes'
            elif value == 0 and counter == 5:
                value = 'No'
            row_updated.append(value)
        tree.insert("",END,values=row_updated)

# Função de deletar algo por ID (está presente no botão 3º e 4º botão)
def CHANGE_REMOVE(this):
    Info5_Label.config(text=f'Insert the ID of the table {this} to delete:')
    Info5_Label.place(x=30,y=45)
    Info5_Entry.config()
    Info5_Entry.place(x=30,y=60)

    Remove_Info.config(command=lambda:DELETE(this))

def DELETE(this):
    id = Info5_Entry.get()

    try:
        check = delete(this,id)
    except TypeError:
        messagebox.showinfo('Error!','Please fill the field')
    except Error as e:
        print(e)
    else:
        if check[0]:
            this1 = [this[count] for count in range(0,len(this)) if count != len(this)-1]
            this = ''.join(this1)
            messagebox.showinfo('Sucess!',f'The {this} is removed!\nPlease Update the page')
        else:
            messagebox.showinfo('Error!',check[1])


# Funções quinto botão (reservar livros e atualizar data de entrega)
def CHANGE_RESERVEBOOK(check=False):
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    clear_all()

    DescriptionName_Label.place(x=180,y=10)
    DescriptionName_Label['text'] = 'Reserve a book:'

    Info3_Label.place(x=15,y=120)
    Info3_Label['text'] = "Insert book's publisher: "
    Info3_Entry.place(x=300,y=120)

    Info1_Label.place(x=15,y=0)
    Info1_Label.config(text="Insert book's id: ")
    Info1_Entry.place(x=300,y=0)

    Info2_Label.place(x=15,y=60)
    Info2_Label.config(text="Insert book's name: ")
    Info2_Entry.place(x=300,y=60)

    Info4_Label.place(x=15,y=180)
    Info4_Label.config(text="Insert book's date:")
    Info4_Entry.place(x=300,y=180)

    if check:
        Info4_Label.config(text="Insert new book's date: ")
        messagebox.showinfo('Notification','To change date, put the informations')
        Change_Info.config(command=lambda:RESERVEBOOK('Succesful there serve date has been updated!'))

    else:
        messagebox.showinfo('Observation','Please put the date in this format (year-month-day) // (xxxx-xx-xx)')
        Change_Info.config(text='Change \nreserve date',command=lambda:CHANGE_RESERVEBOOK(True))

    Save_Info.place(x=205,y=250)
    Change_Info.place(x=405,y=240)
    Save_Info.config(command=RESERVEBOOK)

def RESERVEBOOK(changereservedate='Succesful the book is updated!',update='yes'):
    # Pega as informações para registrar o livro
    id = Info1_Entry.get()
    name = Info2_Entry.get()
    publisher = Info3_Entry.get()
    date = Info4_Entry.get()
    
    # Faz a verificação se o resultado foi True
    if update == 'no':
        check = reserve_a_book(id,name,publisher,date)
    elif update == 'yes':
        check = reserve_a_book(id,name,publisher,date,update='yes')


    if check == True:
        messagebox.showinfo('Sucess',changereservedate)
        clear_all()
        CHANGE_RESERVEBOOK()
    else:
        messagebox.showinfo('Error! ',check)

    
#Funções sexto botão (retornar livro reservado)
def CHANGE_DEVOLVEBOOK():
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    clear_all()

    DescriptionName_Label.place(x=180,y=10)
    DescriptionName_Label['text'] = 'Devolve a book:'

    Info3_Label.place(x=15,y=120)
    Info3_Label['text'] = "Insert book's publisher: "
    Info3_Entry.place(x=300,y=120)

    Info1_Label.place(x=15,y=0)
    Info1_Label.config(text="Insert book's id: ")
    Info1_Entry.place(x=300,y=0)

    Info2_Label.place(x=15,y=60)
    Info2_Label.config(text="Insert book's name: ")
    Info2_Entry.place(x=300,y=60)

    Save_Info.place(x=205,y=250)
    Save_Info.config(command=DEVOLVEBOOK)

def DEVOLVEBOOK(changereservedate='Succesful the book is updated!'):
   # Pega as informações para registrar o livro
    id = Info1_Entry.get()
    name = Info2_Entry.get()
    publisher = Info3_Entry.get()
    
    # Faz a verificação se o resultado foi True
    check = desreserve_a_book(id,name,publisher)

    if check == True:
        messagebox.showinfo('Sucess',changereservedate)
        clear_all()
        CHANGE_DEVOLVEBOOK()
    else:
        messagebox.showinfo('Error! ',check)


#Funções setimo botão (mostrar Editar Informações)
def CHANGE_EDIT():
    top_frame.place(x=0,y=0)
    down_frame.place(x=0,y=90)

    DescriptionName_Label.config(text='What table do you need to update?')
    DescriptionName_Label.place(x=120,y=10)

    clear_all()

    Save_Info.config(text='Books',command=lambda:CHANGE_REGISTERBOOK('edit'))
    Save_Info.place(x=100,y=50)
    Change_Info.config(text='Users',command=lambda:CHANGE_REGISTERUSER('edit'))
    Change_Info.place(x=360,y=50)


def EDIT(this):
    # Pega as informações para registrar o livro
    id = Info1_Entry.get()
    val1= Info2_Entry.get()
    val2 = Info3_Entry.get()
    val3 = Info4_Entry.get()
    val4 = Info6_Entry.get()
    
    # Faz a verificação se o resultado foi True
    check = edit(this,id,val1,val2,val3,val4)

    if check[0] == True:
        messagebox.showinfo('Sucess',check[1])
        clear_all()
        CHANGE_EDIT()
    else:
        messagebox.showinfo('Error! ',check)

# Função mais essencial do código
def clear_all():
    list =['Info4_Entry.delete(0,END)','Info2_Entry.delete(0,END)','Info1_Entry.delete(0,END)','Info3_Entry.delete(0,END)','Info6_Entry.delete(0,END)',
           'Info3_Label.place_forget()','Info3_Entry.place_forget()','Info1_Label.place_forget()','Info1_Entry.place_forget()','tree.place_forget()',
           'Info2_Label.place_forget()','Info2_Entry.place_forget()','Info4_Label.place_forget()','Info4_Entry.place_forget()','Save_Info.place_forget()',
           'Change_Info.place_forget()','Info5_Entry.place_forget()','Info5_Label.place_forget()','Remove_Info.place_forget()','Info6_Label.place_forget()',
           'Info6_Entry.place_forget()','Correct_Info.place_forget()']
    for value in list:
        eval(value)
    for value in tree.get_children():
        tree.delete(value)

def CHANGE_CORRECTIDS(local):
    CorrectIds(local)
    if local == 'USERS':
        CHANGE_SHOWUSERS()
    elif local == 'BOOKS':
        CHANGE_SHOWBOOKS()

# Função para carregar todas as imagens
#def Images(image): Não funciona por enquanto
    #img = Image.open(f'Projetos\Gerenciamento_de_livros\{image}')
    #img = img.resize((40, 40), Image.Resampling.LANCZOS)
    #img = ImageTk.PhotoImage(img)
    #return img

# -- Frames Creation

# Frames Division
Login_Frame = Frame(window,bg=black,width=290,height=400)
Login_Frame.place(x=245,y=40)

Left_App_Frame = Frame(window,bg=light_Gray,width=220,height=480)

RightUp_App_Frame = Frame(window,bg=light_Blue,width=780,height=70)

RightDown_App_Frame = Frame(window,bg=light_Gray_Blue,width=560,height=480)

# Frames Button

top_frame = Frame(RightDown_App_Frame,bg=white,width=560,height=90)

down_frame = Frame(RightDown_App_Frame,bg=white,width=560,height=390)


# -- Login Frame: Label,Buttons, Entrys
Login_Label = Label(Login_Frame,text='LOGIN',bg=black,fg=white,font='Ivy 30 bold')
Login_Label.place(x=83,y=20)
Login_Button = Button(Login_Frame,text='CONFIRM',bg=black,fg=white,font='Ivy 15 bold',command=Login)
Login_Button.place(x=90,y=300)
Login_Button_SingUp =Button(Login_Frame,text='Sing Up',bg=black,fg=white,font='Ivy 8 bold',command=Change_Frame_SignUp)
Login_Button_SingUp.place(x=121,y=270)

Login_Label_EmailUser = Label(Login_Frame,text='Email or User',bg=black,fg=white,font='Ivy 8 bold')
Login_Label_EmailUser.place(x=20,y=75)
Login_Entry_EmailUser = Entry(Login_Frame,width=25,font='Ivy 13')
Login_Entry_EmailUser.place(x=30,y=100)

Login_Label_Password = Label(Login_Frame,text='Password',bg=black,fg=white,font='Ivy 8 bold')
Login_Label_Password.place(x=20,y=175)
Login_Entry_Password = Entry(Login_Frame,width=25,font='Ivy 13',show='*')
Login_Entry_Password.place(x=30,y=200)
Login_Button_Password = Button(Login_Frame,text='Show',bg=black,fg=white,font='Ivy 6 bold',command=Show_Infos)
Login_Button_Password.place(x=230,y=175)

Login_Entry_User = Entry(Login_Frame,width=25,font='Ivy 13')

Login_Label_User = Label(Login_Frame,text='User',bg=black,fg=white,font='Ivy 8 bold')

Login_Button_Return =Button(Login_Frame,text='Return to Login',bg=black,fg=white,font='Ivy 6 bold',command=Change_Frame_Login)

# -- Left App Frame: Buttons and Label
NewUser = Button(Left_App_Frame,text='Register a User',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_REGISTERUSER)
NewUser.place(x=22,y=10)

NewBook = Button(Left_App_Frame,text='Register a Book',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_REGISTERBOOK)
NewBook.place(x=22,y=60)

ShowBooks = Button(Left_App_Frame,text='Show Books',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_SHOWBOOKS)
ShowBooks.place(x=22,y=110)

ShowUsers = Button(Left_App_Frame,text='Show Users',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_SHOWUSERS)
ShowUsers.place(x=22,y=160)

ReserveBook = Button(Left_App_Frame,text='Reserve a Book',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_RESERVEBOOK)
ReserveBook.place(x=22,y=210)

ReturnReservation = Button(Left_App_Frame,text='Return a Book',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_DEVOLVEBOOK)
ReturnReservation.place(x=22,y=260)

BooksInReserve = Button(Left_App_Frame,text='Edit informations',bg=light_Gray_dark,relief='groove',fg=white,font='Ivy 12 bold',width=16,command=CHANGE_EDIT)
BooksInReserve.place(x=22,y=310)

User_In_Moment = Label(Left_App_Frame,text='',fg=white,font='Ivy 12 bold',bg=light_Gray_dark)
User_In_Moment.place(x=22,y=360)

#User_In_MomentIMG = Label(Left_App_Frame,image=Images('user.png')) não estão funcionando por enqt
#User_In_MomentIMG.place(x=20, y=360)

# -- Right Up Frame: Label,Image
Name_App_Label = Label(RightUp_App_Frame,text='Virtual Library Management System',fg=white,font='Ivy 25 bold',bg=light_Blue)
Name_App_Label.place(x=120,y=10)

#Image_App_Label = Label(RightUp_App_Frame,image=Images('logo.png')) não estão funcionando por enqt
#Image_App_Label.place(x=50, y=10)

# -- Right Down Frame: Label,Buttons,Entrys,etc
DescriptionName_Label = Label(top_frame,text='',fg=black,font='Ivy 15 bold',bg=white,anchor=W)
Info1_Label = Label(down_frame,text="",fg=black,font='Ivy 15 bold',bg=white,anchor=W)
Info2_Label = Label(down_frame,text="",fg=black,font='Ivy 15 bold',bg=white,anchor=W)
Info3_Label = Label(down_frame,text="",fg=black,font='Ivy 15 bold',bg=white,anchor=W)
Info4_Label = Label(down_frame,text="",fg=black,font='Ivy 15 bold',bg=white,anchor=W)
Info6_Label = Label(down_frame,text="",fg=black,font='Ivy 15 bold',bg=white,anchor=W)

Info1_Entry = Entry(down_frame,fg=black,font='Ivy 15 bold',bg=white)
Info2_Entry = Entry(down_frame,fg=black,font='Ivy 15 bold',bg=white)
Info3_Entry = Entry(down_frame,fg=black,font='Ivy 15 bold',bg=white)
Info4_Entry = Entry(down_frame,fg=black,font='Ivy 15 bold',bg=white)
Info6_Entry = Entry(down_frame,fg=black,font='Ivy 15 bold',bg=white)

Save_Info = Button(down_frame,text='Save',bg=light_Gray_dark,relief='flat',fg=white,font='Ivy 13 bold',width=10,command=REGISTERUSER)
Change_Info = Button(down_frame,text='Change \nreserve date',bg=light_Gray_dark,relief='flat',fg=white,font='Ivy 11 bold',width=10,command=lambda:CHANGE_RESERVEBOOK(True))

column = ("ID","Name","Author","Publisher","Year","Reserved?","Reserve Date")
tree = ttk.Treeview(down_frame,columns=column,show="headings",height=15)

# Remove Variables
Info5_Label = Label(top_frame,text="",fg=black,font='Ivy 7 bold',bg=white,anchor=W)
Info5_Entry = Entry(top_frame,fg=black,font='Ivy 6 bold',bg=white)
Remove_Info = Button(top_frame,bg=light_Gray_dark,relief='flat',fg=white,font='Ivy 10 bold',width=10)
Correct_Info = Button(top_frame,bg=light_Gray_dark,relief='flat',fg=white,font='Ivy 10 bold',width=10)

window.mainloop()
import mysql.connector 
from mysql.connector import Error

user_in_moment = ''

def Login_FUNCTION(emailuser,password):
    global user_in_moment

    # Váriavel que cria a checagem das informações
    check = False

    # Variável para verificar se o usuário tem adm
    ADM = None

    # Criação da variável None
    user = None

    # Pega TODAS as linhas no comando select
    rows = get_lines('users')[1]
    print(rows)

    # Loop para checar se as informações de Login estão corretas
    for row in rows:
        if row[2] == emailuser and row[3] == password:
            check = True
            ADM = row[4]
            user = row[1]
        elif row[1] == emailuser and row[3] == password:
            check = True
            ADM = row[4]
            user = row[1]
    user_in_moment = user
    return (check,ADM,user)

def SignUp_FUNCTION(user,email,password,ADM=0):
    if user == '' or email == '' or password == '': # Verifica se os campos não estão vazios antes de cadastrar
        return 'Some of the fields are empty'
    else:
        try:
            cursor = conn.cursor()
            rows = get_lines('users')[1] # Pega todas as linhas, para no futuro serem contadas e servirem para nunca falhar na hora de adcionar um id novo
            
            ids_existentes = sorted(row[0] for row in rows)
            menor_id = 1
            for id_existente in ids_existentes:
                if menor_id == id_existente:
                    menor_id +=1
                else:
                    break

            cursor.execute(f'INSERT INTO users VALUES ("{menor_id}","{user}","{email}","{password}","{ADM}")')
        except Error as e:
            # Verifica qual das informações já está na database, se não for esse o erro, printa no cmd.
            rows = get_lines('users')[1]
            for row in rows:
                if email == row[2]:
                    return ('This email is already registered.')
                elif user == row[1]:
                    return ('This username is already registered.')
                
            print(f'Error: {e}')
        else:
            return True

def create_connection(db_name):
    # Tenta criar uma conexão
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=f'{db_name}')
            
    # Se der erro, printa o erro
    except Error as e:
        print(f'Error: {e}')
        print(f'That is not possible to connect to {db_name}' )

    # Se não der erro, retorna a conexão e avisa que foi possível conectar   
    else:
        print(f'That is possible to connect to {db_name}') 
        return connection
        
def insert_table_books(name,author,publisher,year):
    check = True
    if name == '' or author  == '' or publisher  == '' or year == '':
        return 'Some of fields are empty'
    else:
        try:
            cursor = conn.cursor()
            rows = get_lines('books')[1] # Usa a função get_lines, que poupa algumas linhas

            #Verifica se as informações ja não estão na database, de modo que dê para adicionar livros meso tendo mesma editora, editoras diferentes, nomes iguais co editoras diferentes, etc
            for row in rows:
                if row[1] == name and row[3] == publisher:
                    check = False
                    print('false')
                elif (row[1] != name and row[3] == publisher) or (row[1] == name and row[3] != publisher) or (row[1] != name and row[3] != publisher):
                    check = True
                    print('true')
            # Se passar pela verificação roda o comando, se não diz q o livro ja foi registrado
            if check:
                ids_existentes = sorted(row[0] for row in rows)
                menor_id = 1
                for id_existente in ids_existentes:
                    if menor_id == id_existente:
                        menor_id +=1
                    else:
                        break
                cursor.execute(f'INSERT INTO books VALUES ("{menor_id}","{name}","{author}","{publisher}","{year}","{0}","{None}")') # 0 para não reservado e 1 para reservado
            else:
                return 'This book is already registered!'
        except Error as e:
            print(e)
            #print('.eaeaee')
            return e
        else:
            return True
        
def reserve_a_book(id,name,publisher,date,update='no'):
    check = True
    if id == '' or name == '' or publisher == '' or date == '':
        return 'Some of the field is empty'
    else:
        try:
            cursor = conn.cursor()
            rows = get_lines('books')[1]

            if len(rows) == 0:  # Verifica se existe algum livro n o banco de dados
                check = False
                return f"Don't exist books registered"
            
            for row in rows: # Verifica se o livro já não está registrado
                if row[5] == 1 and update == 'no':
                    check = False
                    return 'This book was already reserved'
            if check:
                cursor.execute(f'UPDATE BOOKS SET RESERVED = 1 WHERE ID = "{id}" and name = "{name}" and publisher = "{publisher}"')
                cursor.execute(f'UPDATE BOOKS SET DATE = "{date}" WHERE ID = "{id}" and name = "{name}" and publisher = "{publisher}"')
        except Error as e:
            print(e)
        else:
            return True
        
def desreserve_a_book(id,name,publisher):
    check = True
    if id == '' or name == '' or publisher == '':
        return 'Some of the field is empty'
    else:
        try:
            cursor = conn.cursor()
            rows = get_lines('books')[1]

            if len(rows) ==0:
                check = False
                return f"Don't exist books registered"
            
            for row in rows:
                if row[5] == 0:
                    check = False
                    return 'This book was not reserved'
                
            if check:
                cursor.execute(f'UPDATE BOOKS SET RESERVED = 0 WHERE ID = "{id}" and name = "{name}" and publisher = "{publisher}"')
                cursor.execute(f'UPDATE BOOKS SET DATE = "{None}" WHERE ID = "{id}" and name = "{name}" and publisher = "{publisher}"')
        except Error as e:
            print(e)
        else:
            return True
        
def update_date_reserved(id,name,publisher,date):
    check = True
    if id == '' or name == '' or publisher == '':
        return 'Some of the field is empty'
    else:
        try:
            cursor = conn.cursor()
            rows = get_lines('books')[1]

            if len(rows) ==0:
                check = False
                return f"Don't exist books registered"
            
            for row in rows:
                if row[5] == 1:
                    check = False
                    return 'the book is already at that date'
                
            if check:
                cursor = conn.cursor()
                cursor.execute(f'UPDATE BOOKS SET DATE = "{date}" WHERE ID = "{id}" and name = "{name}" and publisher = "{publisher}"')
        except Error as e:
            print(e)
        else:
            return 'Succesful the book are registered!'

def delete(this,id):
    global user_in_moment
    check = True
    if this == '' or id == '':
        return (False,'Some of the field is empty')
    else:
        try:
            # remove o s final das palavras books e users pra fins estéticos (ficar mais bonito) 
            this1 = [this[count] for count in range(0,len(this)) if count != len(this)-1]
            this1 = ''.join(this1)

            cursor = conn.cursor()
            rows = get_lines(f'{this}')[1]

            if len(rows) ==0:
                check = False
                return (False,f"Don't exist {this} registered")
            print(user_in_moment)

            for row in rows:
                if id == row[0]:
                    check = False
                    return (False,f"This {this1} don't exist")
                '''if user_in_moment == row[1] and this.upper() == 'USERS':
                    return (False,f"YOU CAN'T DELETE THE USER THAT YOU ARE USING")'''
                
            if check:
                cursor.execute(f'DELETE FROM {this} WHERE ID = "{id}"')
        except Error as e:
            print(e)
        else:
            return (True,'')
        
def edit(this,id,val1,val2,val3,val4=None):
    check = True
    # Existem duas opções ou estamos editando a tabela books ou a users, e como cada uma tem quantidades diferentes, a val4 pode ou não ser usada
    if this == 'books':
        if id == '' or val1 == '' or val2 == ''or val3 == ''or val4 == '':
            return 'Some of the field is empty'
    elif this == 'users':
        if id == '' or val1 == '' or val2 == ''or val3 == '':
            return 'Some of the field is empty'
        
    try:
        cursor = conn.cursor()
        rows = get_lines(f'{this}')[1]

        if len(rows) == 0:
            return (False,f"Don't exist books registered")
        
        if this == 'books':
            cursor.execute(f'UPDATE {this} SET NAME = "{val1}", AUTHOR = "{val2}", PUBLISHER = "{val3}", YEAR = "{val4}" where id = {id}')

        elif this == 'users':
            print(val4)
            if val4 not in (0,1,'0','1'):
                return (False,'The field "ADM" only can be 0 or 1')
            else:
                cursor.execute(f'UPDATE {this} SET USER = "{val1}", EMAIL = "{val2}", PASSWORD = "{val3}", ADM = "{val4}" where id = {id}')

    except Error as e:
        print(e)
        return (False,e)
    else:
        return (True,'The informations are updated!')

def get_lines(local): # Pega uma tabela e retorna suas informações
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {local.upper()}')
        rows = cursor.fetchall()
    except Error as e:
        return (False, e)
    return (True,rows)

def CorrectIds(this):
    try:
        cursor = conn.cursor()
        rows = get_lines(f'{this}')[1]
        for row in rows:

            # Pega o menor id
            ids_existentes = sorted(row2[0] for row2 in get_lines(f'{this}')[1])
            menor_id = 1
            for id_existente in ids_existentes:
                if menor_id == id_existente:
                    menor_id +=1
                else:
                    break

            if this == 'BOOKS':
                cursor.execute(f'DELETE FROM BOOKS WHERE ID = "{row[0]}"')
                cursor.execute(f'INSERT INTO BOOKS VALUES ("{menor_id}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}")')
            elif this == 'USERS':
                cursor.execute(f'DELETE FROM USERS WHERE ID = "{row[0]}"')
                cursor.execute(f'INSERT INTO USERS VALUES ("{menor_id}","{row[1]}","{row[2]}","{row[3]}","{row[4]}")')
    except Error as e:
        print(e)
    else:
        return True


conn = create_connection('biblioteca')
'''cursor = conn.cursor()
cursor.execute(f'INSERT INTO users VALUES ("{1}","admin","admin@admin.com","admin","{1}")')'''

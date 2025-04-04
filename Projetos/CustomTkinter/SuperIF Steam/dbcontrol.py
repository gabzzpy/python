import mysql.connector
from mysql.connector import Error
from string import ascii_letters,punctuation

def create_conntection(database):
    try:
        connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database=f'{database}')
    except Error as e:
        print('ERRO:', e)
        print('Não deu pra conectar')
    else:
        print('Conectou men')
        return connection
    
def create_user(user='',email='',senha=''):
    print('Chegou na dbcontrol')
    print(user,email,senha)
    CorrigirIDS_Usuário()
    if user == '' or email == '' or senha == '':
        print(user, email, senha)
        return (False,'Existe alguma informação faltando')
    if user.strip() == '' or email.strip() == '' or senha.strip() == '':
        return(False,'Os valores não podem ser em branco')
    if " " in user or " " in email or " " in senha:
        return (False, 'Os valores não podem conter espaços')
    try:
        cursor = database.cursor()
        rows = get_lines('USERS')
        cursor.execute(f'INSERT INTO USERS (usuario,email,senha,admin) VALUES ("{user}","{email}","{senha}","{0}")')
    except Error as e:
        for row in rows:
            print(row)
            if email == row[2] and user == row[1]:
                return (False,'Já existe esse email e username cadastrados')
            if email == row[2]:
                return (False,'Já existe esse email cadastrado')
            if user == row[1]:
                return (False,'Já existe um usuário cadastrado com esse username')
            
        print('ERRO:', e)
        print('Não criou o usuário men :< )')
    
    else:
        print('Deu bom men, criou ai')
        return (True,'Usuário Criado com Sucesso!')
    
def create_game(nome,genero,desenvolvedor,data,sinopse,imagem):
    try:
        cursor = database.cursor()
        rows = get_lines('JOGOS')
        for row in rows:
            if nome == row[1]:
                print('Já existe um jogo com esse nome')
                return (False,'Já existe um jogo com esse nome') 
        query = """
        INSERT INTO JOGOS (nome, genero, desenvolvedor, data_de_lançamento, sinopse, imagem)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nome, genero, desenvolvedor, data, sinopse, imagem))

        database.commit()
    except Error as e:
        print('ERRO:', e)
        print('Não criou o jogo men :< )')
        return (False,'Informações Inválidas')
    
    else:
        CorrigirIDS()
        print('Deu bom men, criou ai')
        return (True,'Jogo Criado com Sucesso!')

def edit_game(edit_or_remove='',what='',where='',change=''):
    print('Chegou na dbcontrol')
    jogo_encontrado = jogo_editado =False
    try:
        cursor = database.cursor()
        rows = get_lines('JOGOS')
        if len(rows) == 0:
            print('Não tem jogo men :()')
            return (False,'Não existe nenhum jogo cadastrado')
        for row in rows:
            print(where, 'nome:',row[1],'id:',row[0],'mudança:',change)
            print(edit_or_remove)
            print(where == row[1])
            
            if where == row[1] or where == str(row[0]):
                jogo_encontrado = True

            if where == row[1]:
                if edit_or_remove == 'remove':
                    cursor.execute(f'DELETE FROM JOGOS where NOME = "{where}"')
                    cursor.execute(f'DELETE FROM BIBLIOTECA where jogo_id = "{row[0]}"')
                    jogo_editado = True

                if edit_or_remove == 'editar':
                    if what == 'data_de_lançamento':
                        check_data = CorrigirDATA(change)

                        if not check_data[0]:
                            return check_data
                    
                    cursor.execute(f'UPDATE JOGOS SET {what} = "{change}" WHERE NOME = "{where}"')
                    jogo_editado = True
                database.commit()

            elif where == str(row[0]):
                if edit_or_remove == 'remove':
                    print('Deletou')
                    cursor.execute(f'DELETE FROM JOGOS where ID = "{where}"')
                    cursor.execute(f'DELETE FROM BIBLIOTECA where jogo_id = "{where}"')
                    jogo_editado = True

                if edit_or_remove == 'editar':
                    if what == 'data_de_lançamento':
                        check_data = CorrigirDATA(change)

                        if not check_data[0]:
                            return check_data

                    cursor.execute(f'UPDATE JOGOS SET {what} = "{change}"  WHERE ID = "{where}"')
                    jogo_editado = True

                database.commit()
                 
    except Error as e:
        print('ERRO:', e)
        print(f'Não foi possivel {edit_or_remove} um jogo')
        return (False,f'Não foi possivel {edit_or_remove} um jogo')
    
    else:

        if not jogo_encontrado:
            return (False, 'Não existe um jogo com esse nome/id')

        if not jogo_editado:
            return (False, 'Nenhuma alteração foi feita')
        
        CorrigirIDS()
        if edit_or_remove == 'remove':
            print(f'Deu bom men, removeu o jogo ai')
            return (True,f'Jogo foi removido com Sucesso!')
        if edit_or_remove == 'editar':
            print(f'Deu bom men, editou o jogo ai')
            return (True,f'Jogo foi editado com Sucesso!')

def CorrigirDATA(data):
    if len(data) != 10 or data[4] != '-' or data[7] != '-':
        return (False, 'Formato de data inválido. Use YYYY-MM-DD') 
                        
    try:
        ano = int(data[0:4])
        mes = int(data[5:7])
        dia = int(data[8:10])
    except:
        return (False,'Os valores tem que ser números. Use YYYY-MM-DD')
    
    if int(mes) not in range(1, 13):
        return (False, 'O mês não foi colocado corretamente')

    meses_31 = [1, 3, 5, 7, 8, 10, 12]
    meses_30 = [4, 6, 9, 11]


    if mes in meses_31 and not (1<= dia <= 31):
        return (False, 'Este mês tem no máximo 31 dias')
    if mes in meses_30 and not (1<= dia <= 30):
        return (False, 'Este mês tem no máximo 30 dias')
    if mes == 2:
        ano_eh_bissexto = ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))
        print(ano_eh_bissexto)
        if ano_eh_bissexto and not (1<= dia <= 29):
            return (False, f'Fevereiro tem no máximo 29 dias, esse ano é bissexto')
        if not ano_eh_bissexto and not (1<= dia <= 28):
            return (False, f'Fevereiro tem no máximo 28 dias, esse ano não é bissexto')
                        
    for n in data:
        if n == '-':
            continue
        elif n in punctuation or n in ascii_letters:
            return (False,'A data não foi colocada corretamente')
                        
    print(data)    
    print('data colocada de maneira correta!')
    return (True,'Data Colocada com Sucesso!')

def CorrigirIDS():
    try:
        cursor = database.cursor()
        rows = get_lines('JOGOS')

        ids_antigos = {}
        contador = 0
        for row in rows:
            contador+=1
            ids_antigos[row[0]] = contador

        for id_antigo, id_novo in ids_antigos.items():
            cursor.execute(f"UPDATE BIBLIOTECA SET jogo_id = '{id_novo}' WHERE jogo_id = '{id_antigo}'")

        cursor.execute('DELETE FROM JOGOS')
        contador = 0
        for row in rows:
            contador +=1
            query = """
            INSERT INTO JOGOS (id,nome, genero, desenvolvedor, data_de_lançamento, sinopse, imagem)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (contador,row[1], row[2], row[3], row[4], row[5], row[6]))

    except Error as e:
        print('Deu erro em corrigir os IDS', e)

def CorrigirIDS_Usuário():
    try:
        cursor = database.cursor()
        rows = get_lines('USERS')
        cursor.execute('DELETE FROM USERS')
        contador = 0
        for row in rows:
            contador +=1
            query = """
            INSERT INTO USERS (id,usuario, email, senha, admin)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (contador,row[1], row[2], row[3], row[4]))

    except Error as e:
        print('Deu erro em corrigir os IDS DO USER', e)

def CorrigirIDS_Biblioteca():
    try:
        cursor = database.cursor()
        rows = get_lines('BIBLIOTECA')
        cursor.execute('DELETE FROM BIBLIOTECA')
        contador = 0
        for row in rows:
            contador +=1
            query = """
            INSERT INTO BIBLIOTECA (id,usuario_id,jogo_id,transacao)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (contador,row[1], row[2], row[3]))

    except Error as e:
        print('Deu erro em corrigir os IDS DA BIBLIO', e)

def edit_user(user_old='',user='',senha='',email=''):
    if user == '' or senha == '' or email == '':
        return (False,'Existe alguma informação faltando')
    if user.strip() == '' or senha.strip() == '' or email.strip() == '':
        return(False,'Os valores não podem ser em branco')
    if " " in user or " " in senha or " " in email:
        return (False, 'Os valores não podem conter espaços')
    try:
        cursor = database.cursor()
        rows = get_lines('USERS')
        if len(rows) == 0:
            print('Não tem usuário men :()')
            return (False,'Não existe nenhum usuário cadastrado')
        
        id = None
        for row in rows:
            if user_old == row[1]:
                id = row[0]
    
                if user == '':
                    user = row[1] 
                if email == '':
                    email = row[2]  
                if senha == '':
                    senha = row[3]

            elif (user == row[1] or email == row[2]) and user_old != row[1]:
                return (False,'Já existe um usuário com essas informações')
        
        if id == None:
            return (False, 'Usuário antigo não encontrado')

        cursor.execute(f'UPDATE USERS SET usuario = "{user}", email = "{email}", senha = "{senha}" WHERE ID = "{id}"')
        database.commit()
    except Error as e:
        return (False,f'Erro: {e}')
    else:
        return (True,'Atualizado com sucesso')

def create_bibliouser(id_jogo,id_user,text):
    try:
        cursor = database.cursor()
        rows = get_lines('BIBLIOTECA')
        for row in rows:
            if id_user == row[1] and id_jogo == row[2]:
                print('Já está salvo essa transação na db')
                return (False,'Esse jogo já está salvo na sua biblioteca') 
            
        query = """
        INSERT INTO BIBLIOTECA (usuario_id, jogo_id, transacao)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (id_user,id_jogo, text))
        print(id_jogo,id_user,text)

        database.commit()
    except Error as e:
        print('ERRO:', e)
        print('Não add o jogo men :< )')
        return (False,'Informações Inválidas')
    
    else:
        print('Deu bom men, add ai')
        CorrigirIDS_Biblioteca()
        return (True,'Jogo Adicionado com Sucesso na Biblioteca!')

def Mudar_Horas_Jogadas(id,tempo):
    if id == '' or tempo == '':
        return (False,'Existe alguma imformação faltando')
    if tempo.strip() == '':
        return(False,'Os valores não podem ser em branco')
    if " " in tempo:
        return (False, 'Os valores não podem conter espaços')
    try:
        cursor = database.cursor()
        rows = get_lines('BIBLIOTECA')
        if len(rows) == 0:
            print('Não tem jogo na biblioteca men :()')
            return (False,'Sei nem como caralhos vc fez isso mano')
        
        try:
            int(tempo)
        except:
            return (False,'Digite um número!')

        for row in rows:
            if id == row[0]:
                cursor.execute(f'UPDATE BIBLIOTECA SET tempo_jogado = "{tempo}" WHERE ID = "{id}"')

                database.commit()
    except Error as e:
        return (False,f'Erro: {e}')
    else:
        return (True,'Atualizado com sucesso')

def get_lines(table):
    try:
        cursor = database.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
    except Error as e:
        print('ERRO:', e)
        print('Deu erro no get lines men')
    else:
        return rows

database = create_conntection('SuperIFsteam')
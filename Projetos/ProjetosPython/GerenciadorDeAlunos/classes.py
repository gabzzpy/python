class Turma:
    _max_alunos = 30

    def __init__(self,turma,qnt_alunos=0):
        self._turma = turma
        self._qtd_alunos = qnt_alunos
        self._lista_de_alunos = {}
        self._professor = {}

    def AdicionarAluno(self,Aluno):
        if self._qtd_alunos < Turma._max_alunos:
            self._qtd_alunos += 1
            Aluno._Turma = self._turma
            Aluno._id = self._qtd_alunos
            self._lista_de_alunos[Aluno._id] = Aluno
            print(f'Aluno {Aluno._nome} {Aluno._sobrenome} adicionado com Sucesso!')
        else:
            print(f'Permissão Negada! Máximo de Alunos atingida {self._qtd_alunos}/{self._max_alunos}')
    
    def AdicionarProfessor(self,Professor):
        self._professor[f'{Professor._materia}'] = f'{Professor._nome} {Professor._sobrenome}'
        Professor._Turma.append(self._turma)
        print(f'Professor de {Professor._materia}: {Professor._nome} {Professor._sobrenome} adicionado com sucesso')

    def MostrarAlunos(self):
        print('-=-' * 10)
        print(f'{"Lista de Alunos".center(30)}')
        for c in range(self._qtd_alunos):
            print(f'Aluno {c + 1} : {self._lista_de_alunos[c + 1]._nome} {self._lista_de_alunos[c + 1]._sobrenome}')
        print('-=-' * 10)

    def CadastrarBimestre(self):
        for x,y in self._lista_de_alunos.items():
            y._bimestre[f'{len(y._bimestre)+1}'] = y._notas.copy()
                
    # def CorrigirIds(self):

class Aluno:
    def __init__(self,nome,sobrenome,idade,id=0):
        self._nome = nome
        self._sobrenome = sobrenome
        self._Turma = 0
        self._idade = idade
        self._id = id
        self._bimestre = {}
        self._notas = {}


    def MostrarNotas(self):
        l=0
        print('-=-'*10)
        for k,v in self._bimestre.items():
            l+=1
            print()
            print(f'{l}º Bimestre'.center(30))
            for x,y in v.items():
                print(f'{x} : {y}')
        print('-=-'*10)
        

class Professor:
    def __init__(self,nome,sobrenome,idade,materia):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._Turma = []
        self._materia = materia

    def AdicionarNota(self,Aluno,nota,Turma):
        if Turma not in self._Turma and Turma != Aluno._Turma:
            print('Você não pode realizar a ação.')
        else:
            Aluno._notas[self._materia] = nota

    

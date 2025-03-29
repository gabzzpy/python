from classes import Turma,Aluno,Professor
Turma1 = Turma('2º AgroV')
Claudenor = Professor('Claudenor','Silva',42,'Matemática')
Norma = Professor('Norma','Mendes',44,"Biologia")
João_Holanda = Aluno('João','Holanda',16)
Gabriel = Aluno('Gabriel','Monteiro',15)
Turma1.AdicionarAluno(Gabriel)
Turma1.AdicionarAluno(João_Holanda)
Turma1.AdicionarProfessor(Claudenor)
Turma1.AdicionarProfessor(Norma)
Claudenor.AdicionarNota(João_Holanda, 10, '2º AgroV')
Norma.AdicionarNota(João_Holanda, 10,'2º AgroV')
Turma1.CadastrarBimestre()
Claudenor.AdicionarNota(João_Holanda, 9, '2º AgroV')
Norma.AdicionarNota(João_Holanda, 9, '2º AgroV')
Turma1.CadastrarBimestre()
João_Holanda.MostrarNotas()
Turma1.MostrarAlunos()











'''Turma1 = Turma('1º Info')
Gabriel = Aluno('Gabriel','Monteiro',15)
Claudenor = Professor('Claudenor','Silva',42,'Matemática')
Albenes = Professor('Albenes','',30,'Física')
Turma1.AdicionarAluno(Gabriel)
Turma1.AdicionarProfessor(Claudenor)
Turma1.AdicionarProfessor(Albenes)

Claudenor.AdicionarNota(Gabriel,10,'1º Info')
Albenes.AdicionarNota(Gabriel,9,'1º Info')
Turma1.CadastrarBimestre(Gabriel,'1º Info',Claudenor)

Claudenor.AdicionarNota(Gabriel,10,'1º Info')
Albenes.AdicionarNota(Gabriel,9,'1º Info')
Turma1.CadastrarBimestre(Gabriel,'1º Info',Claudenor)

Claudenor.AdicionarNota(Gabriel,10,'1º Info')
Albenes.AdicionarNota(Gabriel,9,'1º Info')
Turma1.CadastrarBimestre(Gabriel,'1º Info',Claudenor)

Claudenor.AdicionarNota(Gabriel,10,'1º Info')
Albenes.AdicionarNota(Gabriel,9,'1º Info')
Turma1.CadastrarBimestre(Gabriel,'1º Info',Claudenor)

Gabriel.MostrarNotas()'''






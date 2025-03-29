
# Funcionario é superclasse(mãe) de gerente(subclasse/filha)
class Funcionario:
    def __str__(self):
        return f'< Instância de {self.__class__.__name__}; endereço {id(self)}>'
        # Muda como sai o jeito da execução print(Funcionario)
    
    def __init__(self,nome,cpf,salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def get_bonitifcacao(self):
        return self._salario *0.10

class Gerente(Funcionario):

    def __init__(self,nome,cpf,salario, senha, qtd_funcionarios):
        super().__init__(nome,cpf,salario) #Funcionario.__init__(nome,cpf,salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios
    
    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso Permitido')
            return True
        else:
            print('Acesso Negado')
            return False

    def get_bonitifcacao(self):
        return self._salario *0.15 # pode ser super().getbonificacao() + 1000 por exemplo
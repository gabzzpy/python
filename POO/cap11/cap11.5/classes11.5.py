
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

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes =0):
        self._total_bonficacoes = total_bonificacoes
    
    def registra(self,funcionario):
        self._total_bonficacoes += funcionario.get_bonitifcacao()

    @property
    def total_bonificacoes(self):
        return self._total_bonficacoes

# Outros exemplos com Cliente, e como fazer para apenas funcionarios ou qualuqer tipo de classe poder estar no Controle De Bonificações

if __name__ == '__main__':
    funcionario = Funcionario('João', '111111111-11', 2000.00)
    print("bonificacao	funcionario:	{}".format(funcionario.get_bonitifcacao()))
    gerente = Gerente('José', '222222222-22', 5000.0, '1234', 0)
    print("bonificacao	gerente:	{}".format(gerente.get_bonitifcacao()))
    controle = ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    print("total:	{}".format(controle.total_bonificacoes))





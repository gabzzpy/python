import datetime
class Historico(): # A classe histórico compõe a classe Conta
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transações = []
        
    def imprime(self):
        print(f'Data de Abertura: {self.data_abertura}\nTransações: ')
        for t in self.transações:
            print('-', t)

class Cliente():
    def __init__(self, nome, sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta():
    _total_contas = 0
    
    __slots__ = ['_numero','_titular','_saldo', '_limite','historico'] #Exclui o metodo __dict__ da classe

    def __init__(self,numero,Cliente,saldo=0.0,limite=1000.0):
        Conta._total_contas +=1
        self._numero = numero
        self._titular = Cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,saldo):
        if saldo <0:
            print('Não é possível ter saldo negativo')
        else:
            self._saldo = saldo

    @staticmethod # classmethod
    def get_total_contas(): # Colocaria cls aqui, caso fosse usar o classmethod
        return Conta._total_contas

    def Depositar(self,valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo < valor:
            print('Não foi possivel executar a operação')
        else: 
            self._saldo -= valor
        
    def extrato(self):
        print(f'Cliente: {self._titular.nome} {self._titular.sobrenome}\nNúmero: {self._numero} \nSaldo: {self._saldo}')

    def	transfere(self,	destino,valor):
        retirou = self.sacar(valor)
        if retirou == False:
            return False
        else:
            destino.Depositar(valor)
            self.historico.transações.append(f'Transferencia de R${valor} para {destino.numero}')
            return True

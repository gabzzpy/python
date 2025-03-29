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
    def __init__(self,numero,Cliente,saldo=0.0,limite=1000.0):
        Conta._total_contas +=1
        self.numero = numero
        self.titular = Cliente
        self._saldo = saldo
        self.limite = limite
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

    # @classmethod  // Mesam coisa, faz a msm coisa do static method soq chamando cls e pode mudar coisas da instancia da classe
    @staticmethod #// Staticmeyhod, funciona para chamar esse metodo sem  precisar criar uma classe dele, chamando tipo Conta.get_total_contas()
    def get_total_contas(): # Colocaria cls aqui, caso fosse usar o classmethod
        return Conta._total_contas

    def Depositar(self,valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            print('Não foi possivel executar a operação')
        else: 
            self.saldo -= valor
        
    def extrato(self):
        print(f'Cliente: {self.titular.nome} {self.titular.sobrenome}\nNúmero: {self.numero} \nSaldo: {self.saldo}')

    def	transfere(self,	destino,valor):
        retirou = self.sacar(valor)
        if retirou == False:
            return False
        else:
            destino.Depositar(valor)
            self.historico.transações.append(f'Transferencia de R${valor} para {destino.numero}')
            return True

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
    def __init__(self,numero,Cliente,saldo,limite=1000.0):
        self.numero = numero
        self.titular = Cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def Depositar(self,valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            print('Não foi possivel executar a operação')
        else: 
            self.saldo -= valor
        
    def extrato(self):
        print(f'Número: {self.numero} \nSaldo: {self.saldo}')

    def	transfere(self,	destino,valor):
        retirou = self.sacar(valor)
        if retirou == False:
            return False
        else:
            destino.Depositar(valor)
            self.historico.transações.append(f'Transferencia de R${valor} para {destino.numero}')
            return True

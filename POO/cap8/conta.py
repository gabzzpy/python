from classes8 import Conta, Cliente
cliente1 = Cliente('João', 'Holanda',111111111-11)
conta1 = Conta('123-4', cliente1, 120.0, 1000.0)
conta2 = Conta('123-5', 'Maria', 130.0, 900.0)
conta3 = Conta('123-6', 'Hélio', 130.0)

conta1.transfere(conta2,100)
print(conta1.saldo)
print(conta1.historico)
print(conta2.saldo)
print(conta1.historico.imprime())
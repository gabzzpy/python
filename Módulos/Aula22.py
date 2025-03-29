import Moedas
print('Desafio107')
p = float(input('Digite o preço: R$ '))
print(f'''A metade de {p} é {Moedas.metade(p)}
O dobro de {p} é {Moedas.dobro(p)}
Aumentando 10% de {p}, temos {Moedas.aumentar(p,10)}
Reduzindo 13% de {p}, temos {Moedas.diminuir(p,13)}
''')


print('Desafio108')
from Moedas import aumentar, diminuir, metade,dobro, moeda
p = float(input('Digite o preço: R$ '))
print(f'''A metade de {moeda(p)} é {moeda(metade(p))}
O dobro de {moeda(p)} é {moeda(dobro(p))}
Aumentando 10% de {moeda(p)}, temos {moeda(aumentar(p,10))}
Reduzindo 13% de {moeda(p)}, temos {moeda(diminuir(p,13))}
''')

print('Desafio109')
import Moedas
p = float(input('Digite o preço: R$ '))
print(f'''A metade de {Moedas.moeda(p)} é {Moedas.metade(p,True)}
O dobro de {Moedas.moeda(p)} é {Moedas.dobro(p,True)}
Aumentando 10% de {Moedas.moeda(p)}, temos {Moedas.aumentar(p,10,True)}
Reduzindo 13% de {Moedas.moeda(p)}, temos {Moedas.diminuir(p,13,True)}
''')

print('Desafio110')
p = float(input('Digite o preço de: R$'))
Moedas.resumo(p,20,12)

print('Desafio111')
from utilidades import moedas

p = float(input('Digite o preço de: R$'))
moedas.resumo(p,20,12)

print('Desafio112')
from Módulos.utilidades import moedas, dado
p = dado.leiaDinheiro('Digite o preço: R$')
moedas.resumo(p,20,12)
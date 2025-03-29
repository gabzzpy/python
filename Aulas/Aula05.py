potato= input('Digite qualquer fuckin coisa')
print(potato)
print(potato.isnumeric)

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1 + n2
print('A soma entre {} e {} é: {}' .format(n1, n2,  soma), end= '') # Assim a linha não se quebra
print('A \n soma é: {}! ' .format( soma ))
# Para quebrar alguma linha '\n' para não quebrar ' , end='' '
# Pode-se colocar mais de um valor no .format
# como por exemplo:
# print('A soma entre {} e {} é: {}') . format(n1, n2,  soma)
# isalpha é pra saber se é letra, isnumeric é rpa saber se é numérico
# mas so da rpa usar quando não tem um int, float, bool ou srt

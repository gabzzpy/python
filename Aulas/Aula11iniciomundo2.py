 #Cores no terminal, não é essencial, ok?
# Ordem dps do '[' é style, text, background // Para mais cores, tem que se importar uma biblioteca de cores
# style: 0, 1, 4, 7 // o = none, 1 = negrito, 4 = sublinhado, 7 vai inverter as cores 
# text: 30 - 37// 30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = rosa, 36 = ciano(aqua), 37 = cinza
# background: 40 - 47 // msm ordem da de cima, so muda que é de 40 - 47
# ANSI, ESCAPE SEQUENCE começa com \033[0;33;44;m]
#\033[4;31;45m]
a = 3
b = 5
print('Os valores são \033[7;30m{}\033[m e \033[1;37m{}\033[m'.format(a, b))
      

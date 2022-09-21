import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, math.trunc(num)))
# Podendo também usar 'from math import trunc' e remover math. do .format
# Pode também apenas usar '.format(num, int(num))' sem precisar importar o módulo math

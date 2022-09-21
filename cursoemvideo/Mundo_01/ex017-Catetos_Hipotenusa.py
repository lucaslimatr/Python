import math
# Sem importação
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi1 = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa 1 vai medir {:.2f}'.format(hi1))

# Com importação usando as mesmas variáveis
hi2 = math.hypot(co, ca)
print('A hipotenusa 2 vai medir {:.2f}'.format(hi2))

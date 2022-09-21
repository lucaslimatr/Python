s = float(input('Quanto o funcionário Lucas recebe por mês? R$'))
# Considerar aumento de 15%
print('Lucas recebe R${:.2f}.\nA partir do próximo mês receberá R${:.2f}.'.format(s, (s + s * 15 / 100)))

dis = float(input('Distância do trajeto: '))
if dis <= 200:
    print('O valor da sua passagem é de R${}.'.format(dis * 0.5))
else:
    print('O valor de sua passagem é de R${}.'.format(dis * 0.45))

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua nota foi {}. Média abaxido de 5.0:\nREPROVADO'.format(m))
elif 5 < m < 6.9:
    print('Sua nota foi {}. Média entre 5.0 e 6.9:\nEM RECUPERAÇÃO'.format(m))
elif 6.9 < m < 9.9:
    print('Sua nota foi {}. Média entre 7.0 e 9.9:\nAPROVADO'.format(m))
else:
    print('Nota máxima, você tirou 10!\nPARABÉNS')

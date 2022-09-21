print('=' * 29)
print('BEM-VINDO À TABUADA DIGITAL')
n1 = int(input('Qual será o multiplicador? '))
print('=' * 29)
for n2 in range(1, 11):
    print('{} x {:2} = {:2}'.format(n1, n2, n1 * n2))
print('=' * 11)

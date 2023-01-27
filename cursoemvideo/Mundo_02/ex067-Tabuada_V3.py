while True:
    print('-' * 35)
    mult = int(input('Deseja ver a tabuada de quanto? '))
    print('-' * 35)
    if mult < 0:
        break
    for c in range (1, 11):
        print(f'{mult} x {c} = {mult * c}')
print('FIM')

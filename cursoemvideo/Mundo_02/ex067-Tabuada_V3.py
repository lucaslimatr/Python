mult = 0
while True:
    print('-' * 35)
    mult = int(input('Deseja ver a tabuada de quanto? '))
    print('-' * 35)
    if mult < 0:
        break
    print(f'{mult} x 1 = {mult * 1}\n{mult} x 2 = {mult * 2}\n{mult} x 3 = {mult * 3}\n{mult} x 4 = {mult * 4}\n{mult} x 5 = {mult * 5}')
    print(f'{mult} x 6 = {mult * 6}\n{mult} x 7 = {mult * 7}\n{mult} x 8 = {mult * 8}\n{mult} x 9 = {mult * 9}\n{mult} x 10 = {mult * 10}')
print('FIM')

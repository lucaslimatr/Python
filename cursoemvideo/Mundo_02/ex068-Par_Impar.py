from time import sleep
from random import randint
num = comp = soma = escolha = result = cont = 0
while True:
    if result == 'PERDEU':
        break
    escolha = int(input('Quer IMPAR ou PAR? [1 = IMPAR |2 = PAR]: '))
    comp = randint(0, 10)
    num = int(input('Escolha um número: '))
    soma = comp + num
    if escolha == 1:
        if soma % 2 == 0:
            result = 'PERDEU'
        elif soma % 2 != 0:
            result = 'GANHOU'
    if escolha == 2:
        if soma % 2 == 0:
            result = 'GANHOU'
        elif soma % 2 != 0:
            result = 'PERDEU'
    cont += 1
    print(f'Escolhi {comp}')
    if result == 'GANHOU':
        print(f'Você {result}, Mizeravi! Vamos de novo!')
    sleep(1)
print('PERDEU MANÉ!')
print(f'Você ganhou {cont} vezes!')

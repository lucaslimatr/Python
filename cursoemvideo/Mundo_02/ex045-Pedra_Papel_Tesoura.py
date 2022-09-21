from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual você escolhe? '))
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOUUUUU', end='')
sleep(0.5)
print('RA')
sleep(0.5)
print('-=' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')

from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador "pensar"
print('-=-' * 19)
print('Vou pensar em um número emtre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em qual número pensei? '))
print('PROCESSANDO...')
sleep(1)  # sleep é uma contagem de tempo
if jogador == computador:
    print('{}! Você acertou!'.format(computador))
else:
    print('Errou! Eu pensei no número {} e não no {}!'.format(computador, jogador))

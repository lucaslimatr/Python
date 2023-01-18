from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
op = 0
r = 0
while op != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('>>> Qual é a operação que deseja? '))
    if op == 1:
        r = n1 + n2
        print('O resultado de {} + {} é {}.'.format(n1, n2, r))
    elif op == 2:
        r = n1 * n2
        print('O resultado de {} * {} é {}.'.format(n1, n2, r))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:
        print('Finalizando processo...')
    else:
        print('Opção inválida!')
    print('=-= ' * 9)
    sleep (1)
print('FIM')

num = maior = menor = media = soma = cont = 0
n = False
while not n:
    num = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        maior = num
        menor = num
        soma = num
    else:
        soma += num
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    n = input('Deseja continuar [S/N]? ').lower().strip()[0]
    if n == 'n':
        n = True
    else:
        n = False
media = soma / cont
print('A média de todos os valores é {}.\nO maior número foi {}.\nO menor número foi {}. '.format(media, maior, menor))


    

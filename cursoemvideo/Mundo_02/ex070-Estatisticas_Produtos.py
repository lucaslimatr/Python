from time import sleep
total = cont = contpreco = menor_valor = mais_barato = 0
print('~' * 20,'\nLISTA DE PRODUTOS')
print('~' * 20)
while True:
    prod = input('Digite o nome do produto: ').upper().strip()
    preco = float(input('Digite o valor do produto: '))
    continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
    cont += 1
    while continuar not in 'SN':
        print('Opção inválida')
        sleep(1)
        continuar = input('Deseja continuar [S/N]? ').upper().strip()[0]
    total += preco
    if preco > 1000:
        contpreco += 1
    if cont == 1 or preco < menor_valor:
        menor_valor = preco
        mais_barato = prod
    if continuar == 'N':
        break
print('~' * 20)
print(f'Total gasto na compra: R${total:.2f}\n{contpreco} produtos custam mais de R$1000.00')
print(f'O mais barato foi: {mais_barato} - R${menor_valor:.2f}')
preco = float(input('Qual o preço do produto? '))
pag = str(input('Qual a forma de pagamento? ')).upper()
if pag == 'CARTAO':
    parc = int(input('Quer parcelar em quantas vezes? '))
    if parc == 1:
        preco = preco - (preco * (5 / 100))
    elif parc > 2:
        preco = preco + (preco * (20/100))
else:
    preco = preco - (preco * (10/100))
print('O total da sua compra é de R${:.2f}.\nObrigado pela preferência!'.format(preco))

valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Quanto é o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
num_pres = anos * 12
valor_pres = valorcasa / num_pres
print('Veja a simulação do seu emprestimo:')
print('{} prestações no valor de {:.2f} ao mês.'.format(num_pres, valor_pres))
if valor_pres <= (salario * (30 / 100)):
    print('Empréstimo aprovado! Em até 24h o saldo estará liberado para transferência.')
else:
    print('Empréstimo negado! Valor a ser pago por parcela está abaixo do permitido de até 30% do salário.')

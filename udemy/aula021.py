nome = 'Luiz'
idade = int(32)
altura = float(1.8)
peso = float(80)
ano_atual = int(2022)
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.0f}kg.')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')

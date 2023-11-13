# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)
print('')

# Lucas tem 25 anos de idade, tem 1.72 de altura
# pesa 62 quilos 

nome = 'Lucas'
idade = int(25)
altura = float(1.72)
peso = float(62)
ano_atual = int(2023)
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.2f}kg.')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')

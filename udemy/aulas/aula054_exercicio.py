"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    teste_par_impar = numero_int % 2 == 0

    if teste_par_impar:
        print(f'O número {numero_int} é par.')
    else:
        print(f'O número {numero_int} é ímpar.')
except:
    print(f'{numero} não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Informe as horas: ')
# hora_int = int(hora[0:2])

# if hora_int <= 11:
#     print(f'Bom dia! São {hora} horas.')
# elif hora_int >= 12 and hora_int <= 17:
#     print(f'Boa tarde! São {hora} horas.')
# else:
#     print(f'Boa noite! São {hora} horas.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input('Digite seu primeiro nome: ')
# qtd_letras = len(nome)

# if qtd_letras <= 4:
#     print(f'Olá, {nome}! Seu nome é curto!')
# elif qtd_letras >= 5 and qtd_letras <= 6:
#     print(f'Olá, {nome}! Seu nome é normal!')
# else:
#     print(f'Olá, {nome}! Seu nome é grande!')

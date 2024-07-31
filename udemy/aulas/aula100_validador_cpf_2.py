"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf_recebido ='74682489070'

# Validador do primeiro dígito
cpf = cpf_recebido[:9]
multiplicador = 10
soma = 0
resultado = 0
primeiro_digito = 0
for n in cpf:
    num_cpf = int(n) * multiplicador
    multiplicador -= 1
    soma = soma + num_cpf
    print(f'Número do CPF:', num_cpf,f'Soma:', soma)
resultado = (soma * 10) % 11
print(f'Resultado:', resultado)

primeiro_digito = resultado if resultado < 9 else 0
print(F'Primeiro Digito:', primeiro_digito)

# Validador do segundo dígito
cpf_2 = cpf_recebido[:10] # Apenas alterei o fatiamento de 9 para 10
multiplicador_2 = 11 # Apenas alterei o multiplicador de 10 para 11
soma_2 = 0
resultado_2 = 0
segundo_digito = 0 # Alterei o nome da variável
for n in cpf_2:
    num_cpf = int(n) * multiplicador_2
    multiplicador_2 -= 1
    soma_2 = soma_2 + num_cpf
    print(f'Número do CPF:', num_cpf,f'Soma:', soma_2)
resultado = (soma_2 * 10) % 11
print(f'Resultado:', resultado_2)

segundo_digito = resultado_2 if resultado_2 < 9 else 0
print(F'Segundo Digito:', segundo_digito)

# Validador do CPF 
validacao = f'{cpf}{primeiro_digito}{segundo_digito}'

if cpf_recebido == validacao:
    print(f'{cpf_recebido} é válido!')
else:
    print(f'CPF inválido!')

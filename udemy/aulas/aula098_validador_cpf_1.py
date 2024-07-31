"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# Jeito que eu fiz a variável: cpf = [7, 4, 6, 8, 2, 4, 8, 9, 0]
digitos ='74682489070'
cpf = digitos[:9]
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
    

import random

for _ in range(100):
    cpf_recebido = ''
    for i in range(9):
        cpf_recebido += str(random.randint(0, 9))
    # print(cpf_recebido)

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

    resultado = (soma * 10) % 11   

    primeiro_digito = resultado if resultado < 9 else 0

    # Validador do segundo dígito
    cpf_2 = cpf_recebido[:10] # Apenas alterei o fatiamento de 9 para 10
    multiplicador_2 = 11 # Apenas alterei o multiplicador de 10 para 11
    soma_2 = 0
    resultado_2 = 0
    segundo_digito = 0 # Alterei o nome da variável

    for n2 in cpf_2:
        num_cpf_2 = int(n2) * multiplicador_2
        multiplicador_2 -= 1
        soma_2 = soma_2 + num_cpf_2

    resultado_2 = (soma_2 * 10) % 11

    segundo_digito = resultado_2 if resultado_2 < 9 else 0
    
    # CPF gerado
    validacao = f'{cpf}{primeiro_digito}{segundo_digito}'

    print(validacao)

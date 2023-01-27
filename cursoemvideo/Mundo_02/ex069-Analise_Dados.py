from time import sleep
nome = idade = sexo = continuar = cont18 = homem = mulher = 0
print('~' * 20)
print('CADASTRO DE PESSOAS')
print('~' * 20)
while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Informe o sexo [M/F]: ').upper().strip()[0]
    while sexo not in ['M', 'F']:
        print('Opção inválida')
        sleep(1)
        sexo = input('Informe o sexo [M/F]: ').upper().strip()[0]
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while continuar not in ['S', 'N']:
        print('Opção inválida')
        sleep(1)
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    print('~' * 20)
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    if continuar == 'N':
        break      
print(f'Neste cadastro, {cont18} pessoas são maiores de 18 anos, tiveram {homem} homens e {mulher} mulheres tem menos de 20 anos')
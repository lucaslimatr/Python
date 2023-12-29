primeiro_numero = 0
segundo_numero = 0
operador = 0
resultado = 0

while True:
    try:
        primeiro_numero = input('Digite um número: ')
        primeiro_numero = int(primeiro_numero)
        
        operador = input('Digite um operador: ')

        segundo_numero = input('Digite um número: ')
        segundo_numero = int(segundo_numero)

        if operador == '+':
            resultado = primeiro_numero + segundo_numero
            print(resultado)
        elif operador == '-':
            resultado = primeiro_numero - segundo_numero
            print(resultado)
        elif operador == '*':
            resultado = primeiro_numero * segundo_numero
            print(resultado)
        elif operador == '/':
            resultado = primeiro_numero / segundo_numero
            print(resultado)
        else:
            print('Operação inválida!')
    except:
        print('Operação inválida!')
    
    continuar = input('Deseja continuar? [S/N] = ').upper().startswith('N')
    if continuar:
        break
print('Fim')

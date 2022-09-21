vel = int(input('Qual a velociadade do carro? '))
print('VOCÊ PASSOU A {}Km/h.'.format(vel))
if vel > 80:
    print('LIMITE DE VELOCIDADE EXCEDIDO. MULTA APLICADA COM SUCESSO!')
    print('SUA MULTA É DE R${:2f}.'.format(float((vel - 80) * 7)))
else:
    print('VELOCIDADE DENTRO DO PERMITIDO. BOA VIAGEM!')

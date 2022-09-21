peso = float(input('Qual é seu peso?(kg) '))
altura = float(input('Qual é a sua altora?(m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do PESO ideal.')
elif 18.5 < imc < 25.1:
    print('Você está no PESO ideal.')
elif 25 < imc < 30.1:
    print('Você está no SOBREPESO.')
elif 30 < imc < 40.1:
    print('VocÊ tem OBESIDADE.')
else:
    print('Você tem OBESIDADE MÓRBIDA.')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    alist = str(input('Você já se alistou? ')).upper()
    saldo = idade - 18
    if alist == 'SIM':
        print('Então, seu ano de alistastamento foi realizado em {}.'.format(atual - saldo))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado à {} anos, em {}.'.format(saldo, (atual - saldo)))

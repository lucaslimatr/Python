from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idd = ano - nasc
if idd < 10:
    print('Sua categoria: MIRIM')
elif 9 < idd < 15:
    print('Sua categoria: INFANTIL')
elif 14 < idd < 20:
    print('Sua categoria: JUNIOR')
elif 19 < idd < 26:
    print('Sua categoria: SÊNIOR')
else:
    print('Sua categoria: MASTER')

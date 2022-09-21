nome = str(input('Digite seu nome completo: '))
print('Seu nome tem {} letras.'.format(len(nome)))# Considerando o espaço entre as palavras
print('Seu em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))# Considerando o nome sem os espaços
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

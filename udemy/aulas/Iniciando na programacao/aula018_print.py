# Argumento sep= vai separar as strings desse print usando o que tiver dentro das aspas
# Argumento end= inclui o que eu quero ao final do print onde ele está e tira a quebra de linha
print('Lucas', 'dos', 'Santos', 'Lima', end='####')
print('Lucas', 'dos', 'Santos', 'Lima', sep='-')

print('824', '176', '070', sep='.', end='-')
print('18')

# \r\n -> CRLF = CR/LF (carriage return AND line feed) - Quebra de linha utilizado no Windows
# \n -> LF - Quebra de linha utilizado no Linux e Mac
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
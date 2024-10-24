# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
resposta = 0
gabarito = 0
qtd_acertos = 0

for p in perguntas:
    print(p['Pergunta'])

    for i, opcao in enumerate(p['Opções']):    
        print(f'{i})', opcao)

    resposta = input('Responda:' )
    gabarito = (p['Resposta'])

    if resposta.isdigit():
        if resposta == gabarito:
            qtd_acertos += 1
            print(f'Parabéns, você acertou!')
        else:
            print(f'Que pena, você errou!')
    else:
        print(f'"{resposta}" não é uma opção válida!')

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')




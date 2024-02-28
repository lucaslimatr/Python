"""
Faça uma lista de compas com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valor da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""
import os

lista = []
while True:
    print('Selecione uma opção')
    acao = input('[i]nseir, [a]pagar, [l]istar: ')

    if acao == 'i':
        os.system('cls')
        valor = input('Digite o nome do produto: ')
        lista.append(valor)
        print(f'{valor} inserido com sucesso.')
    elif acao == 'a':
            indice_str = input('Escolha o índice para apagar: ')
            os.system('cls')
            try:
                indice_str = int(indice_str)
                del lista[indice]
            except ValueError:
                print('Por favor digite número inteiro.')
            except IndexError:
                print('Índice não existe na lista.')
            except Exception:
                print('Erro desconhecido.')
    elif acao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar.')
        for indice, produto in enumerate(lista):
            print(indice, produto)
    
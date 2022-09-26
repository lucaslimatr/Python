import bisect

def valor_honorario(quant_funcionarios: int, faturamento_empresa: float):
    funcionarios = [0, 5, 10, 15, 20]
    faturamento = [0, 100, 500, 1000, 2000]
    preco = [600, 800, 1000, 2000, 3000]
    faixa_funcionario = max(bisect.bisect_left(
        funcionarios, quant_funcionarios), 1)
    faixa_faturamento = max(bisect.bisect_left(
        faturamento, faturamento_empresa), 1)
    valor_funcionario = preco[faixa_funcionario - 1]
    valor_faturamento = preco[faixa_faturamento - 1]
    valor = (valor_funcionario + valor_faturamento) / 2
    print(
        f'De acordo com a quantidade de funcionarios a empresa se enquadra na faixa {faixa_funcionario} o honorario é: {valor_funcionario}')
    print(
        f'De acordo com o faturamento a empresa se enquadra na faixa {faixa_funcionario} o honorario é: {valor_faturamento}')
    print('O honorairio real é: ', valor)

if __name__ == "__main__":
    valor_honorario(16, 650.50)
    valor_honorario(10, 500)
p = float(input('Qual é o preço do produto? '))
# Considerar desconto de 5%
print('Não perca a promoção do dia dos pais.\nCombo Família de R${:.2f}\nPor apenas R${:.2f}'.format(p,
                                                                                                     p - (p * 5 / 100)))

codigo =input('Qual o codigo do produto?')
qtd = input('quantas undidades do produto')
preco = float(input('uqal o preco da unidade do produto'))

codigo2 =input('Qual o codigo do produto?')
qtd2 = input('quantas undidades do produto')
preco2 = float(input('uqal o preco da unidade do produto'))
qtd = float(qtd)
qtd2 = float(qtd2)

total1 = preco * qtd
total2 = preco2 * qtd2
total = total1 + total2

print('valor a pagar: R$',total)
nome = input('qual o seu nome: \n')
salario = float(input('qual o seu salario \n'))
vendas = float(input('Qual o valor tota que voce conseguiu vender? \n'))
bonus = vendas*(15/100)
total = bonus + salario
print('o total do seu pagamento sera de :', total)
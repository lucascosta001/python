d = float(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
# dia = 60 reais
# km rodado = R$0,15
total = (d * 60) + (k * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))

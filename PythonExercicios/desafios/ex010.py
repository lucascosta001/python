dincart = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 3.27
dindolar = dincart / dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(dincart, dindolar))

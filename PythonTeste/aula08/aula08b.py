from math import sqrt, floor
num = float(input('Digite um número: '))
raiz = sqrt(num)
form = floor(raiz)
print('A raiz de {} é igual a {:.2f}'.format(num, form))

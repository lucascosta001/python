n1 = float(input('Digite um valor númerico: '))
n2 = float(input('Digite outro valor númerico: '))
n3 = input('Qual o tipo de operação, ex.: * ;/ ;- ;+:')

if n3 == '+':
    r = n1+n2
elif n3 == '-':
    r = n1-n2
elif n3 == '*':
    r = n1*n2
elif n3 == '/':
    r = n1/n2
else:
    print('Ultilize algum dos operadores indicados!')
    exit()
print(r, end=' ')
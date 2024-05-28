n1 = float(input('Um valor: '))
n2 = float(input('Outro valor: '))
n3 = input('tipo de operação ex.: * ;/ ;- ;+:')

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
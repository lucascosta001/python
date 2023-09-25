nome = input('Qual o nome do aluno? ')
n1 = float(input('Digite a primeira nota do {}: '.format(nome)))
n2 = float(input('Digite a segunda nota do {}: '.format(nome)))
m = (n1 + n2) / 2
print('A média de {} é {:.1f}'.format(nome, m))

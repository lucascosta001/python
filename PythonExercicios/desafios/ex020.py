from random import shuffle
print('Digite os nomes dos Alunos! ')
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)

# Usando alinhamentos e repetições com o '{:}' .format()
nome = str(input('Qual é seu nome? '))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Prazer em te conhecer {:-^20}!'.format(nome))
print('Prazer em te conhecer {:~^20}!'.format(nome))
print('Prazer em te conhecer {:_^20}!'.format(nome))

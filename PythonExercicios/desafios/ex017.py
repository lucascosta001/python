from math import sqrt
ca = int(input('Qual a Medida do Cateto Adjacente: '))
co = int(input('Qual a Medida do Cateto Oposto: '))
h = sqrt((ca * ca) + (co * co))
print('A Hipotenusa do triângulo retâgulo, tendo o Cateto Adjcente {} e o Cateto Oposto {} é {}'.format(ca ,co, h))

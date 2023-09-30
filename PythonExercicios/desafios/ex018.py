from math import cos, sin, tan
angulo = int(input('Informe o ângulo: '))
numsen = sin(angulo)
numcos = cos(angulo)
numtg = tan(angulo)
print('O seno, cosseno e tangente do angulo {} são respectivamente {}, {} e {}'.format(angulo, numsen, numcos, numtg))

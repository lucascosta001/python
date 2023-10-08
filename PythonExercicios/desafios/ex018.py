from math import cos, sin, tan, radians
angulorad = float(input('Informe o ângulo: '))
angulo = radians(angulorad)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(angulo)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(angulo)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan(angulo)))

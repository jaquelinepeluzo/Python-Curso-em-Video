from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input(('Digite o comprimento do cateto adjacente: ')))
print('O triângulo retângulo com cateto oposto {} e cateto adjacente {}, '
      'tem a hipotenusa: {:.2f}'.format(co, ca, hypot(co, ca)))


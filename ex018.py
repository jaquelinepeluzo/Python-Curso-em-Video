from math import sin, cos, tan, radians
a = float(input('Digite o ângulo desejado: '))
r = radians(a)
print('O ângulo digitado é {}, \n seu seno é {:.2f}, '
      '\n seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(a,sin(r),cos(r),tan(r)))
import random
from random import randint
comp = random.randint(0, 6)
num = int(input('Vou pensar em um número entre 0 e 5, tente adivinhar: '))
print('PROCESSANDO...')
print('O número escolhido pelo computador foi: {}'.format(comp))
if num == comp:
    print('Acertou!')
else:
    print('Errou...Tente novamente')

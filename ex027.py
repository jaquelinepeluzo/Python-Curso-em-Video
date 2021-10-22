nome = str(input('Qual é o seu nome completo? ')).strip()
dividido = nome.split()
print('O Primeiro nome é {}'.format(dividido[0]))
print('O último nome é {}'.format(dividido[len(dividido)-1]))

ano = int(input('Digite um ano e saiba se ele é bissexto: '))

if ano % 4:
    print('O ano digitado: {} é bissexto'.format(ano))
else:
    print('O ano digitado: {} não é bissexto'.format(ano))
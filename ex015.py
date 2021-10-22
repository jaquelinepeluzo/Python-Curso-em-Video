kmpercorrido = float(input('Quantos Km você percorreu com o carro: '))
diasusados = int(input('Quantos dias você utilizou o carro? '))
calculo = (diasusados * 60) + (kmpercorrido * 0.15)
print('O carro que foi alugado por {} dias, e rodou {}Km, vai custar: R${:.2f}'.format(diasusados, kmpercorrido, calculo))

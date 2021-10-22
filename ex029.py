vel = float(input('Qual foi a velocidade do carro: '))
multa = 7 * (vel - 80)
if vel >= 81:
    print('Você foi multado! Sua multa custará R$ {:.2f}'.format(multa))
else:
    print('Você não ultrapassou o limite de velocidade, siga viagem!')
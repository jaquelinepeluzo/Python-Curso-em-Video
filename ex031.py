dist = float(input('Quantos KM percorridos na sua viagem? '))

if dist >= 200:
    print('Sua viagem de {:.1f} Km,  custará R$ {:.2f}'.format(dist, dist * 0.50))

else:
    print('Sua viagem de {:.1f} Km, custará R$ {:.2f}'.format(dist, dist * 0.45))
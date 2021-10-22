nome = str(input('Qual é o seu nome? '))
if nome == 'Jaqueline':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))
m = (n1+n2)/2
print('A sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, PARABÉNS!!!')
else:
    print('Você precisa estudar mais')

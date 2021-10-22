salario = float(input('Qual é o seu salário? R$'))
novosalario = salario + (salario * 15) / 10
print('O salário que era R${:.2f} , com o aumento de 15% passa a ser R${:.2f}'.format(salario, novosalario))
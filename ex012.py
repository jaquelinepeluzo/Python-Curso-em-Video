preco = float(input('Digite o valor do produto: R$ '))
desconto = preco - (preco * 5)/100
print('O produto que custa R${:.2f} , com desconto de 5% passa a custar R${:.2f}'.format(preco, desconto))

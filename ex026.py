frase = str(input('escreva uma frase: ')).lower().strip()
print('A Letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição: {}'.format(frase.rfind('a')+1))




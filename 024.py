palavra = input('Escerva uma palavra: ').strip().replace(' ', '')
pontos = 0
for i in range(0, len(palavra)):
    if palavra [i] == palavra[-i -1]:
        pontos = pontos + 1

if pontos == len(palavra):
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

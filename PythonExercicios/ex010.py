real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US$\033[1;31m{:.2f}\033[m'.format(real, dolar))

dol = float(3.27)
dinheiro = float(input('Quanto dinheiro voce tem ? '))
# conversao = dinheiro - dol   #errei o correto é divisão e não substração
conversao = dinheiro / dol
print('Voce pode comprar US {}'.format(conversao))
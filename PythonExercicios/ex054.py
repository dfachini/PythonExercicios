'''
import random

anoatual = 2021
anos = 0

contmaior = 0
contmenor = 0
for i in range(0, 7):
    anos = random.randint(1990, 2020)
    if anoatual - anos >= 21:
        contmaior += 1
        print('Voce é maior de idade. Sua idade é {}'.format(anoatual - anos))
    else:
        contmenor += 1
        print('Voce é menor de idade. Sua idade é {}'.format(anoatual - anos))

print('Total de maiores de idade foi de {} e Total de menores de idade foi de {}.'.format(contmaior, contmenor))
'''

#Resolucao do Professor

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu ? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

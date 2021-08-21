'''
from datetime import date

anocorrente = date.today().year
anonasc = int(input('Digite Ano: '))

idadeatleta = anocorrente - anonasc

if idadeatleta > 0 and idadeatleta <= 9:
    print('MIRIM')
elif 9 < idadeatleta <= 14:
    print('INFANTIL')
elif 14 < idadeatleta <=19:
    print('JUNIOR')
elif 19 < idadeatleta == 20:
    print('SENIOR')
elif idadeatleta > 20:
    print('MASTER')
else:
    print('Valor incorrento. Digite novamente.')
'''

# Resolucao do professor
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

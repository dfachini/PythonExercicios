''' Exercicio de alistamento '''
'''
from datetime import date
nome = 'David'
anonasc = 1987

if (date.today().year - anonasc) < 18:
    falta = 18 - (date.today().year - anonasc)
    print('Faltam {} anos ainda para se alistar {}'.format(falta, nome))
elif (date.today().year - anonasc) == 18:
    print('É a hora de se alistar {}!'.format(nome))
elif (date.today().year - anonasc) > 18:
    passou = (date.today().year - anonasc) - 18
    print('Passaram-se {} anos para se alistar {}. Sinto muito.'.format(passou, nome))
'''

# Resolucao do professor
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
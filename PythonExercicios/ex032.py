'''
ano = str(2025)
unidade = ano[len(ano)-1]
dezena = ano[len(ano)-2]
valorfinal = dezena + unidade
convertido = int(valorfinal)

if (convertido % 4) == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} NÃO é bissexto.'.format(ano))
'''

# Resolucao do professor
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

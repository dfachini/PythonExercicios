'''
num = int(8)
if (num % 2) == 0:
    print('O número é PAR')
else:
    print('O número é ÍMPAR')
'''

# Resolucao do professor
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR.'.format(resultado))
else:
    print('o número {} é ÍMPAR.'.format(resultado))
'''# import math
from math import trunc
print(float(trunc(6.127)))'''

# versao 1 do professor
'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

# Versao 2 do professor (sem importar modulos)
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

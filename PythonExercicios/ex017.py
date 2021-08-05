'''
import math

print('Hipotenusa: {}'.format(math.hypot(55)))

'''

'''
# Maneira tradicional
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)         # raiz quadrada da soma dos quadrados dos catetos
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

#  Maneira usando modulo
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
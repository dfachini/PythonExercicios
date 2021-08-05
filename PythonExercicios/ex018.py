'''
import math

angulo = float(input('Digite o Angulo: '))
print('Baseado no Angulo {}, temos o seno {}, o cosseno {} e a tangente {}'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))

'''

from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Baseado no Angulo {}, temos o seno {:.2f}'.format(angulo, seno))
print('Baseado no Angulo {}, temos o cosseno {:.2f}'.format(angulo, cosseno))
print('Baseado no rAngulo {}, temos a tangente {:.2f}'.format(angulo, tangente))
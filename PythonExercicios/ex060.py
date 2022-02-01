'''
n = 5
resultado = 0
i = 1
mult = 1
desc = n+1
acumulado = 0
print('{}!='.format(n), end="")
while i <= n:
    i += 1
    desc -= 1
    mult *= desc
    print(desc, end="x")
    # print(i, desc, mult)
print('={}'.format(mult))
'''



# Resolução do Professor
'''
from math import factorial

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1  # Sempre que for trabalhar com multiplicação tem que começar com 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
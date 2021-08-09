'''
n1 = 3
n2 = 2
n3 = 1

if n2 < n1 > n3:
    if n2 < n3:
        print('n1 {} é o maior. n2 {} é o menor. n3 {} é do meio.'.format(n1, n2, n3))
    else:
        print('n1 {} é o maior. n3 {} é o menor. n2 {} é do meio.'.format(n1, n3, n2))
if n1 < n2 > n3:
    if n1 < n3:
        print('n2 {} é o maior. n1 {} é o menor. n3 {} é do meio.'.format(n2, n1, n3))
    else:
        print('n2 {} é o maior. n3 {} é o menor. n1 {} é do meio.'.format(n2, n3, n1))
if n1 < n3 > n2:
    if n1 < n2:
        print('n3 {} é o maior. n1 {} é o menor. n2 {} é do meio.'.format(n3, n1, n2))
    else:
        print('n3 {} é o maior. n2 {} é o menor. n1 {} é do meio.'.format(n3, n2, n1))
'''

# Resolucao do professor
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verficando quem é menor
menor = a   # Elegendo um para ser menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))

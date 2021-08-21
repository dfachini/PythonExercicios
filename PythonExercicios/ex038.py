'''
n1 = 3
n2 = 2
# n1 = int(input('n1: '))
# n2 = int(input('n2: '))
tipon1 = type(n1)
tipon2 = type(n2)

if tipon1 == int and tipon2 == int:
    if n1 == n2:
        print('Não existe valor maior, os dois são iguais!')
    elif n1 > n2:
        print('O primeiro valor é maior')
    elif n1 < n2:
        print('O segundo valor é maior')
else:
    print('valor não permitido! Tente novamente.')
'''

# Resolucao do professor
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')

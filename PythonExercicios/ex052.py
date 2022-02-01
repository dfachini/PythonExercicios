
'''
Inicialmente, pedimos um número inteiro e positivo para o usuário e armazenamos na variável n.

Vamos armazenar na variável mult o número de múltiplos que existe de 2 até n-1.

Ou seja, do intervalo (2, 3, 4, ..., n-1)
Isso é obtido usando a função range: range(2,n).

Vamos usar a variável count pra receber cada um desses valores, dentro desse intervalo.

Dentro do looping, temos que testar se o resto da divisão de n por count vai ser 0. Se for, é porque n é múltiplo de count, logo não é primo.

A medida que nosso programa ai encontrando múltiplos, conta eles na variável mult e exibe na tela.

Após terminar o laço, testamos o valor de mult.
Se permanecer zerado, é porque o número fornecido pelo usuário é primo.

'''

# numero inteiro primo ou nao primo
'''
multiplos=0
n = int(input('Digite um numero: '))
for i in range(2, n):
    if (n % i == 0):
        print(i)
        multiplos += 1

if (multiplos==0):
    print('É Primo')
else:
    print('Tem {} multiplos acima de 2 e abaixo de {}'.format(multiplos,n))
'''

# Resolucao do Professor
num =  int(input('Digite um numero: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
       print('\033[33m', end='')
       total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
'''
i = 0
resultado = 1
n = int(input('Quer ver a tabuada de qual valor? '))
print('-'*30)
while n >= 0:
    for i in range(0, 10, 1):
        i = i + 1
        # n *= i
        resultado = i * n
        print(f'{i} x {n} = {resultado}')
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
'''

# Resolucao Professor

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('POGRAMA TABUADA ENCERRADO. Volte sempre!')

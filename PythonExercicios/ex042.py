'''
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Todos os lados são iguais [EQUILÁTERO].')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Dois lados são iguais [ISÓSCELES].')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Todos os lados são diferentes [ESCALENO].')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
'''

# Resolucao do professor
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
'''
a = 2
b = 15
c = 20

if (b - c) < a < b + c:
    if (a - c) < b < a + c:
        if (a -b) < c < a + b:
            print('Juntas as 3 partes formam um triangulo!')
        else:
            print('Juntas as partes NÃO formam um triangulo!')
'''

# Resolucao do professor
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
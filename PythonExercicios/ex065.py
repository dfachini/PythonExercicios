'''
import math
import statistics

i = 0
n = 0
lista = []
menornum = 0
maiornum = 0
quantidadenum = 0
somanumeros = 0

while i < 2:
    n = int(input('Digite numero: '))
    quantidadenum += 1
    i += 1
    maiornum = n # 1
    menornum = n # 1
    if maiornum > menornum:
        somanumeros += maiornum + menornum
        print('maior: {} é maior que menor: {}'.format(maiornum, menornum))
    if maiornum == menornum:
        somanumeros += maiornum + menornum
        print('maior: {} e menor: {} são iguais'.format(maiornum, menornum))
    else:
        somanumeros += maiornum + menornum
        print('menor: {} é maior que maior: {}'.format(menornum, maiornum))
    if i == 2:
        pergunta = str(input('Voce quer continuar? [S/N]: ')).upper()
        if pergunta == 'S':
            i = 0
        else:
            print('Obrigado!')
'''

# Resolucao do Professor

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

'''
from datetime import date

anonasc = int(1937)
peso = float(66)
altura = float(1.78)

idadepessoa = date.today().year - anonasc

if idadepessoa <= 65:
    imc = peso / (altura * altura)
    if imc < 18.5:
        print('Abaixo do Peso.')
    elif 18.5 <= imc < 25:
        print('Peso Ideal.')
    elif 25 <= imc <= 30:
        print('Sobrepeso.')
    elif imc > 40:
        print('Obesidade Mórbida.')
else:
    print('Voce é idoso. Esse calculo nao se enquadra.')
'''

# Resolucao do professor
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)   # altura ao quadrado
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 24 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado.')

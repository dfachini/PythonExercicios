'''
vel = float(input('Velocidade carro: '))
if vel > 80:
    mul = (vel - 80) * 7
    print('A multa vai custar R$ {:.2f}'.format(mul))
else:
    print('Trafegando dentro da velocidade permitida.')
'''

# Resolucao do professor
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade > 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
